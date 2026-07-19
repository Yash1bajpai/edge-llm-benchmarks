import paramiko
import sys

def run_ssh_command(host, port, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, port=port, username=user, password=password)
        stdin, stdout, stderr = client.exec_command(command, get_pty=True)
        # Stream output
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
    echo "Benchmarking TinyLlama..."
    ./llama.cpp/build/bin/llama-bench -m models/TinyLlama-Q4_K_M.gguf -p 128 -n 128 -r 1 -o md
    termux-wake-unlock
    """
    run_ssh_command('10.88.85.133', 8022, 'u0_a346', '1234567890', commands)
