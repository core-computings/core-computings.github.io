# Compute

The compute path combines `VulkanCompute`, buffers, a command buffer, and a fence.
The `ComputeSum` test is the smallest complete example in the repository.

## Define a workload

A derived compute class provides:

- `GetBindingInfo()` for uniform, storage buffer, and image bindings.
- `LoadShaderCode()` for the embedded SPIR-V compute shader.
- An application method that binds the pipeline and descriptors, then calls
  `vkCmdDispatch()`.

Override `Init()` when the workload needs to populate descriptor sets after
`VulkanCompute::Init()` creates the pipeline infrastructure.

```cpp
class AddValues : public core::vulkan::VulkanCompute {
 public:
  AddValues(core::vulkan::VulkanContext* context,
            core::vulkan::VulkanBuffer& input,
            core::vulkan::VulkanBuffer& output)
      : VulkanCompute(context), input_(input), output_(output) {}

  void Init() override {
    VulkanCompute::Init();
    CreateStorageBufferDescriptorSet(0, input_);
    CreateStorageBufferDescriptorSet(1, output_);
    vkUpdateDescriptorSets(context_->logical_device,
                           static_cast<uint32_t>(writes_.size()),
                           writes_.data(), 0, nullptr);
  }

  void Run(VkCommandBuffer command_buffer, uint32_t element_count) {
    vkCmdBindPipeline(command_buffer, VK_PIPELINE_BIND_POINT_COMPUTE,
                      pipeline);
    vkCmdBindDescriptorSets(command_buffer,
                            VK_PIPELINE_BIND_POINT_COMPUTE,
                            pipeline_layout, 0, 1, &descriptor_set_,
                            0, nullptr);
    vkCmdDispatch(command_buffer, (element_count + 255) / 256, 1, 1);
  }

 protected:
  std::vector<core::vulkan::BindingInfo> GetBindingInfo() const override {
    return {
        {0, VK_DESCRIPTOR_TYPE_STORAGE_BUFFER,
         VK_SHADER_STAGE_COMPUTE_BIT},
        {1, VK_DESCRIPTOR_TYPE_STORAGE_BUFFER,
         VK_SHADER_STAGE_COMPUTE_BIT},
    };
  }

 private:
  const std::vector<uint32_t>& LoadShaderCode() const override;
  core::vulkan::VulkanBuffer& input_;
  core::vulkan::VulkanBuffer& output_;
};
```

`LoadShaderCode()` must return storage whose lifetime extends through pipeline
creation. Existing workloads use a function-local `static std::vector<uint32_t>`
containing generated SPIR-V data.

## Dispatch

Choose workgroup counts from the data dimensions and the local size declared in
the shader. `ComputeSum` uses 16 × 16 groups:

```cpp
const uint32_t group_x = (width + 15) / 16;
const uint32_t group_y = (height + 15) / 16;
vkCmdDispatch(command_buffer, group_x, group_y, 1);
```

The division rounds up so partial edge workgroups are included. The shader must
still bounds-check global invocation coordinates before reading or writing data.

## Execute and read back

```cpp
pipeline.Run(command_buffer.buffer(), element_count);
fence.Reset();
command_buffer.Submit(fence.fence);
VK_CHECK(vkWaitForFences(
    context.logical_device, 1, &fence.fence, VK_TRUE, UINT64_MAX));

output_buffer.MapData([&result](void* data) {
  memcpy(result.data(), data, result.size() * sizeof(result[0]));
});
```

```{important}
Waiting on the fence establishes completion of the GPU work, but shader memory
dependencies inside a longer command buffer still require appropriate Vulkan
barriers. The current simple tests dispatch once and wait before reading.
```

## Existing compute coverage

- **ComputeSum** demonstrates uniform and storage buffers.
- **ComputeGaussianBlur** demonstrates image processing.
- **Roofline** measures copy and fused multiply-add workloads.
- **ComputeBarycentricRasterizer** uses compute shaders for rasterization.
