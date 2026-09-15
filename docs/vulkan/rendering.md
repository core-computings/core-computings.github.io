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

```cpp
class TriangleRenderer : public core::vulkan::VulkanRender {
 public:
  TriangleRenderer(core::vulkan::VulkanContext* context,
                   const core::vulkan::DynamicRenderingInfo& info)
      : VulkanRender(context, info) {}

  void Draw(VkCommandBuffer command_buffer, VkExtent2D extent) {
    vkCmdBindPipeline(command_buffer,
                      VK_PIPELINE_BIND_POINT_GRAPHICS, pipeline);

    VkViewport viewport{};
    viewport.width = static_cast<float>(extent.width);
    viewport.height = static_cast<float>(extent.height);
    viewport.maxDepth = 1.0f;
    vkCmdSetViewport(command_buffer, 0, 1, &viewport);

    VkRect2D scissor{{0, 0}, extent};
    vkCmdSetScissor(command_buffer, 0, 1, &scissor);
    vkCmdDraw(command_buffer, 3, 1, 0, 0);
  }

 protected:
  const std::vector<uint32_t> LoadVertexShader() const override;
  const std::vector<uint32_t> LoadFragmentShader() const override;
  std::vector<VkVertexInputBindingDescription>
  GetVertexBindingDescriptions() const override { return {}; }
  std::vector<VkVertexInputAttributeDescription>
  GetVertexAttributeDescriptions() const override { return {}; }
  std::vector<core::vulkan::BindingInfo>
  GetBindingInfo() const override { return {}; }
};
```

## Dynamic rendering

The current triangle example uses `DynamicRenderingInfo` to declare its color
format, then brackets draw commands with `BeginDynamicRendering()` and
`EndDynamicRendering()`.

```cpp
core::vulkan::DynamicRenderingInfo pipeline_info{};
pipeline_info.color_formats = {swap_chain.swapchain_image_format};

TriangleRenderer renderer(&context, pipeline_info);
renderer.Init();

core::vulkan::VulkanDynamicRendering dynamic_rendering(&context);
const VkClearValue clear = {{{0.02f, 0.02f, 0.03f, 1.0f}}};

dynamic_rendering.BeginDynamicRendering(
    command_buffer.buffer(),
    swap_chain.swapchain_image_views[image_index],
    swap_chain.swapchain_extent, clear);
renderer.Draw(command_buffer.buffer(), swap_chain.swapchain_extent);
dynamic_rendering.EndDynamicRendering(command_buffer.buffer());
```

```{warning}
The formats supplied in `DynamicRenderingInfo` are baked into the graphics
pipeline and must match the image views used when rendering. When depth or MSAA
is enabled, pass matching depth, stencil, resolve, and sample-count information.
```

## Traditional render passes

`VulkanRenderPass` creates color and optional depth attachments. Pass it to the
corresponding `VulkanRender` constructor and use swapchain framebuffers when an
application needs the render-pass model.

## Record a draw

Inside the renderer's draw method, bind the graphics pipeline, viewport, scissor,
vertex and index buffers, and descriptor set before issuing `vkCmdDraw*`.

The base renderer uses dynamic viewport and scissor state. Set both during command
recording before drawing. The triangle example also flips the projection matrix's
Y axis because Vulkan's framebuffer coordinate convention differs from GLM's
default projection.
