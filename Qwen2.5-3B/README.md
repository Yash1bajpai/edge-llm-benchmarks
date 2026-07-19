# Qwen 2.5 3B

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
