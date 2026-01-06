# Cgroups v2 Usage

This runtime uses cgroup v2 to limit resource usage.

## Limits Applied
- Memory: 256 MB
- PIDs: 64 processes

## Reasoning
Resource limits prevent containers from exhausting host resources
and are a core part of production container runtimes.
