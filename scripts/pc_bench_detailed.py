import subprocess
import os

models = [
    ("Qwen-Q4", "models/Qwen2.5-3B-Instruct-Q4_K_M.gguf"),
    ("Qwen-Q8", "models/Qwen2.5-3B-Instruct-Q8_0.gguf"),
    ("Phi3-Q4", "models/Phi-3-mini-4k-instruct-Q4_K_M.gguf"),
    ("Phi3-Q8", "models/Phi-3-mini-4k-instruct-Q8_0.gguf")
]
contexts = [512, 1024]

print("=== PC Benchmarks (Multiple Contexts & RAM Info) ===")

with open("pc_bench_raw.log", "w") as f:
    f.write("Raw Benchmarks\\n\\n")

for name, path in models:
    for ctx in contexts:
        print(f"\\nRunning {name} with Ctx {ctx}...")
        p = ctx // 2
        n = ctx // 2
        cmd = f'wsl -e bash -c "cd /mnt/c/Yash/edge-llm-benchmarks && ./llama.cpp/build/bin/llama-bench -m {path} -p {p} -n {n} -t 6 -r 1 -o md"'
        
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        with open("pc_bench_raw.log", "a") as f:
            f.write(f"=== {name} Ctx {ctx} ===\\n")
            f.write("--- STDOUT ---\\n")
            f.write(result.stdout)
            f.write("\\n--- STDERR ---\\n")
            f.write(result.stderr)
            f.write("\\n\\n")
        
        print(f"Done: {name} {ctx}")
