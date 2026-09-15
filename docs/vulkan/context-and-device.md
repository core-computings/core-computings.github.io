# Context and device

`VulkanContext` owns the Vulkan instance, physical device, logical device, queue
families, queues, and optional debug messenger. Other Vulkan wrappers receive a
pointer to this context and must not outlive it.

## Queue modes

CORE exposes two queue modes through `QueueFamilyType`:

- `Compute` selects a compute queue for headless workloads.
- `Graphics` selects graphics and presentation queues for windowed rendering.

## Compute initialization

```cpp
core::vulkan::VulkanContext context(
    true, core::vulkan::QueueFamilyType::Compute, VK_NULL_HANDLE);
context.Init();
```

The first argument enables validation layers. They are useful during development
and should be selected deliberately by applications.

## Graphics initialization

For rendering, create the platform surface after the context has created its
instance, then finish initialization with that surface:

```cpp
core::vulkan::VulkanContext context(
    true, core::vulkan::QueueFamilyType::Graphics, VK_NULL_HANDLE);

VkSurfaceKHR surface = VK_NULL_HANDLE;
// Create the platform surface using context.instance.
context.Init(surface);
```

## Lifetime rule

Declare the context before buffers, images, pipelines, command buffers, and sync
objects. C++ then destroys the dependent wrappers before destroying the logical
device and instance.
