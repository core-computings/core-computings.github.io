# Context and device

`VulkanContext` owns the Vulkan instance, physical device, logical device, queue
families, queues, and optional debug messenger. Other Vulkan wrappers receive a
pointer to this context and must not outlive it.

## Queue modes

CORE exposes two queue modes through `QueueFamilyType`:

- `Compute` selects a compute queue for headless workloads.
- `Graphics` selects graphics and presentation queues for windowed rendering.

## Compute initialization

```cpp
core::vulkan::VulkanContext context(
    true, core::vulkan::QueueFamilyType::Compute, VK_NULL_HANDLE);
context.Init();
```

The first argument enables validation layers. They are useful during development
and should be selected deliberately by applications.

## Graphics initialization

For rendering, create the platform surface after the context has created its
instance, then finish initialization with that surface:

```cpp
#define GLFW_INCLUDE_VULKAN
#include <GLFW/glfw3.h>

glfwInit();
glfwWindowHint(GLFW_CLIENT_API, GLFW_NO_API);
GLFWwindow* window =
    glfwCreateWindow(800, 600, "CORE Vulkan", nullptr, nullptr);

core::vulkan::VulkanContext context(
    true, core::vulkan::QueueFamilyType::Graphics, VK_NULL_HANDLE);

VkSurfaceKHR surface = VK_NULL_HANDLE;
VK_CHECK(glfwCreateWindowSurface(
    context.instance, window, nullptr, &surface));
context.Init(surface);
```

The constructor creates the Vulkan instance immediately. `Init()` then selects a
physical device, finds the required queue families, creates the logical device,
and retrieves the queues.

## Access queues and device properties

```cpp
const core::vulkan::QueueFamilyIndices indices =
    context.GetQueueFamilyIndices();

VkQueue graphics_queue = context.graphics_queue();
VkQueue present_queue = context.present_queue();
const float timestamp_period_ns = context.timestamp_period;
```

```{note}
The current implementation requests Vulkan 1.3 and selects only devices that
support dynamic rendering, either in Vulkan 1.3 or through
`VK_KHR_dynamic_rendering`. A machine with Vulkan support can still be rejected if
that feature is unavailable.
```

```{warning}
For `QueueFamilyType::Graphics`, pass the real surface to `Init(surface)`.
Presentation support is checked against that surface while the physical device is
selected.
```

## Lifetime rule

Declare the context before buffers, images, pipelines, command buffers, and sync
objects. C++ then destroys the dependent wrappers before destroying the logical
device and instance.

For a windowed application, `VulkanSwapChain` currently owns and destroys the
surface. Destroy the swapchain before the context, and destroy the GLFW window
after the device has become idle.
