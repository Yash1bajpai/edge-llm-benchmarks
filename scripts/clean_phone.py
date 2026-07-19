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
        out = stdout.read().decode('utf-8', errors='ignore').strip()
        err = stderr.read().decode('utf-8', errors='ignore').strip()
        return out, err
    except Exception as e:
        return "", str(e)
    finally:
        client.close()

if __name__ == "__main__":
    print("Deleting GGUF files from Phone...")
    out, err = exec_ssh("rm -f *.gguf")
    if err:
        print("Error:", err)
    else:
        print("Done. Verifying...")
        out2, err2 = exec_ssh("ls -lh *.gguf")
        print("Remaining files:", out2)
