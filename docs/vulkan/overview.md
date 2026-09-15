# Vulkan overview

The Vulkan module is currently the most complete backend in CORE. It wraps the
repeated setup and lifetime work around Vulkan while keeping native Vulkan handles
available when an application needs direct API access.

## Module map

| Area | CORE types |
| --- | --- |
| Instance, device, and queues | `VulkanContext` |
| Buffers and images | `VulkanBuffer`, `VulkanImage`, `VulkanSampler` |
| Command recording and submission | `VulkanCommandBuffer` |
| Synchronization | `VulkanFence`, `VulkanSemaphore` |
| Descriptor and pipeline foundation | `VulkanBase` |
| Compute pipelines | `VulkanCompute` |
| Graphics pipelines | `VulkanRender` |
| Render targets | `VulkanDynamicRendering`, `VulkanRenderPass` |
| Window presentation | `VulkanSwapChain` |
| GPU timing | `VulkanQueryPool` |

## Typical compute flow

1. Create a compute `VulkanContext` and call `Init()`.
2. Create input, output, and uniform buffers.
3. Derive a workload from `VulkanCompute` and declare its bindings and shader.
4. Initialize the pipeline and descriptor sets.
5. Record the dispatch into a `VulkanCommandBuffer`.
6. Submit, wait on a fence, and read the result.

## Typical rendering flow

1. Create a window and Vulkan surface.
2. Initialize a graphics `VulkanContext` with that surface.
3. Create `VulkanSwapChain`, command, and synchronization objects.
4. Derive a renderer from `VulkanRender` and initialize its pipeline.
5. Acquire an image, record rendering commands, submit, and present.

Continue with [Context and device](context-and-device.md) for the first layer of
the Vulkan API.
