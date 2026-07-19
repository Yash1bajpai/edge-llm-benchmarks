import subprocess
import re
import csv
import sys
import os

PROMPTS = {
    "Logic & Reasoning": "Jane has 3 brothers. Each of her brothers has 2 sisters. How many sisters does Jane have? Think step-by-step.",
    "Reading Comprehension": "Summarize the following in exactly 15 words: 'The James Webb Space Telescope is an infrared space observatory that launched on December 25, 2021, from Kourou, French Guiana, and arrived at the Sun-Earth L2 Lagrange point in January 2022.'"
}

# Use the appropriate llama-cli path depending on OS
# WSL: ./llama.cpp/build/bin/llama-cli
# Termux: ./llama-cli (we'll assume it's in PATH or current dir)
BINARY = sys.argv[1] if len(sys.argv) > 1 else "./llama.cpp/build/bin/llama-cli"
MODELS = sys.argv[2].split(",") if len(sys.argv) > 2 else [
    "models/Qwen2.5-3B-Instruct-Q4_K_M.gguf",
    "models/Qwen2.5-3B-Instruct-Q8_0.gguf",
    "models/Phi-3-mini-4k-instruct-Q4_K_M.gguf",
    "models/Phi-3-mini-4k-instruct-Q8_0.gguf"
]

OUTPUT_CSV = "benchmark_results.csv"

def run_benchmark(model_path, prompt_name, prompt):
    print(f"Benchmarking {model_path} - {prompt_name}...")
    cmd = [
        BINARY,
        "-m", model_path,
        "--single-turn",
        "-n", "150",
        "--seed", "42",
        "-p", prompt
    ]
    
    try:
        # Run command and capture output (llama-cli prints timings to stderr)
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout + result.stderr
        
        # Parse output for metrics
        ttft = "N/A"
        prompt_tps = "N/A"
        gen_tps = "N/A"
        
        prompt_match = re.search(r"prompt eval time =.*?/\s*(\d+)\s*tokens.*?,\s*([\d.]+)\s*tokens per second", output)
        if prompt_match:
            tokens, tps = prompt_match.groups()
            prompt_tps = tps
            # Calculate TTFT roughly based on prompt eval time (time taken to evaluate the prompt)
            time_match = re.search(r"prompt eval time =\s*([\d.]+)\s*ms", output)
            if time_match:
                ttft = str(round(float(time_match.group(1)) / 1000.0, 2)) + "s"
                
        eval_match = re.search(r"eval time =.*?/\s*(\d+)\s*runs.*?,\s*([\d.]+)\s*tokens per second", output)
        if eval_match:
            gen_tps = eval_match.group(2)
            
        return {
            "Model": os.path.basename(model_path),
            "Prompt Type": prompt_name,
            "TTFT": ttft,
            "Prompt T/s": prompt_tps,
            "Gen T/s": gen_tps,
        }
    except Exception as e:
        print(f"Error running {model_path}: {e}")
        return None

results = []
for model in MODELS:
    if not os.path.exists(model):
        print(f"Skipping {model}, file not found.")
        continue
    for p_name, p_text in PROMPTS.items():
        res = run_benchmark(model, p_name, p_text)
        if res:
            results.append(res)

with open(OUTPUT_CSV, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Model", "Prompt Type", "TTFT", "Prompt T/s", "Gen T/s"])
    writer.writeheader()
    writer.writerows(results)

print(f"Benchmarking complete. Results saved to {OUTPUT_CSV}")
