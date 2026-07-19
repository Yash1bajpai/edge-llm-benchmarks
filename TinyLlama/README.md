# TinyLlama 1.1B

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
