# Swapchain and presentation

`VulkanSwapChain` manages surface capabilities, format and presentation mode
selection, swapchain images, image views, optional depth resources, and
framebuffers.

## Create the swapchain

Create it only after initializing a graphics context with a valid surface:

```cpp
core::vulkan::VulkanSwapChain swap_chain(&context, surface);
```

Pass `true` as the third argument when depth buffering is required.

For a traditional render pass, create the matching framebuffers explicitly:

```cpp
core::vulkan::VulkanSwapChain swap_chain(&context, surface, true);
core::vulkan::VulkanRenderPass render_pass(
    &context, swap_chain.swapchain_image_format, true);
swap_chain.CreateFrameBuffers(render_pass);
```

## Frame loop

The windowed examples follow this order:

1. Wait for and reset the in-flight fence.
2. Acquire the next swapchain image.
3. Reset and begin the command buffer.
4. Transition the image for color attachment use.
5. Record rendering commands.
6. Transition the image to `VK_IMAGE_LAYOUT_PRESENT_SRC_KHR`.
7. Submit with acquire and render-finished semaphores.
8. Call `Present()` with the selected image index.

```cpp
uint32_t image_index = 0;
VK_CHECK(vkAcquireNextImageKHR(
    context.logical_device, swap_chain.swapchain, UINT64_MAX,
    image_available.semaphore, VK_NULL_HANDLE, &image_index));

command_buffer.Reset();
VkCommandBufferBeginInfo begin_info{};
begin_info.sType = VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO;
VK_CHECK(vkBeginCommandBuffer(command_buffer.buffer(), &begin_info));

swap_chain.TransitionImageLayout(
    command_buffer.buffer(), image_index,
    VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL);
// Record rendering here.
swap_chain.TransitionImageLayout(
    command_buffer.buffer(), image_index,
    VK_IMAGE_LAYOUT_PRESENT_SRC_KHR);

command_buffer.Submit(
    in_flight_fence.fence,
    core::vulkan::SubmitSyncInfo{
        .wait_semaphores = {image_available.semaphore},
        .wait_stage_masks = {
            VK_PIPELINE_STAGE_COLOR_ATTACHMENT_OUTPUT_BIT},
        .signal_semaphores = {render_finished.semaphore},
    });

const VkResult result =
    swap_chain.Present(image_index, render_finished.semaphore);
```

Applications should check presentation results for errors and
`VK_SUBOPTIMAL_KHR`, and wait for the device before destroying window resources.

```{warning}
The current wrapper does not recreate the swapchain automatically. Handle
`VK_ERROR_OUT_OF_DATE_KHR` and `VK_SUBOPTIMAL_KHR` in the application when the
window is resized or surface properties change. Call `vkDeviceWaitIdle()` before
destroying or replacing resources still used by queued frames.
```

`VulkanSwapChain` tracks each swapchain image's current layout internally. Use its
`TransitionImageLayout()` method for those images so the tracked state remains in
sync with recorded barriers.
