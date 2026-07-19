# Gemma-2 2B

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
