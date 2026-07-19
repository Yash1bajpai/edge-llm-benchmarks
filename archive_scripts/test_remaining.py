import paramiko
import sys

def run_ssh_command(host, port, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, port=port, username=user, password=password)
        stdin, stdout, stderr = client.exec_command(command, get_pty=True)
        for line in iter(stdout.readline, ""):
            print(line, end="")
        exit_status = stdout.channel.recv_exit_status()
        print(f"\\nExit status: {exit_status}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    commands = """
    termux-wake-lock
    
    echo "=== Benchmarking TinyLlama ==="
    ./llama.cpp/build/bin/llama-bench -m models/TinyLlama-Q4_K_M.gguf -p 128 -n 128 -r 1 -o md
    
    echo "=== Downloading Qwen Q8_0 ==="
    wget -qO Qwen-Q8.gguf "https://huggingface.co/Yash1bajpai/edge-llm-benchmarks-gguf/resolve/main/Qwen2.5-3B-Instruct-Q8_0.gguf?download=true"
    
    echo "=== Benchmarking Qwen Q8_0 ==="
    ./llama.cpp/build/bin/llama-bench -m Qwen-Q8.gguf -p 128 -n 128 -r 1 -o md
    
    echo "=== Retrying Phi-3 Q4_K_M (Low Mem Mode) ==="
    # Trying with lower batch size and threads to avoid OOM
    ./llama.cpp/build/bin/llama-bench -m Phi-Q4.gguf -p 128 -n 128 -r 1 -b 64 -ub 64 -t 4 -o md
    
    termux-wake-unlock
    """
    run_ssh_command('10.61.130.233', 8022, 'u0_a346', '1234567890', commands)
