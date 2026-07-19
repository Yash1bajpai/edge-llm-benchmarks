import paramiko
import time

IP = "10.61.130.233"
PORT = 8022
USER = "u0_a346"
PASS = "1234567890"

models = {
    "Qwen-Q8": "Qwen-Q8.gguf",
    "Phi-Q8": "Phi-Q8.gguf",
    "Qwen-Q4 (RAM Check)": "Qwen-Q4.gguf"
}

def exec_ssh(command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(IP, port=PORT, username=USER, password=PASS, timeout=10)
        stdin, stdout, stderr = client.exec_command(command)
        out = stdout.read().decode('utf-8', errors='ignore')
        err = stderr.read().decode('utf-8', errors='ignore')
        return out, err, stdout.channel.recv_exit_status()
    except Exception as e:
        return "", str(e), -1
    finally:
        client.close()

if __name__ == "__main__":
    print("=== Retrying Q8 Models on Phone & Fetching RAM Usage ===")
    
    for name, path in models.items():
        print(f"\\nTrying {name}...")
        cmd = f"termux-wake-lock; ./llama.cpp/build/bin/llama-bench -m {path} -p 64 -n 64 -b 1 -ub 1 -mmp 0 -t 4 -r 1 -v"
        out, err, status = exec_ssh(cmd)
        
        if status != 0:
            print(f"CRASHED! Exit code: {status}")
            print(f"Error Log snippet:\\n{err[-500:]}")
            time.sleep(2)
        else:
            print(f"Success!\\n{out.strip()}")
            
        print("\\nRAM Usage Extractions:")
        for line in err.split('\\n'):
            if "model size" in line or "total size" in line or "KV self size" in line or "compute buffer" in line:
                print(line.strip())
