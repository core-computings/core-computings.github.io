# First example

Complete the [installation steps](installation.md) before running an example.


## macOS

From the CORE repository root, download the demo assets and build for macOS:

```bash
./scripts/sync_data.sh
./scripts/run.sh -t macos
./build/macos/examples/vk_triangle_demo
```

The asset sync script requires **Git LFS** and **SSH access** to the
[core_data repository](https://github.com/chuzcjoe/core_data).
Run examples from the repository root so relative asset paths resolve correctly.

## Android

For Android, prepare the NDK using the installation guide, then build with:

```bash
./scripts/run.sh -t arm64-v8a
```

