import paramiko
import os

IP = os.environ["PHONE_IP"]
PORT = int(os.environ.get("PHONE_PORT", "8022"))
USER = os.environ["PHONE_USER"]
PASS = os.environ["PHONE_PASS"]

local_path = r"c:\Yash\edge-llm-benchmarks\models\LFM2.5-2.6B-Q6_K.gguf"
remote_path = "/data/data/com.termux/files/home/models/LFM2.5-2.6B-Q6_K.gguf"

try:
    transport = paramiko.Transport((IP, PORT))
    transport.connect(username=USER, password=PASS)
    sftp = paramiko.SFTPClient.from_transport(transport)
    
    # Ensure models dir exists
    sftp.execute = lambda cmd: paramiko.SSHClient().exec_command(cmd) # Hacky, but paramiko SFTP doesn't have mkdir-p easily. 
    # Actually just run ssh
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, port=PORT, username=USER, password=PASS)
    ssh.exec_command("mkdir -p ~/models")
    ssh.close()

    print("Uploading LFM to phone... This may take a minute.")
    sftp.put(local_path, remote_path)
    print("Upload complete!")
    
    sftp.close()
    transport.close()
except Exception as e:
    print("Error:", e)
