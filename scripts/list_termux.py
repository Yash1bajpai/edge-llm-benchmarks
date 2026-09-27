import paramiko
import os

IP = os.environ["PHONE_IP"]
PORT = int(os.environ.get("PHONE_PORT", "8022"))
USER = os.environ["PHONE_USER"]
PASS = os.environ["PHONE_PASS"]

def exec_ssh(command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(IP, port=PORT, username=USER, password=PASS, timeout=5)
        stdin, stdout, stderr = client.exec_command(command)
        out = stdout.read().decode('utf-8', errors='ignore').strip()
        return out
    except Exception as e:
        return f"Error: {e}"
    finally:
        client.close()

if __name__ == "__main__":
    print(exec_ssh("ls -lh ~/models"))
