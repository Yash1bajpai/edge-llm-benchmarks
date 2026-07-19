import subprocess
import re

models = [
    ("Qwen-Q4", "models/Qwen2.5-3B-Instruct-Q4_K_M.gguf"),
    ("Qwen-Q8", "models/Qwen2.5-3B-Instruct-Q8_0.gguf"),
    ("Phi3-Q4", "models/Phi-3-mini-4k-instruct-Q4_K_M.gguf")
]
contexts = [512, 1024]

print("=== Exact RAM Usage Extractor ===")

for name, path in models:
    for ctx in contexts:
        # Run llama-cli to generate 1 token and capture stderr
        cmd = f'wsl -e bash -c "cd /mnt/c/Yash/edge-llm-benchmarks && ./llama.cpp/build/bin/llama-cli -m {path} -p \\"A\\" -n 1 -c {ctx}"'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        err = result.stderr
        
        model_size = "Unknown"
        kv_cache = "Unknown"
        compute_buf = "Unknown"
        
        for line in err.split('\\n'):
            if "llm_load_print_meta: model size" in line and "=" in line:
                model_size = line.split("=")[1].strip().split(' ')[0].strip()
            elif "llama_new_context_with_model: KV self size" in line and "=" in line:
                kv_cache = line.split("=")[1].strip().split(',')[0].strip()
            elif "llama_new_context_with_model: compute buffer total size" in line and "=" in line:
                compute_buf = line.split("=")[1].strip()
                
        print(f"[{name} @ Ctx {ctx}] -> Model Size: {model_size} MB, KV Cache: {kv_cache}, Compute Buffer: {compute_buf}")
