Minimal Container Runtime

Author: Samir Nimgade
Institute: IIT (ISM) Dhanbad

Overview

A lightweight Linux container runtime built from first principles.
This project re-implements the core ideas behind Docker using Linux namespaces, cgroups v2, and a minimal root filesystem to clearly demonstrate how containers work internally.

Key Features

PID, UTS, and Mount namespace isolation

Minimal Alpine Linux–based root filesystem

Simple CLI to execute arbitrary commands in isolation

Resource control via cgroups v2 (memory, pids)

Re-exec model to create a proper isolated PID 1

Full STDIN / STDOUT / STDERR forwarding to host

Project Structure
minimal-container-runtime/
├── src/            # Runtime, namespaces, cgroups logic
├── scripts/        # Root filesystem setup
├── rootfs/         # Minimal container filesystem
├── notes/          # Design & theory documentation
├── tests/          # Basic runtime tests
├── requirements/   # Python dependencies
└── README.md

Requirements

Linux kernel 5.x or newer

Python 3.9+

cgroups v2 enabled

Root privileges

Root Filesystem Setup
chmod +x scripts/setup_rootfs.sh
./scripts/setup_rootfs.sh

Objective

This project is designed for learning, clarity, and correctness, focusing on how container isolation actually works at the OS level rather than abstract tooling.
