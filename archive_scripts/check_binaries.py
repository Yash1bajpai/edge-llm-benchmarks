import paramiko
import sys
import os

def run_ssh_command(host, port, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, port=port, username=user, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode('utf-8'))
        print(stderr.read().decode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    commands = """
    ls -l llama.cpp/build/bin/llama-bench
    ls -l llama.cpp/build/bin/llama-cli
    """
    run_ssh_command(os.environ["PHONE_IP"], int(os.environ.get("PHONE_PORT", "8022")), os.environ["PHONE_USER"], os.environ["PHONE_PASS"], commands)
