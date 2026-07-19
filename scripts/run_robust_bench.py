import paramiko
import time

IP = "10.61.130.233"
PORT = 8022
USER = "u0_a346"
PASS = "1234567890"

downloads = {
    "Qwen-Q8": 'wget -c -qO Qwen-Q8.gguf "https://huggingface.co/Yash1bajpai/edge-llm-benchmarks-gguf/resolve/main/Qwen2.5-3B-Instruct-Q8_0.gguf?download=true"',
    "Phi-Q8": 'wget -c -qO Phi-Q8.gguf "https://huggingface.co/Yash1bajpai/edge-llm-benchmarks-gguf/resolve/main/Phi-3-mini-4k-instruct-Q8_0.gguf?download=true"'
}

benchmarks = [
    ("TinyLlama-Q4", "models/TinyLlama-Q4_K_M.gguf", 512),
    ("TinyLlama-Q4", "models/TinyLlama-Q4_K_M.gguf", 1024),
    ("TinyLlama-INT8", "models/TinyLlama-INT8.gguf", 512),
    ("Qwen-Q4", "Qwen-Q4.gguf", 512),
    ("Qwen-Q4", "Qwen-Q4.gguf", 1024),
    ("Qwen-Q8", "Qwen-Q8.gguf", 512),
    ("Phi-Q4", "Phi-Q4.gguf", 512)
]

def exec_ssh(command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(IP, port=PORT, username=USER, password=PASS, timeout=15)
        stdin, stdout, stderr = client.exec_command(command)
        out = stdout.read().decode('utf-8', errors='ignore')
        err = stderr.read().decode('utf-8', errors='ignore')
        return out, err, stdout.channel.recv_exit_status()
    except Exception as e:
        return "", str(e), -1
    finally:
        client.close()

if __name__ == "__main__":
    print("Testing connection...")
    out, err, status = exec_ssh("termux-wake-lock; echo Connected")
    if status != 0:
        print(f"Failed to connect: {err}")
        exit(1)
    
    print("Connection successful. Initiating downloads (this might take a while if not cached)...")
    for name, cmd in downloads.items():
        print(f"Downloading {name}...")
        exec_ssh(cmd)
        
    print("\\n=== Starting Benchmarks ===")
    for name, path, ctx in benchmarks:
        print(f"\\n--- Benchmarking {name} (Ctx: {ctx}) ---")
        p = ctx // 2
        n = ctx // 2
        cmd = f"./llama.cpp/build/bin/llama-bench -m {path} -p {p} -n {n} -t 4 -r 1 -o md"
        out, err, status = exec_ssh(cmd)
        
        if status == -1 or status != 0:
            print(f"CRASHED! Exit Status: {status}")
            print(f"Error Log:\\n{err}")
            break # Stop if sshd crashes to avoid infinite errors
            
        print(out.strip())
        
        # Extract RAM usage from stderr
        ram_info = []
        for line in err.split('\\n'):
            if "total size" in line or "model size" in line or "total VRAM" in line:
                ram_info.append(line.strip())
        print("RAM Usage Info:")
        for r in ram_info:
            print(r)
