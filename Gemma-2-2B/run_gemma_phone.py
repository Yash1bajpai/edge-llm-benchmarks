import os
import subprocess
import paramiko
import time

URL = "https://huggingface.co/bartowski/gemma-2-2b-it-GGUF/resolve/main/gemma-2-2b-it-Q8_0.gguf?download=true"
MODEL_NAME = "gemma-2-2b-it-Q8_0.gguf"
PC_PATH = f"models/{MODEL_NAME}"

# Phone Details
IP = "10.61.130.233"
PORT = 8022
USER = "u0_a346"
PASS = "1234567890"

def exec_ssh(command, wait=True):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(IP, port=PORT, username=USER, password=PASS, timeout=10)
        stdin, stdout, stderr = client.exec_command(command)
        if wait:
            out = stdout.read().decode('utf-8', errors='ignore')
            err = stderr.read().decode('utf-8', errors='ignore')
            return out, err, stdout.channel.recv_exit_status()
        return "", "", 0
    except Exception as e:
        return "", str(e), -1
    finally:
        client.close()

if __name__ == "__main__":
    print("=== Downloading Gemma Q8 on Phone ===")
    exec_ssh("killall -9 llama-bench; killall -9 wget")
    exec_ssh(f"wget -qO {MODEL_NAME} '{URL}'")
    
    print("\\n=== Benchmarking on Phone ===")
    cmd = f"termux-wake-lock; ./llama.cpp/build/bin/llama-bench -m {MODEL_NAME} -p 256 -n 256 -b 128 -ub 128 -t 4 -r 1"
    out, err, status = exec_ssh(cmd)
    print(f"Status: {status}")
    print(out)
    if status != 0:
        print("Phone Bench Crashed! (Likely OOM)")
        
    print("\\n=== Extracting Phone RAM Usage ===")
    cmd_ram = f"./llama.cpp/build/bin/llama-bench -m {MODEL_NAME} -p 1 -n 1 -b 1 -ub 1 -t 4 -r 1 -v"
    out2, err2, status2 = exec_ssh(cmd_ram)
    for line in err2.split('\\n'):
        if "model size" in line or "total size" in line or "KV self size" in line or "compute buffer" in line:
            print(line.strip())
