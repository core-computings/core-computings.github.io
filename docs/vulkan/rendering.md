# Rendering

`VulkanRender` creates a graphics pipeline for either a traditional
`VulkanRenderPass` or `VulkanDynamicRendering`.

## Define a renderer

A renderer subclass provides:

- vertex and fragment SPIR-V through `LoadVertexShader()` and
  `LoadFragmentShader()`;
- vertex buffer and attribute descriptions;
- descriptor bindings through `GetBindingInfo()`.

It may also override culling, front-face orientation, depth testing, depth
writing, and color blending.

## Dynamic rendering

The current triangle example uses `DynamicRenderingInfo` to declare its color
format, then brackets draw commands with `BeginDynamicRendering()` and
`EndDynamicRendering()`.

## Traditional render passes

`VulkanRenderPass` creates color and optional depth attachments. Pass it to the
corresponding `VulkanRender` constructor and use swapchain framebuffers when an
application needs the render-pass model.

## Record a draw

Inside the renderer's draw method, bind the graphics pipeline, viewport, scissor,
vertex and index buffers, and descriptor set before issuing `vkCmdDraw*`.
