# Linux Namespaces Used

## PID Namespace
Ensures the container sees its own process tree starting from PID 1.

## UTS Namespace
Allows the container to have its own hostname.

## Mount Namespace
Prevents the container from seeing host mounts.

These namespaces together create process-level isolation without
virtualization.
