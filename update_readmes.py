import os

BASE_DIR = r"c:\Yash\edge-llm-benchmarks"

main_readme = """# 📱 Edge LLM Benchmarks: PC vs Android

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
"""

tinyllama_readme = """# TinyLlama 1.1B

TinyLlama is a 1.1B parameter model pre-trained on 3 trillion tokens. Because of its incredibly small footprint, it serves as the perfect baseline for edge devices, embedded systems, and IoT. 

**Edge Capability:** TinyLlama is so lightweight that it can comfortably run at `INT8` (or `Q8_0`) quantization on a standard 6GB RAM phone without triggering Android's OOM killer, leaving plenty of room for system processes.

## Download Links (HuggingFace)
- [TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf)
- [TinyLlama-1.1B-Chat-v1.0.Q8_0.gguf](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q8_0.gguf)

## Benchmarking Results
| Device | Quantization | Size (RAM) | Context | Prompt Processing | Text Generation |
|---|---|---|---|---|---|
| **PC (WSL)** | Q4_K_M | ~682 MiB | 512 | N/A | N/A |
| **Phone** | Q4_K_M | 682 MiB | 512 | 41.21 T/s | 16.58 T/s |
| **Phone** | Q4_K_M | 682 MiB | 1024 | 40.55 T/s | 15.26 T/s |
| **Phone** | INT8 | 1.15 GiB | 512 | 91.97 T/s | 11.42 T/s |

> *Note: The phone achieves blistering 90+ T/s prompt processing speeds on INT8 due to efficient ARM NEON integer math optimizations.*
"""

qwen_readme = """# Qwen 2.5 3B

Qwen 2.5 is Alibaba's latest open-weights model series. The 3B parameter variant is an absolute powerhouse for its size, offering excellent reasoning, coding, and multilingual capabilities that punch far above its weight class.

**Edge Capability:** For a 6GB RAM Android phone, the `Q4_K_M` (1.9 GB) quantization is the absolute sweet spot, running smoothly. However, the `Q8_0` variant (3.16 GB) combined with KV cache pushes the Termux app past Android's memory limits, resulting in an OOM crash.

## Download Links (HuggingFace)
- [Qwen2.5-3B-Instruct-Q4_K_M.gguf](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF/resolve/main/qwen2.5-3b-instruct-q4_k_m.gguf)
- [Qwen2.5-3B-Instruct-Q8_0.gguf](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF/resolve/main/qwen2.5-3b-instruct-q8_0.gguf)

## Benchmarking Results
| Device | Quantization | Size (RAM) | Context | Prompt Processing | Text Generation |
|---|---|---|---|---|---|
| **PC (WSL)** | Q4_K_M | ~1.90 GiB | 256 | 25.35 T/s | 8.16 T/s |
| **PC (WSL)** | Q8_0 | ~3.16 GiB | 256 | 16.59 T/s | 5.37 T/s |
| **Phone** | Q4_K_M | 1.90 GiB | 256 | 17.51 T/s | 5.35 T/s |
| **Phone** | Q8_0 | 3.16 GiB | 256 | 4.38 T/s | **OOM Crash** |
"""

phi_readme = """# Phi-3 Mini 4k

Phi-3 Mini (3.8B parameters) is Microsoft's highly capable SLM trained on heavily filtered "textbook quality" data. It is known for its high reasoning capabilities, matching much larger models in benchmark performance.

**Edge Capability:** Because it sits at nearly 4B parameters, it is the heaviest model tested here. The `Q8_0` version requires almost 4GB of pure available RAM. On a 6GB Android device (where ~2GB is used by the OS), this causes an instant memory limit violation and Termux is killed. `Q4_K_M` runs perfectly.

## Download Links (HuggingFace)
- [Phi-3-mini-4k-instruct-Q4_K_M.gguf](https://huggingface.co/lmstudio-community/Phi-3-mini-4k-instruct-GGUF/resolve/main/Phi-3-mini-4k-instruct-Q4_K_M.gguf)
- [Phi-3-mini-4k-instruct-Q8_0.gguf](https://huggingface.co/lmstudio-community/Phi-3-mini-4k-instruct-GGUF/resolve/main/Phi-3-mini-4k-instruct-Q8_0.gguf)

## Benchmarking Results
| Device | Quantization | Size (RAM) | Context | Prompt Processing | Text Generation |
|---|---|---|---|---|---|
| **PC (WSL)** | Q4_K_M | ~2.32 GiB | 256 | 16.87 T/s | 7.07 T/s |
| **PC (WSL)** | Q8_0 | ~3.90 GiB | 256 | 2.92 T/s | 0.09 T/s |
| **Phone** | Q4_K_M | 2.32 GiB | 256 | 17.38 T/s | 4.90 T/s |
| **Phone** | Q8_0 | 3.90 GiB | 256 | 2.12 T/s | **OOM Crash** |
"""

gemma_readme = """# Gemma-2 2B

Built by Google using the same research and technology as the Gemini models, Gemma-2 2B is a highly efficient model with a unique architecture (2.6B active parameters). It provides excellent conversational and instruction-following abilities.

**Edge Capability:** Gemma-2 strikes an excellent balance of size and intelligence. It processes prompts very quickly on the Snapdragon 695 (~30 T/s for Q4). However, its `Q8_0` size of 2.59 GB plus the KV cache overhead is just enough to trigger Android's OOM killer on a 6GB device. 

## Download Links (HuggingFace)
- [gemma-2-2b-it-Q4_K_M.gguf](https://huggingface.co/bartowski/gemma-2-2b-it-GGUF/resolve/main/gemma-2-2b-it-Q4_K_M.gguf)
- [gemma-2-2b-it-Q8_0.gguf](https://huggingface.co/bartowski/gemma-2-2b-it-GGUF/resolve/main/gemma-2-2b-it-Q8_0.gguf)

## Benchmarking Results
| Device | Quantization | Size (RAM) | Context | Prompt Processing | Text Generation |
|---|---|---|---|---|---|
| **PC (WSL)** | Q4_K_M | ~1.61 GiB | 256 | 39.76 T/s | 8.31 T/s |
| **PC (WSL)** | Q8_0 | ~2.59 GiB | 256 | 36.83 T/s | 5.95 T/s |
| **Phone** | Q4_K_M | 1.61 GiB | 256 | 30.16 T/s | 6.89 T/s |
| **Phone** | Q8_0 | 2.59 GiB | 256 | 3.28 T/s | **OOM Crash** |
"""

with open(os.path.join(BASE_DIR, "README.md"), "w", encoding='utf-8') as f: f.write(main_readme)
with open(os.path.join(BASE_DIR, "TinyLlama", "README.md"), "w", encoding='utf-8') as f: f.write(tinyllama_readme)
with open(os.path.join(BASE_DIR, "Qwen2.5-3B", "README.md"), "w", encoding='utf-8') as f: f.write(qwen_readme)
with open(os.path.join(BASE_DIR, "Phi-3-Mini-4k", "README.md"), "w", encoding='utf-8') as f: f.write(phi_readme)
with open(os.path.join(BASE_DIR, "Gemma-2-2B", "README.md"), "w", encoding='utf-8') as f: f.write(gemma_readme)

print("All READMEs updated successfully.")
