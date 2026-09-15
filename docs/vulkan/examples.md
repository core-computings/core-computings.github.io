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
