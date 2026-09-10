# Reflection


## 1. Image vs Container

A Docker image is a read-only template containing the application code, dependencies, and runtime environment. A container is a running instance created from that image with its own isolated process environment.


## 2. One Dockerfile choice

I selected python:3.12-slim as the base image because it provides the required Python environment while keeping the image size smaller. If this was replaced with a full operating system image, the build size and deployment time would increase.


## 3. First error and solution

The first issue occurred because Docker Desktop could not start the Linux engine due to missing virtualization components. The issue was solved by enabling Virtual Machine Platform and configuring WSL2. After restarting Docker Desktop, the container started successfully.
