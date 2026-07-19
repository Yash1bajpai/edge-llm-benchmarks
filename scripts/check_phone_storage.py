import paramiko

IP = "10.61.130.233"
PORT = 8022
USER = "u0_a346"
PASS = "1234567890"

def exec_ssh(command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(IP, port=PORT, username=USER, password=PASS, timeout=10)
        stdin, stdout, stderr = client.exec_command(command)
        return stdout.read().decode('utf-8', errors='ignore').strip()
    except Exception as e:
        return str(e)
    finally:
        client.close()

if __name__ == "__main__":
    print("Phone GGUF files:")
    print(exec_ssh("ls -lh *.gguf"))
    print("\nTotal size of GGUF files:")
    print(exec_ssh("du -ch *.gguf | grep total"))
