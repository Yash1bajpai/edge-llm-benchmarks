import os
import shutil

BASE_DIR = r"c:\Yash\edge-llm-benchmarks"

dirs_to_create = [
    "TinyLlama",
    "Qwen2.5-3B",
    "Phi-3-Mini-4k",
    "Gemma-2-2B",
    "scripts",
    "archive_scripts"
]

for d in dirs_to_create:
    os.makedirs(os.path.join(BASE_DIR, d), exist_ok=True)

# Define generic scripts
generic_scripts = [
    "check_phone_specs.py",
    "run_robust_bench.py",
    "benchmark.py",
    "pc_bench_detailed.py"
]

# Define archive scripts (debug/one-off files)
archive_scripts = [
    "check_binaries.py",
    "check_phone.py",
    "check_phone_progress.py",
    "clean_phone_bench.py",
    "find_tinyllama.py",
    "get_ram_pc.py",
    "retry_q8_phone.py",
    "ssh_test.py",
    "test_remaining.py",
    "verify_token.py",
    "phone_setup.py"
]

# Move scripts
for f in generic_scripts:
    src = os.path.join(BASE_DIR, f)
    dst = os.path.join(BASE_DIR, "scripts", f)
    if os.path.exists(src): shutil.move(src, dst)

for f in archive_scripts:
    src = os.path.join(BASE_DIR, f)
    dst = os.path.join(BASE_DIR, "archive_scripts", f)
    if os.path.exists(src): shutil.move(src, dst)

# Model specific scripts
if os.path.exists(os.path.join(BASE_DIR, "final_phone_bench.py")):
    shutil.move(os.path.join(BASE_DIR, "final_phone_bench.py"), os.path.join(BASE_DIR, "TinyLlama", "run_tinyllama_phone.py"))

if os.path.exists(os.path.join(BASE_DIR, "run_phone_bench.py")):
    shutil.move(os.path.join(BASE_DIR, "run_phone_bench.py"), os.path.join(BASE_DIR, "Qwen2.5-3B", "run_qwen_phone.py"))

if os.path.exists(os.path.join(BASE_DIR, "gemma_q8_phone.py")):
    shutil.move(os.path.join(BASE_DIR, "gemma_q8_phone.py"), os.path.join(BASE_DIR, "Gemma-2-2B", "run_gemma_phone.py"))
if os.path.exists(os.path.join(BASE_DIR, "run_q8_pc.py")):
    shutil.move(os.path.join(BASE_DIR, "run_q8_pc.py"), os.path.join(BASE_DIR, "Gemma-2-2B", "run_gemma_pc.py"))

# Create READMEs for each model
tinyllama_readme = """# TinyLlama

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
"""

qwen_readme = """# Qwen 2.5 3B

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
"""

phi_readme = """# Phi-3 Mini 4k

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
"""

gemma_readme = """# Gemma-2 2B

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
"""

with open(os.path.join(BASE_DIR, "TinyLlama", "README.md"), "w") as f: f.write(tinyllama_readme)
with open(os.path.join(BASE_DIR, "Qwen2.5-3B", "README.md"), "w") as f: f.write(qwen_readme)
with open(os.path.join(BASE_DIR, "Phi-3-Mini-4k", "README.md"), "w") as f: f.write(phi_readme)
with open(os.path.join(BASE_DIR, "Gemma-2-2B", "README.md"), "w") as f: f.write(gemma_readme)

print("Restructuring Complete.")
