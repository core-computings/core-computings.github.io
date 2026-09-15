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

## Specialize the pipeline

- Derive from `VulkanCompute` for one compute shader and a compute pipeline.
- Derive from `VulkanRender` for vertex and fragment shaders and a graphics
  pipeline.

Both base classes expect the application-specific subclass to provide shader code
and binding declarations.
