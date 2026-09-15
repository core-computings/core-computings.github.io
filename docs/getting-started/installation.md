# Installation

CORE supports local development on **macOS** and cross-compilation for
**Android arm64-v8a**. Start by cloning the source and initializing its dependencies:

```bash
git clone --recurse-submodules https://github.com/chuzcjoe/CORE.git
cd CORE
```

## Install dependencies with an AI agent

The canonical installation instructions are maintained in
[`docs/install_dependencies.md`](https://github.com/chuzcjoe/CORE/blob/main/docs/install_dependencies.md)
in the CORE repository. Ask an AI coding agent to read that file and prepare the
local machine for the required target.

For a macOS build, send the agent this instruction:

```text
Read docs/install_dependencies.md and prepare this machine to build CORE for
macOS. Work from the CORE repository root, check existing tools before installing
anything, install only missing dependencies, and run the verification and build
steps described in that file.
```

For an Android build, send the agent this instruction:

```text
Read docs/install_dependencies.md and prepare this machine to build CORE for
Android arm64-v8a. Work from the CORE repository root, check existing tools before
installing anything, install only missing dependencies, configure the required
Android SDK and NDK environment variables, and run the verification and build
steps described in that file.
```

```{important}
Treat `docs/install_dependencies.md` as the source of truth. It contains the
supported tool versions, platform-specific setup, permission requirements,
environment variables, verification commands, and build commands.
```
