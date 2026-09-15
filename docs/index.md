<div class="core-eyebrow">COMPUTE AND OPEN RENDERING ENGINE</div>

# CORE: Computing and Rendering

<div class="core-lead">A C++20 framework for GPU computing and rendering across Vulkan, Metal, OpenGL, and OpenCL.</div>

<div class="core-tags"><span>C++20</span><span>macOS</span><span>Android</span><span>Compute + Graphics</span></div>

CORE provides higher-level abstractions over GPU APIs to reduce boilerplate when
building compute and graphics workloads. Start with a working example, then explore
the backend that fits your application.

```{note}
This documentation framework is a preview. The pages contain starter content;
detailed guides and the API reference will follow.
```

## Start here

- [Installation](getting-started/installation.md): prepare your development environment.
- [First example](getting-started/first-example.md): build and run a demo.

## Explore Vulkan

- [Vulkan overview](vulkan/overview.md): understand the module and its workflow.
- [Context and device](vulkan/context-and-device.md): initialize Vulkan and select queues.
- [Buffers and images](vulkan/buffers-and-images.md): manage GPU resources and transfers.
- [Compute](vulkan/compute.md): create and dispatch a compute pipeline.
- [Rendering](vulkan/rendering.md): create graphics pipelines and present frames.

## Other backends

OpenGL, OpenGL ES, OpenCL, and Metal have reserved documentation sections. Their
content will be added as those modules mature.

## Project guides

- [Run tests](development/testing.md): validate your build.
- [Writing documentation](development/documentation.md): add chapters and Markdown pages.

```{toctree}
:hidden:
:caption: Get started
:maxdepth: 1

getting-started/installation
getting-started/first-example
```

```{toctree}
:hidden:
:caption: Vulkan
:maxdepth: 1

vulkan/overview
vulkan/context-and-device
vulkan/buffers-and-images
vulkan/commands-and-sync
vulkan/descriptors-and-pipelines
vulkan/compute
vulkan/rendering
vulkan/swapchain-and-presentation
vulkan/examples
vulkan/testing-and-performance
```

```{toctree}
:hidden:
:caption: OpenGL
:maxdepth: 1

opengl/overview
```

```{toctree}
:hidden:
:caption: OpenGL ES
:maxdepth: 1

opengles/overview
```

```{toctree}
:hidden:
:caption: OpenCL
:maxdepth: 1

opencl/overview
```

```{toctree}
:hidden:
:caption: Metal
:maxdepth: 1

metal/overview
```

```{toctree}
:hidden:
:caption: Project
:maxdepth: 1

development/testing
development/documentation
```
