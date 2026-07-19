import paramiko
import json

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
        return out
    except Exception as e:
        return str(e)
    finally:
        client.close()

if __name__ == "__main__":
    specs = {}
    
    # Device details
    specs["Brand"] = exec_ssh("getprop ro.product.brand")
    specs["Model"] = exec_ssh("getprop ro.product.model")
    specs["Platform (SoC)"] = exec_ssh("getprop ro.board.platform")
    specs["Hardware"] = exec_ssh("getprop ro.hardware")
    specs["Android Version"] = exec_ssh("getprop ro.build.version.release")
    
    # CPU
    cpu_info = exec_ssh("grep -i 'Hardware' /proc/cpuinfo")
    if not cpu_info:
        cpu_info = exec_ssh("grep -i 'model name' /proc/cpuinfo | head -n 1")
    specs["CPU Info"] = cpu_info
    
    cores = exec_ssh("nproc")
    specs["Cores"] = cores
    
    # RAM
    mem_total = exec_ssh("grep MemTotal /proc/meminfo | awk '{print $2}'")
    try:
        ram_gb = round(int(mem_total) / 1024 / 1024, 2)
        specs["Total RAM (GB)"] = f"{ram_gb} GB"
    except:
        specs["Total RAM (GB)"] = mem_total
        
    print(json.dumps(specs, indent=4))
