# Commands and synchronization

`VulkanCommandBuffer` owns a command pool and one primary command buffer for the
queue mode selected by its `VulkanContext`.

## Reusable command buffers

Call `Reset()`, begin the native command buffer, record work, and submit through
one of the `Submit()` overloads. `SubmitSyncInfo` groups wait semaphores, pipeline
stage masks, and signal semaphores for rendering submissions.

## One-time commands

Resource transfers and layout transitions can use:

```cpp
auto command =
    core::vulkan::VulkanCommandBuffer::BeginOneTimeCommands(&context);
// Record transfer or transition commands.
command.EndOneTimeCommands();
```

## Fences and semaphores

- `VulkanFence` lets the CPU wait for a submitted command buffer and can be reset
  before reuse.
- `VulkanSemaphore` orders GPU operations, such as image acquisition, rendering,
  and presentation.

The graphics examples use a fence for frames in flight, an image-available
semaphore, and one render-finished semaphore per swapchain image.
