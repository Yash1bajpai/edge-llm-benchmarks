# 📱 Edge LLM Benchmarks: PC vs Android

> A comprehensive benchmark of Small Language Models (SLMs) running locally on constrained edge devices (Android Smartphones) versus PC (WSL), using `llama.cpp`.

![Runtime](https://img.shields.io/badge/Runtime-llama.cpp-green)
![Hardware](https://img.shields.io/badge/Hardware-Android%20%7C%20PC-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 🎯 Project Overview
Running Large Language Models entirely on-device ensures privacy, zero latency, and offline availability. However, mobile devices face severe constraints in **Memory (RAM)** and **Compute (Thermal throttling)**.

This repository benchmarks 4 leading sub-4B parameter models across different quantization levels (`Q4_K_M` vs `Q8_0`/`INT8`) to find the exact deployment limits of a standard mid-range Android phone (6GB RAM, Snapdragon 695).

## 🚀 Models Tested
1. **[TinyLlama 1.1B](./TinyLlama/)**: The ultra-lightweight baseline.
2. **[Qwen 2.5 3B](./Qwen2.5-3B/)**: The intelligent reasoning powerhouse.
3. **[Phi-3 Mini 4K](./Phi-3-Mini-4k/)**: Microsoft's dense textbook-trained model.
4. **[Gemma-2 2B](./Gemma-2-2B/)**: Google's highly efficient 2.6B parameter architecture.

## 🔑 Key Findings (Edge Limitations)
- **The RAM Wall:** A 6GB RAM Android phone only has about **3.0 - 3.5 GB of usable RAM** for user-space applications (Termux) after the OS and background apps take their share.
- **Q4_K_M is the Mobile Sweet Spot:** All tested models (up to 3.8B parameters) successfully run on the Android device using `Q4_K_M` quantization, leaving enough headroom for the KV Cache.
- **Q8_0 Causes Immediate OOM:** Attempting to run `Q8_0` quantizations of models > 2B parameters pushes the RAM usage past the ~3.5GB threshold, resulting in instant Out-Of-Memory (OOM) OS kills during text generation.
- **Prompt Processing Speed:** The Snapdragon 695 CPU (using ARM NEON instructions) achieved impressive prompt processing speeds of ~17 to ~40 Tokens/second depending on the model architecture.

## 📂 Repository Structure
- `scripts/` - Contains generic utility scripts to reproduce these benchmarks or check device specs via SSH.
- `archive_scripts/` - Old debugging and exploratory scripts.
- Model Folders - Each model has a dedicated folder containing specific test scripts, HuggingFace download links, and exact benchmark results.

## 🛠️ Hardware Setup
- **Phone:** iQOO Z7s 5G (Snapdragon 695 "Parrot", 6GB RAM, Android 16, Termux environment)
- **PC:** WSL2 on Windows (CPU Inference)
