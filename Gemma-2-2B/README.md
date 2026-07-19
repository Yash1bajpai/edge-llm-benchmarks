# Gemma-2 2B

## Download Links (HuggingFace)
- [gemma-2-2b-it-Q4_K_M.gguf](https://huggingface.co/bartowski/gemma-2-2b-it-GGUF/resolve/main/gemma-2-2b-it-Q4_K_M.gguf)
- [gemma-2-2b-it-Q8_0.gguf](https://huggingface.co/bartowski/gemma-2-2b-it-GGUF/resolve/main/gemma-2-2b-it-Q8_0.gguf)

## Benchmarking Results
| Device | Quantization | Size (RAM) | Context | Prompt Processing | Text Generation |
|---|---|---|---|---|---|
| **PC (WSL)** | Q4_K_M | ~1.61 GiB | 256 | 39.76 T/s | 8.31 T/s |
| **PC (WSL)** | Q8_0 | ~2.59 GiB | 256 | 36.83 T/s | 5.95 T/s |
| **Phone** | Q4_K_M | 1.61 GiB | 256 | 30.16 T/s | 6.89 T/s |
| **Phone** | Q8_0 | 2.59 GiB | 256 | 3.28 T/s | OOM Crash |
