import paramiko

def run_ssh_command(host, port, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, port=port, username=user, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode('utf-8'))
    finally:
        client.close()

if __name__ == "__main__":
    commands = """
    find /data/data/com.termux/files/home -name "*tiny*llama*.gguf" -o -name "*Tiny*Llama*.gguf" 2>/dev/null
    find /sdcard/ -name "*tiny*llama*.gguf" -o -name "*Tiny*Llama*.gguf" 2>/dev/null
    """
    run_ssh_command('10.88.85.133', 8022, 'u0_a346', '1234567890', commands)
