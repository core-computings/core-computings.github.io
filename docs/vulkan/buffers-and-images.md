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

## Images

`VulkanImage` creates the image, memory, and image view as one object. Its API
supports layout transitions, depth layouts, mipmap generation, array layers, and
multisampling.

Use `VulkanBuffer::CopyToImage()` to upload staged pixel data. Use
`VulkanSampler` when the image will be read through a combined image sampler
descriptor.

## Ownership

Both resource wrappers are movable and release their Vulkan objects in their
destructors. Avoid copying them, and keep their `VulkanContext` alive for their
entire lifetime.
