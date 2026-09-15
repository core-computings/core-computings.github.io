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

Applications should check presentation results for errors and
`VK_SUBOPTIMAL_KHR`, and wait for the device before destroying window resources.
