import paramiko
import os

IP = os.environ["PHONE_IP"]
PORT = int(os.environ.get("PHONE_PORT", "8022"))
USER = os.environ["PHONE_USER"]
PASS = os.environ["PHONE_PASS"]

def test_ssh():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(IP, port=PORT, username=USER, password=PASS, timeout=5)
        print("SSH Connection Successful!")
        return True
    except Exception as e:
        print(f"SSH Connection Failed: {e}")
        return False
    finally:
        client.close()

if __name__ == "__main__":
    test_ssh()
