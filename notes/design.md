# Design Overview – Minimal Container Runtime

## Objective
To build a minimal container runtime that demonstrates how Docker-like
containers work internally using Linux kernel primitives.

## Architecture
The runtime follows a re-exec model:
1. A parent process forks a child.
2. The child re-execs itself to enter container mode.
3. The container init process becomes PID 1.

## Isolation Mechanisms
- **PID Namespace**: Isolates process tree
- **UTS Namespace**: Isolates hostname
- **Mount Namespace**: Isolates filesystem view

## Resource Control
Cgroup v2 is used to apply:
- Memory limits
- Process count limits

## Filesystem
A minimal Alpine Linux root filesystem is used and entered via `chroot`.

## Limitations
This project intentionally excludes networking, image layering,
and OCI compliance to keep the focus on core container mechanics.
