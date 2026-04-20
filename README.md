# 🧪 Edge LLM Benchmarks

> Systematically benchmarking quantized Large Language Models for Edge AI deployment — comparing quality degradation across FP16, INT8, INT4, Q4_K_M, and Q5_K_M formats.

![Model](https://img.shields.io/badge/Model-TinyLlama--1.1B-blue)
![Quantization](https://img.shields.io/badge/Quantization-FP16%20%7C%20INT8%20%7C%20INT4%20%7C%20K--Quant-orange)
![Runtime](https://img.shields.io/badge/Runtime-llama.cpp-green)
![HuggingFace](https://img.shields.io/badge/🤗-Models%20on%20HuggingFace-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 🎯 Why This Project?

When deploying LLMs on edge devices (mobile, embedded systems, IoT), memory is the primary constraint. Quantization reduces model size drastically — but at what cost to output quality?

This repo answers that question with **real, reproducible benchmarks** across 5 critical capability dimensions — testing 5 quantization formats on TinyLlama 1.1B.

---

## 📦 Models Tested

| Model | Format | Size | RAM Usage | Download |
|-------|--------|------|-----------|----------|
| TinyLlama-1.1B | FP16 | ~2.2 GB | ~2212 MiB | [🤗 HuggingFace](https://huggingface.co/Yash1bajpai/tinyllama-1.1b-gguf-benchmarks/blob/main/TinyLlama-FP16.gguf) |
| TinyLlama-1.1B | INT8 (Q8_0) | ~1.1 GB | ~1229 MiB | [🤗 HuggingFace](https://huggingface.co/Yash1bajpai/tinyllama-1.1b-gguf-benchmarks/blob/main/TinyLlama-INT8.gguf) |
| TinyLlama-1.1B | INT4 (Q4_0) | ~670 MB | ~744 MiB | [🤗 HuggingFace](https://huggingface.co/Yash1bajpai/tinyllama-1.1b-gguf-benchmarks/blob/main/Tinyllama-INT4.gguf) |
| TinyLlama-1.1B | Q4_K_M | ~750 MB | ~800 MiB | [🤗 HuggingFace](https://huggingface.co/Yash1bajpai/tinyllama-1.1b-gguf-benchmarks/blob/main/TinyLlama-Q4_K_M.gguf) |
| TinyLlama-1.1B | Q5_K_M | ~900 MB | ~950 MiB | [🤗 HuggingFace](https://huggingface.co/Yash1bajpai/tinyllama-1.1b-gguf-benchmarks/blob/main/TinyLlama-Q5_K_M.gguf) |

> All models in GGUF format — ready to run with llama.cpp, no conversion needed.

---

## ⚙️ Setup & Reproduction

```bash
# 1. Clone llama.cpp and build
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build
cmake --build build --config Release

# 2. Download a model from HuggingFace and place in models/

# 3. Run a single prompt
./build/bin/llama-cli -m models/TinyLlama-FP16.gguf --single-turn --seed 42 -n 150 -p "Your prompt here"

# 4. Run full benchmark suite
bash scripts/run_benchmark.sh models/TinyLlama-FP16.gguf FP16

# 5. Create K-Quant versions yourself
./build/bin/llama-quantize models/TinyLlama-FP16.gguf models/TinyLlama-Q4_K_M.gguf Q4_K_M
./build/bin/llama-quantize models/TinyLlama-FP16.gguf models/TinyLlama-Q5_K_M.gguf Q5_K_M
```

---

## 🧩 Benchmark Prompts

| # | Category | Prompt |
|---|----------|--------|
| 1 | 🧠 Logic & Reasoning | Jane has 3 brothers. Each brother has 2 sisters. How many sisters does Jane have? Think step-by-step. |
| 2 | 📋 JSON Formatting | Extract problem/solution strictly as JSON. No other text. |
| 3 | 📝 Constraint Adherence | 2-sentence email. Sentence 1 starts with 'Unfortunately', Sentence 2 with 'However'. |
| 4 | 📖 Reading Comprehension | Summarize JWST passage in exactly 15 words. |
| 5 | 🎭 Creativity & Tone | Grumpy old sailor explains smartphone in exactly 3 sentences. |

---

## 📊 Results — All 5 Quantization Formats

### 1. 🧠 Logic & Reasoning

| Model | Answer | Correct? | Notes |
|-------|--------|----------|-------|
| FP16 | 2 sisters | ✅ | Only model to answer correctly |
| INT8 | 5 sisters | ❌ | Added brothers + sisters incorrectly |
| INT4 (Q4_0) | No answer | ❌ | Looped forever, never concluded |
| Q4_K_M | No answer | ❌ | Looped — step-by-step framework but no conclusion |
| Q5_K_M | No answer | ❌ | Looped — same pattern as Q4_K_M |

**Winner: FP16 only** — K-quants did not improve reasoning over Q4_0.

---

### 2. 📋 JSON Formatting

| Model | Valid JSON? | No Extra Text? | Notes |
|-------|-----------|----------------|-------|
| FP16 | ✅ | ❌ | Markdown wrapper added |
| INT8 | ✅ | ✅ | Best — clean raw JSON |
| INT4 (Q4_0) | ❌ | ❌ | Prose + malformed nested object |
| Q4_K_M | ❌ | ❌ | Prose preamble + truncated JSON |
| Q5_K_M | ❌ | ❌ | Prose preamble + truncated JSON |

**Winner: INT8** — K-quants performed worse than INT8 on structured output.

---

### 3. 📝 Constraint Adherence

| Model | 'Unfortunately' first? | 'However' second? | 2 sentences only? |
|-------|------------------------|-------------------|-------------------|
| FP16 | ✅ | ✅ | ❌ Extra sentences |
| INT8 | ✅ | ✅ | ❌ Extra sentences |
| INT4 (Q4_0) | ❌ | ❌ | ❌ Ignored both |
| Q4_K_M | ❌ | ✅ | ❌ 'Unfortunately' buried in middle |
| Q5_K_M | ❌ | ✅ | ❌ 'Unfortunately' buried in middle |

**Winner: FP16 / INT8 tied** — K-quants partially followed constraints but failed sentence starts.

---

### 4. 📖 Reading Comprehension (15-word limit)

| Model | Word Count | Notes |
|-------|-----------|-------|
| FP16 | ~45 words | Repeated passage verbatim |
| INT8 | ~55 words | Added extra sentence |
| INT4 (Q4_0) | ~40 words | Still far over |
| Q4_K_M | ~40 words | Still far over |
| Q5_K_M | ~35 words | Closest to 15 but still over |

**Winner: Q5_K_M (partial)** — Slightly better compression but no model hit 15 words.

---

### 5. 🎭 Creativity & Tone

| Model | Sailor Persona? | Exactly 3 Sentences? | Notes |
|-------|----------------|----------------------|-------|
| FP16 | ❌ | ❌ (2 sent.) | Factual, no persona |
| INT8 | ❌ | ❌ (2 sent.) | Factual, no persona |
| INT4 (Q4_0) | ❌ | ❌ (4+ sent.) | Went on too long |
| Q4_K_M | ❌ | ❌ (1 sent.) | One giant run-on sentence |
| Q5_K_M | ❌ | ❌ (numbered list) | Formatted as list, no persona |

**Winner: None** — All formats failed. Persona-following needs larger models.

---

## 📈 Full Performance Scorecard

| Category | FP16 | INT8 | INT4 | Q4_K_M | Q5_K_M |
|----------|------|------|------|---------|---------|
| 🧠 Reasoning | ✅ | ❌ | ❌ | ❌ | ❌ |
| 📋 JSON Formatting | ⚠️ | ✅ | ❌ | ❌ | ❌ |
| 📝 Constraint Adherence | ⚠️ | ⚠️ | ❌ | ⚠️ | ⚠️ |
| 📖 Reading Comprehension | ❌ | ❌ | ❌ | ❌ | ⚠️ |
| 🎭 Creativity & Tone | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Total Score** | **2/5** | **1.5/5** | **0/5** | **0/5** | **0/5** |

---

## ⚡ Speed vs Quality — All Formats

| Model | Prompt Speed | Generation Speed | Quality |
|-------|-------------|-----------------|---------|
| FP16 | ~65 t/s | ~9.5 t/s | 2/5 |
| INT8 (Q8_0) | ~75 t/s | ~17 t/s | 1.5/5 |
| INT4 (Q4_0) | ~115 t/s | ~26 t/s | 0/5 |
| Q4_K_M | ~100 t/s | ~22 t/s | 0/5 |
| Q5_K_M | ~67 t/s | ~20 t/s | 0/5 |

---

## 🔑 Key Takeaways

1. **FP16 is still king for quality** — only format to pass reasoning at 1.1B scale.
2. **INT8 is the edge deployment sweet spot** — 1.8x faster, half the RAM, acceptable quality.
3. **K-quants did NOT help at 1.1B scale** — Q4_K_M and Q5_K_M scored same as Q4_0 (0/5). Better quantization math cannot compensate for insufficient model capacity.
4. **The real bottleneck is model size, not quantization format** — upgrading to 3B+ will matter far more than switching quantization methods.
5. **Q5_K_M was marginally better on word compression** — only detectable difference across K-quants.
6. **INT8 beat all INT4 variants including K-quants** — for structured tasks, less compression = better results.

---

## 🗺️ Roadmap

- [x] TinyLlama 1.1B — FP16, INT8, INT4 (Q4_0)
- [x] TinyLlama 1.1B — Q4_K_M, Q5_K_M
- [x] HuggingFace uploads — all 5 GGUF files available for download
- [ ] Phi-3-mini (3.8B) — FP16, INT8, INT4 on Lightning AI
- [ ] Mistral-7B — INT4, Q4_K_M on Lightning AI
- [ ] Automated Python benchmark script with CSV output
- [ ] Speed vs Quality visualization chart

---

## 🛠️ Tech Stack

- **Runtime:** [llama.cpp](https://github.com/ggml-org/llama.cpp)
- **Models:** [🤗 HuggingFace](https://huggingface.co/Yash1bajpai/tinyllama-1.1b-gguf-benchmarks)
- **OS:** Ubuntu (WSL2) on Windows
- **Hardware:** CPU-only inference
- **Format:** GGUF

---

## 👤 Author

**Yash Bajpai** — Aspiring NLP & Edge AI Engineer

[![GitHub](https://img.shields.io/badge/GitHub-Yash1bajpai-black?logo=github)](https://github.com/Yash1bajpai)
[![HuggingFace](https://img.shields.io/badge/🤗-Yash1bajpai-yellow)](https://huggingface.co/Yash1bajpai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Yash%20Bajpai-blue?logo=linkedin)](https://www.linkedin.com/in/yash-bajpai-b5a86332a/)

---

*More models and quantization methods coming soon. Star ⭐ the repo to follow along!*
