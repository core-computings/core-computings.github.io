# Testing and performance

Vulkan-specific tests live under `vulkan/tests/` and build as the
`vulkan_tests` executable.

## Run the suite

On macOS, use the supported repository command:

```bash
./scripts/run.sh -t macos -r vulkan
```

Android execution additionally requires an authorized device visible to `adb`.

## Test groups

- **ComputeSumTest** validates buffer-based compute and compares the GPU result
  with a CPU sum.
- **ComputeGaussianBlurTest** covers a compute image-processing workload.
- **RooflineTest** exercises copy and fused multiply-add kernels for performance
  analysis.

## GPU timestamps

`VulkanQueryPool` records timestamps at selected pipeline stages and returns the
raw values. Convert their difference using `VulkanContext::timestamp_period` to
measure GPU elapsed time.

```cpp
core::vulkan::VulkanQueryPool query_pool(
    &context, VK_QUERY_TYPE_TIMESTAMP);

query_pool.Reset(command_buffer.buffer());
query_pool.Query(command_buffer.buffer(), 0,
                 VK_PIPELINE_STAGE_COMPUTE_SHADER_BIT);

compute.Run(command_buffer.buffer());

query_pool.Query(command_buffer.buffer(), 1,
                 VK_PIPELINE_STAGE_COMPUTE_SHADER_BIT);
command_buffer.Submit(fence.fence);
VK_CHECK(vkWaitForFences(
    context.logical_device, 1, &fence.fence, VK_TRUE, UINT64_MAX));

query_pool.GetQueryResults();
const std::vector<uint64_t> timestamps = query_pool.GetTimeStamps();
const double elapsed_ms =
    static_cast<double>(timestamps[1] - timestamps[0]) *
    static_cast<double>(context.timestamp_period) / 1'000'000.0;
```

`GetQueryResults()` uses `VK_QUERY_RESULT_WAIT_BIT`, so it may block until results
are available. Waiting on the submission fence first makes that synchronization
explicit in the calling code.

```{important}
Choose timestamp stages around the work being measured. A timestamp at
`BOTTOM_OF_PIPE` measures a different interval from timestamps placed directly at
the compute shader stage. Also verify that the selected device exposes meaningful
timestamp support for the queue family used by the test.
```

Keep correctness assertions separate from timing output so performance changes do
not hide functional failures.
