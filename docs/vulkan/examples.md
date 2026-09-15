# Vulkan examples

The examples form a practical learning path from a single triangle to complete
interactive scenes.

## Recommended order

1. **GLFWWindowDemo** — create a Vulkan-compatible window.
2. **DrawTriangleDemo** — context, swapchain, dynamic rendering, and indexed draw.
3. **DrawTextureDemo** — image upload, sampler, and texture descriptors.
4. **DepthTestingDemo** — depth resources and depth pipeline state.
5. **LoadModelDemo** — model loading and indexed geometry.
6. **MipmapDemo** — mipmap generation and sampled textures.
7. **MultiSamplingDemo** — multisampled rendering and resolve.
8. **CubeMapDemo** — cubemap images and skybox rendering.

## Compute and simulation examples

- **ComputeBarycentricRasterizer** implements rasterization through a compute
  shader.
- **GalaxyDemo** and **PhysicsDemo** demonstrate animated workloads.
- **CarControlDemo** and **FPSShooterDemo** combine several renderers into
  interactive applications.

## Build

```bash
./scripts/sync_data.sh
./scripts/run.sh -t macos
```

Run the selected executable from the CORE repository root so relative shader and
asset paths resolve correctly.

```bash
# Start with the smallest graphics example.
./build/macos/examples/vk_triangle_demo

# Then exercise textures and model resources.
./build/macos/examples/vk_texture_demo
./build/macos/examples/vk_model_demo
```

## Read an example efficiently

For each example, begin with `main.cpp` to see object ownership and the frame
loop. Then inspect its `Render*.h` for the `VulkanRender` specialization and its
`Render*.cpp` for resource upload, descriptor writes, and draw recording.

For example, `DrawTriangleDemo` separates responsibilities like this:

```text
main.cpp
  window + surface → context → swapchain → frame loop

RenderTriangle.cpp
  staging buffers → descriptor set → graphics pipeline → draw commands
```

```{note}
Run examples from the repository root. Several examples depend on relative asset
paths, and `scripts/sync_data.sh` populates assets maintained in the separate
`core_data` repository.
```
