# Buffers and images

CORE provides RAII wrappers for the two resource types used throughout its Vulkan
examples: `VulkanBuffer` and `VulkanImage`.

## Buffers

Construct a buffer with its size, usage, and memory properties. Host-visible
buffers can be populated through `MapData()`:

```cpp
core::vulkan::VulkanBuffer input(
    &context, byte_size, VK_BUFFER_USAGE_STORAGE_BUFFER_BIT,
    VK_MEMORY_PROPERTY_HOST_VISIBLE_BIT |
        VK_MEMORY_PROPERTY_HOST_COHERENT_BIT);

input.MapData([&source](void* data) {
  memcpy(data, source.data(), source.size_bytes());
});
```

`CopyToBuffer()` supports staging uploads to device-local buffers.

```cpp
const VkDeviceSize size = vertices.size() * sizeof(vertices[0]);

core::vulkan::VulkanBuffer staging(
    &context, size, VK_BUFFER_USAGE_TRANSFER_SRC_BIT,
    VK_MEMORY_PROPERTY_HOST_VISIBLE_BIT |
        VK_MEMORY_PROPERTY_HOST_COHERENT_BIT);

core::vulkan::VulkanBuffer device_buffer(
    &context, size,
    VK_BUFFER_USAGE_TRANSFER_DST_BIT |
        VK_BUFFER_USAGE_VERTEX_BUFFER_BIT,
    VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT);

staging.MapData([&vertices, size](void* data) {
  memcpy(data, vertices.data(), static_cast<size_t>(size));
});
staging.CopyToBuffer(device_buffer);
```

```{important}
`CopyToBuffer()` requires the source and destination to have exactly the same
size. `MapData()` accepts only memory created with both `HOST_VISIBLE` and
`HOST_COHERENT`; mapping device-local memory throws an exception.
```

## Images

`VulkanImage` creates the image, memory, and image view as one object. Its API
supports layout transitions, depth layouts, mipmap generation, array layers, and
multisampling.

Use `VulkanBuffer::CopyToImage()` to upload staged pixel data. Use
`VulkanSampler` when the image will be read through a combined image sampler
descriptor.

A basic texture upload follows three distinct operations:

```cpp
core::vulkan::VulkanImage texture(
    &context, width, height, VK_FORMAT_R8G8B8A8_SRGB,
    VK_IMAGE_USAGE_TRANSFER_DST_BIT | VK_IMAGE_USAGE_SAMPLED_BIT,
    VK_IMAGE_ASPECT_COLOR_BIT,
    VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT);

texture.TransitionImageLayout(
    VK_IMAGE_LAYOUT_UNDEFINED,
    VK_IMAGE_LAYOUT_TRANSFER_DST_OPTIMAL,
    VK_FORMAT_R8G8B8A8_SRGB);

staging.CopyToImage(texture, width, height);

texture.TransitionImageLayout(
    VK_IMAGE_LAYOUT_TRANSFER_DST_OPTIMAL,
    VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL,
    VK_FORMAT_R8G8B8A8_SRGB);

core::vulkan::VulkanSampler sampler(&context);
```

```{warning}
`TransitionImageLayout()` currently supports a fixed set of color-image
transitions. Unsupported old/new layout pairs throw `std::invalid_argument`.
`CopyToImage()` expects the destination to already be in
`VK_IMAGE_LAYOUT_TRANSFER_DST_OPTIMAL`.
```

For mipmaps, create the image with `TRANSFER_SRC`, `TRANSFER_DST`, and `SAMPLED`
usage flags, allocate all mip levels, upload level 0, and call
`GenerateMipmaps()`. The selected format must support linear blitting.

## Ownership

Both resource wrappers are movable and release their Vulkan objects in their
destructors. Avoid copying them, and keep their `VulkanContext` alive for their
entire lifetime.
