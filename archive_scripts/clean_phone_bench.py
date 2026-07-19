import paramiko

IP = "10.61.130.233"
PORT = 8022
USER = "u0_a346"
PASS = "1234567890"

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
    print("=== Cleaning Up Zombies ===")
    exec_ssh("killall -9 llama-bench; killall -9 wget")
    
    print("=== Running Qwen-Q8 Isolated ===")
    cmd = "termux-wake-lock; ./llama.cpp/build/bin/llama-bench -m Qwen-Q8.gguf -p 128 -n 128 -b 128 -ub 128 -mmp 1 -t 4 -r 1 -v"
    out, err, status = exec_ssh(cmd)
    
    print(f"Status: {status}")
    if status == 0:
        print("Success! Output:")
        print(out)
    else:
        print("Crashed! Error:")
        print(err[-500:])
        
    print("\\n=== RAM Usage ===")
    for line in err.split('\\n'):
        if "model size" in line or "total size" in line or "KV self size" in line or "compute buffer" in line:
            print(line.strip())
