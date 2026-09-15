# Descriptors and pipelines

`VulkanBase` is the shared foundation for compute and graphics pipelines. It
creates descriptor set layouts, descriptor pools, descriptor sets, pipeline
layouts, and shader modules.

## Declare bindings

Derived workloads implement `GetBindingInfo()` and return one `BindingInfo` per
shader binding:

```cpp
std::vector<core::vulkan::BindingInfo> GetBindingInfo() const override {
  return {
      {0, VK_DESCRIPTOR_TYPE_UNIFORM_BUFFER,
       VK_SHADER_STAGE_COMPUTE_BIT},
      {1, VK_DESCRIPTOR_TYPE_STORAGE_BUFFER,
       VK_SHADER_STAGE_COMPUTE_BIT},
  };
}
```

## Write descriptors

After the base initialization, derived classes use the protected helpers for
uniform buffers, storage buffers, and combined image samplers. Finish by calling
`vkUpdateDescriptorSets()` with the writes assembled by those helpers.

```cpp
void MyComputePipeline::Init() {
  core::vulkan::VulkanCompute::Init();

  CreateUniformBufferDescriptorSet(0, uniform_buffer_);
  CreateStorageBufferDescriptorSet(1, input_buffer_);
  CreateStorageBufferDescriptorSet(2, output_buffer_);

  vkUpdateDescriptorSets(
      context_->logical_device,
      static_cast<uint32_t>(writes_.size()), writes_.data(),
      0, nullptr);
}
```

The sequence matters: the base `Init()` creates the descriptor layout, pool,
set, pipeline layout, and concrete pipeline. The descriptor helper calls then
fill the writes for that allocated set.

## Bind before dispatch or draw

```cpp
vkCmdBindPipeline(
    command_buffer, VK_PIPELINE_BIND_POINT_COMPUTE, pipeline);
vkCmdBindDescriptorSets(
    command_buffer, VK_PIPELINE_BIND_POINT_COMPUTE,
    pipeline_layout, 0, 1, &descriptor_set_, 0, nullptr);
```

Use `VK_PIPELINE_BIND_POINT_GRAPHICS` for a `VulkanRender` subclass.

```{warning}
The binding numbers, descriptor types, and shader stages returned by
`GetBindingInfo()` must match the shader declarations exactly. Also create one
descriptor write for every declared binding before calling
`vkUpdateDescriptorSets()`; the base class sizes its internal arrays from that
declaration.
```

## Specialize the pipeline

- Derive from `VulkanCompute` for one compute shader and a compute pipeline.
- Derive from `VulkanRender` for vertex and fragment shaders and a graphics
  pipeline.

Both base classes expect the application-specific subclass to provide shader code
and binding declarations.

Pipeline objects and their descriptor resources are destroyed by `VulkanBase`.
The buffers, image views, and samplers referenced by a descriptor remain owned by
the application and must stay alive while submitted commands can access them.
