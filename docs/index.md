<div class="core-eyebrow">COMPUTE AND OPEN RENDERING ENGINE</div>

# GPU computing, made approachable.

<div class="core-lead">A C++20 framework for GPU computing and rendering across Vulkan, Metal, OpenGL, and OpenCL.</div>

<div class="core-tags"><span>C++20</span><span>macOS</span><span>Android</span><span>Compute + Graphics</span></div>

CORE provides higher-level abstractions over GPU APIs to reduce boilerplate when
building compute and graphics workloads. Start with a working example, then explore
the backend that fits your application.

```{note}
This is the first documentation preview. This page introduces the project and its
basic workflow; detailed guides and the API reference will follow.
```

## Installation

CORE supports local development on **macOS** and cross-compilation for
**Android arm64-v8a**. Start by cloning the source and initializing its dependencies:

```bash
git clone --recurse-submodules https://github.com/chuzcjoe/CORE.git
cd CORE
```

Follow the project's [dependency installation guide](https://github.com/chuzcjoe/CORE/blob/main/docs/install_dependencies.md)
to prepare the tools and SDKs for your target platform before building.

## First example

From the CORE repository root, download the demo assets and build for macOS:

```bash
./scripts/sync_data.sh
./scripts/run.sh -t macos
./build/macos/examples/vk_triangle_demo
```

The asset sync script requires **Git LFS** and **SSH access** to the
[core_data repository](https://github.com/chuzcjoe/core_data).
Run examples from the repository root so relative asset paths resolve correctly.

For Android, prepare the NDK using the installation guide, then build with:

```bash
./scripts/run.sh -t arm64-v8a
```

## Run tests

Use the supported build script to build and run either test suite on macOS:

```bash
# General integration tests.
./scripts/run.sh -t macos -r tests

# Vulkan-specific tests.
./scripts/run.sh -t macos -r vulkan
```

## GPU backends

| Backend | Focus |
| --- | --- |
| **Vulkan** | Explicit GPU computing and rendering |
| **Metal** | Native GPU workflows on Apple platforms |
| **OpenGL** | Desktop graphics |
| **OpenCL** | GPU computing with dynamically loaded OpenCL |

The repository also includes utilities for image and file I/O, math, timing,
tracing, and thread pools. Browse the [source code](https://github.com/chuzcjoe/CORE)
and [examples](https://github.com/chuzcjoe/CORE/tree/main/examples) to explore further.
