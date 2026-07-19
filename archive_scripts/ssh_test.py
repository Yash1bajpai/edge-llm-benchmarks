import paramiko

def run_ssh_command(host, port, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, port=port, username=user, password=password)
        print(f"Connected to {host}")
        stdin, stdout, stderr = client.exec_command(command)
        out = stdout.read().decode()
        err = stderr.read().decode()
        if out: print("STDOUT:\n" + out)
        if err: print("STDERR:\n" + err)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    run_ssh_command('10.61.130.233', 8022, 'u0_a346', '1234567890', 'echo "Screen is off but I am still connected!"')
