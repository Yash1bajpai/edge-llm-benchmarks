import subprocess
cmd = 'wsl -e bash -c "cd /mnt/c/Yash/edge-llm-benchmarks && ./llama.cpp/build/bin/llama-bench -m models/gemma-2-2b-it-Q8_0.gguf -p 256 -n 256 -t 6 -r 1"'
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print("OUT:")
print(res.stdout)
print("ERR:")
print(res.stderr)
