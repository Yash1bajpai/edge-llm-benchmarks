# Qwen 2.5 3B

## Download Links (HuggingFace)
- [Qwen2.5-3B-Instruct-Q4_K_M.gguf](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF/resolve/main/qwen2.5-3b-instruct-q4_k_m.gguf)
- [Qwen2.5-3B-Instruct-Q8_0.gguf](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF/resolve/main/qwen2.5-3b-instruct-q8_0.gguf)

## Benchmarking Results
| Device | Quantization | Size (RAM) | Context | Prompt Processing | Text Generation |
|---|---|---|---|---|---|
| **PC (WSL)** | Q4_K_M | ~1.90 GiB | 256 | 25.35 T/s | 8.16 T/s |
| **PC (WSL)** | Q8_0 | ~3.16 GiB | 256 | 16.59 T/s | 5.37 T/s |
| **Phone** | Q4_K_M | 1.90 GiB | 256 | 17.51 T/s | 5.35 T/s |
| **Phone** | Q8_0 | 3.16 GiB | 256 | 4.38 T/s | OOM Crash |
