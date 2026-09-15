# Commands and synchronization

`VulkanCommandBuffer` owns a command pool and one primary command buffer for the
queue mode selected by its `VulkanContext`.

## Reusable command buffers

Call `Reset()`, begin the native command buffer, record work, and submit through
one of the `Submit()` overloads. `SubmitSyncInfo` groups wait semaphores, pipeline
stage masks, and signal semaphores for rendering submissions.

```cpp
core::vulkan::VulkanCommandBuffer command_buffer(&context);
core::vulkan::VulkanFence fence(&context);

command_buffer.Reset();
VkCommandBufferBeginInfo begin_info{};
begin_info.sType = VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO;
VK_CHECK(vkBeginCommandBuffer(command_buffer.buffer(), &begin_info));

// Record vkCmd* operations here.

fence.Reset();
command_buffer.Submit(fence.fence);
VK_CHECK(vkWaitForFences(
    context.logical_device, 1, &fence.fence, VK_TRUE, UINT64_MAX));
```

```{note}
CORE's `Submit()` ends the command buffer internally. Do not call
`vkEndCommandBuffer()` before it. `Reset()` only resets the command buffer; wait
for earlier work that uses it before recording again.
```

## One-time commands

Resource transfers and layout transitions can use:

```cpp
auto command =
    core::vulkan::VulkanCommandBuffer::BeginOneTimeCommands(&context);
// Record transfer or transition commands.
command.EndOneTimeCommands();
```

`EndOneTimeCommands()` submits to the context's selected queue and waits on a
temporary fence. It is convenient for setup operations, but each call blocks the
CPU until that queue completes the command.

## Fences and semaphores

- `VulkanFence` lets the CPU wait for a submitted command buffer and can be reset
  before reuse.
- `VulkanSemaphore` orders GPU operations, such as image acquisition, rendering,
  and presentation.

The graphics examples use a fence for frames in flight, an image-available
semaphore, and one render-finished semaphore per swapchain image.

```cpp
command_buffer.Submit(
    in_flight_fence.fence,
    core::vulkan::SubmitSyncInfo{
        .wait_semaphores = {image_available.semaphore},
        .wait_stage_masks = {
            VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT},
        .signal_semaphores = {
            render_finished[image_index]->semaphore},
    });
```

```{warning}
`wait_semaphores` and `wait_stage_masks` must have the same number of entries.
Keep a render-finished semaphore per swapchain image as the current triangle
example does; reusing a semaphore before presentation has consumed its signal is
invalid.
```
