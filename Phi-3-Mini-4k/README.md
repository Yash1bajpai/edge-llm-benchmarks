# Phi-3 Mini 4k

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
