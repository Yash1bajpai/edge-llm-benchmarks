# TinyLlama

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
