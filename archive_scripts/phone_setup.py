import paramiko
import sys

def run_ssh_command(host, port, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, port=port, username=user, password=password)
        print(f"Connected to {host}")
        
        print("Executing command on phone... this will take a while.")
        stdin, stdout, stderr = client.exec_command(command, get_pty=True)
        
        # Stream the output
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
    pkg update -y
    pkg install clang cmake make git wget python -y
    if [ ! -d "llama.cpp" ]; then
        git clone https://github.com/ggml-org/llama.cpp
    fi
    cd llama.cpp
    cmake -B build
    cmake --build build --config Release
    """
    run_ssh_command('10.88.85.133', 8022, 'u0_a346', '1234567890', commands)
