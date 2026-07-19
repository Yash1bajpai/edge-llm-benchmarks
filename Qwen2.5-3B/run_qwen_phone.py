import paramiko
import time

def run_ssh_command(host, port, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, port=port, username=user, password=password)
        # We run the command and wait for it to just spawn the background process
        stdin, stdout, stderr = client.exec_command(command)
        print("Spawned background process.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    commands = """
    nohup sh -c '
    termux-wake-lock
    wget -L -O Qwen-Q4.gguf "https://huggingface.co/Yash1bajpai/edge-llm-benchmarks-gguf/resolve/main/Qwen2.5-3B-Instruct-Q4_K_M.gguf?download=true"
    ./llama.cpp/build/bin/llama-bench -m Qwen-Q4.gguf -p 128 -n 128 -r 1 -o md > phone_bench.md
    wget -L -O Phi-Q4.gguf "https://huggingface.co/Yash1bajpai/edge-llm-benchmarks-gguf/resolve/main/Phi-3-mini-4k-instruct-Q4_K_M.gguf?download=true"
    ./llama.cpp/build/bin/llama-bench -m Phi-Q4.gguf -p 128 -n 128 -r 1 -o md >> phone_bench.md
    echo "DONE" > bench_status.txt
    termux-wake-unlock
    ' > phone_log.txt 2>&1 &
    """
    run_ssh_command('10.88.85.133', 8022, 'u0_a346', '1234567890', commands)
