import paramiko
import os

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
    run_ssh_command(os.environ["PHONE_IP"], int(os.environ.get("PHONE_PORT", "8022")), os.environ["PHONE_USER"], os.environ["PHONE_PASS"], 'echo "Screen is off but I am still connected!"')
