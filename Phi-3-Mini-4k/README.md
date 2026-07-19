# Phi-3 Mini 4k

## Download Links (HuggingFace)
- [Phi-3-mini-4k-instruct-Q4_K_M.gguf](https://huggingface.co/lmstudio-community/Phi-3-mini-4k-instruct-GGUF/resolve/main/Phi-3-mini-4k-instruct-Q4_K_M.gguf)
- [Phi-3-mini-4k-instruct-Q8_0.gguf](https://huggingface.co/lmstudio-community/Phi-3-mini-4k-instruct-GGUF/resolve/main/Phi-3-mini-4k-instruct-Q8_0.gguf)

## Benchmarking Results
| Device | Quantization | Size (RAM) | Context | Prompt Processing | Text Generation |
|---|---|---|---|---|---|
| **PC (WSL)** | Q4_K_M | ~2.32 GiB | 256 | 16.87 T/s | 7.07 T/s |
| **PC (WSL)** | Q8_0 | ~3.90 GiB | 256 | 2.92 T/s | 0.09 T/s |
| **Phone** | Q4_K_M | 2.32 GiB | 256 | 17.38 T/s | 4.90 T/s |
| **Phone** | Q8_0 | 3.90 GiB | 256 | 2.12 T/s | OOM Crash |
