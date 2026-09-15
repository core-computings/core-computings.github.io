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

## Dispatch

Choose workgroup counts from the data dimensions and the local size declared in
the shader. `ComputeSum` uses 16 × 16 groups:

```cpp
const uint32_t group_x = (width + 15) / 16;
const uint32_t group_y = (height + 15) / 16;
vkCmdDispatch(command_buffer, group_x, group_y, 1);
```

## Existing compute coverage

- **ComputeSum** demonstrates uniform and storage buffers.
- **ComputeGaussianBlur** demonstrates image processing.
- **Roofline** measures copy and fused multiply-add workloads.
- **ComputeBarycentricRasterizer** uses compute shaders for rasterization.
