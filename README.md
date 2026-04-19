# 🧪 Edge LLM Benchmarks

> Systematically benchmarking quantized Large Language Models for Edge AI deployment — comparing quality degradation across FP16, INT8, and INT4 formats.

![Model](https://img.shields.io/badge/Model-TinyLlama--1.1B-blue)
![Quantization](https://img.shields.io/badge/Quantization-FP16%20%7C%20INT8%20%7C%20INT4-orange)
![Runtime](https://img.shields.io/badge/Runtime-llama.cpp-green)
![HuggingFace](https://img.shields.io/badge/🤗-Models%20on%20HuggingFace-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 🎯 Why This Project?

When deploying LLMs on edge devices (mobile, embedded systems, IoT), memory is the primary constraint. Quantization reduces model size drastically — but at what cost to output quality?

This repo answers that question with **real, reproducible benchmarks** across 5 critical capability dimensions.

---

## 📦 Models Tested

| Model | Format | Size | RAM Usage | Download |
|-------|--------|------|-----------|----------|
| TinyLlama-1.1B | FP16 | ~2.2 GB | ~2212 MiB | [🤗 HuggingFace](https://huggingface.co/Yash1bajpai/tinyllama-1.1b-gguf-benchmarks/blob/main/TinyLlama-FP16.gguf) |
| TinyLlama-1.1B | INT8 (Q8_0) | ~1.1 GB | ~1229 MiB | [🤗 HuggingFace](https://huggingface.co/Yash1bajpai/tinyllama-1.1b-gguf-benchmarks/blob/main/TinyLlama-INT8.gguf) |
| TinyLlama-1.1B | INT4 (Q4_0) | ~670 MB | ~744 MiB | [🤗 HuggingFace](https://huggingface.co/Yash1bajpai/tinyllama-1.1b-gguf-benchmarks/blob/main/Tinyllama-INT4.gguf) |

> All models are in GGUF format, ready to run with llama.cpp — no conversion needed.

---

## ⚙️ Setup & Reproduction

```bash
# 1. Clone llama.cpp and build
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build
cmake --build build --config Release

# 2. Download a model from HuggingFace (links above) and place in models/

# 3. Run a benchmark
./build/bin/llama-cli -m models/TinyLlama-FP16.gguf --single-turn --seed 42 -n 150 -p "Your prompt here"

# 4. Or run the full benchmark suite
bash scripts/run_benchmark.sh models/TinyLlama-FP16.gguf FP16
```

---

## 🧩 Benchmark Prompts

| # | Category | Prompt Summary |
|---|----------|----------------|
| 1 | 🧠 Logic & Reasoning | Jane has 3 brothers puzzle |
| 2 | 📋 JSON Formatting | Extract problem/solution as strict JSON |
| 3 | 📝 Constraint Adherence | Email starting with 'Unfortunately' / 'However' |
| 4 | 📖 Reading Comprehension | Summarize JWST in exactly 15 words |
| 5 | 🎭 Creativity & Tone | Grumpy sailor explaining smartphone in 3 sentences |

---

## 📊 Results Table

### 1. 🧠 Logic & Reasoning
*"Jane has 3 brothers. Each brother has 2 sisters. How many sisters does Jane have?"*

| Model | Answer | Correct? | Notes |
|-------|--------|----------|-------|
| FP16 | 2 sisters | ✅ | Clean reasoning, correct answer |
| INT8 | 5 sisters (3+2) | ❌ | Added brothers+sisters incorrectly |
| INT4 | No answer given | ❌ | Looped on problem restatement, never concluded |

**Winner: FP16** — INT8 and INT4 both failed basic deductive reasoning.

---

### 2. 📋 JSON Formatting
*"Extract problem and solution as a valid JSON object. Do not add any other text."*

| Model | Valid JSON? | Followed Format? | Notes |
|-------|-----------|-----------------|-------|
| FP16 | ✅ | ⚠️ Partial | Wrapped in markdown block, solution hallucinated extra content |
| INT8 | ✅ | ✅ Best | Raw valid JSON, no markdown wrapper |
| INT4 | ❌ | ❌ | Added prose preamble, malformed nested object |

**Winner: INT8** — Surprisingly outperformed FP16 on strict formatting.

---

### 3. 📝 Constraint Adherence
*"Write 2-sentence email. First sentence starts with 'Unfortunately', second with 'However'."*

| Model | Starts with 'Unfortunately'? | Starts with 'However'? | Exactly 2 sentences? |
|-------|------------------------------|------------------------|----------------------|
| FP16 | ✅ | ✅ | ❌ Added 3rd sentence + sign-off |
| INT8 | ✅ | ✅ | ❌ Added 3rd sentence + sign-off |
| INT4 | ❌ | ❌ | ❌ Ignored both constraints completely |

**Winner: FP16 / INT8 tied** — Both followed keyword constraints. INT4 failed completely.

---

### 4. 📖 Reading Comprehension (Exact Word Count)
*"Summarize in exactly 15 words."*

| Model | Word Count | Correct Count? | Notes |
|-------|-----------|----------------|-------|
| FP16 | ~45 words | ❌ | Repeated the passage almost verbatim |
| INT8 | ~55 words | ❌ | Added extra sentence beyond the passage |
| INT4 | ~40 words | ❌ | Slightly condensed but still far over limit |

**Winner: None** — All three models failed the exact word count constraint. Common weakness of small models.

---

### 5. 🎭 Creativity & Tone
*"You are a grumpy old sailor. Explain smartphone in exactly 3 sentences."*

| Model | Sailor Tone? | Exactly 3 Sentences? | Notes |
|-------|-------------|----------------------|-------|
| FP16 | ❌ | ❌ (2 sentences) | Factual/neutral, no sailor character |
| INT8 | ❌ | ❌ (2 sentences) | Same issue, added wrong etymology |
| INT4 | ❌ | ❌ (4+ sentences) | No persona, went on too long |

**Winner: None** — All three models ignored the creative persona. TinyLlama 1.1B is too small for complex instruction-following.

---

## 📈 Performance Scorecard

| Category | FP16 | INT8 | INT4 |
|----------|------|------|------|
| 🧠 Reasoning | ✅ | ❌ | ❌ |
| 📋 JSON Formatting | ⚠️ | ✅ | ❌ |
| 📝 Constraint Adherence | ⚠️ | ⚠️ | ❌ |
| 📖 Reading Comprehension | ❌ | ❌ | ❌ |
| 🎭 Creativity & Tone | ❌ | ❌ | ❌ |
| **Total Score** | **2/5** | **1.5/5** | **0/5** |

---

## ⚡ Speed vs Quality Tradeoff

| Model | Prompt Speed | Generation Speed | Quality Score |
|-------|-------------|-----------------|---------------|
| FP16 | ~65 t/s | ~9.5 t/s | 2/5 |
| INT8 | ~75 t/s | ~17 t/s | 1.5/5 |
| INT4 | ~115 t/s | ~26 t/s | 0/5 |

> INT4 is **2.7x faster** than FP16 but quality drops to near-zero on complex tasks.
> INT8 hits a sweet spot — **1.8x faster** than FP16 with only marginal quality loss.

---

## 🔑 Key Takeaways

1. **INT8 is the edge deployment sweet spot** — nearly half the RAM of FP16, nearly double the speed, acceptable quality loss for simple tasks.
2. **INT4 is too aggressive for 1.1B models** — at this scale, INT4 destroys instruction-following ability.
3. **All quantizations struggle with exact constraints** — word counts, sentence counts, and personas are hard for small models regardless of precision.
4. **INT8 surprised on JSON formatting** — structured output tasks may actually benefit from quantization noise acting as regularization.
5. **Model size matters more than quantization** — upgrading to a 3B model will improve results more than fighting INT4 degradation at 1.1B.

---

## 🗺️ Roadmap

- [x] TinyLlama 1.1B — FP16, INT8, INT4 (Q4_0)
- [x] HuggingFace model uploads — all 3 GGUF files available for download
- [ ] TinyLlama 1.1B — Q4_K_M, Q5_K_M (better quantization methods)
- [ ] Phi-2 (2.7B) — FP16, INT8, INT4
- [ ] Qwen2-1.5B — FP16, INT8, INT4
- [ ] Automated benchmark script

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

---

*More models and quantization methods coming soon. Star ⭐ the repo to follow along!*
