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

Keep correctness assertions separate from timing output so performance changes do
not hide functional failures.
