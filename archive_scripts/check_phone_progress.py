import paramiko
import sys
import os

def run_ssh_command(host, port, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, port=port, username=user, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        out = stdout.read().decode('utf-8')
        err = stderr.read().decode('utf-8')
        print(out)
        if err:
            print(f"Errors: {err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    commands = """
    echo "--- phone_log.txt (last 5 lines) ---"
    tail -n 5 phone_log.txt 2>/dev/null
    echo "--- phone_bench.md ---"
    cat phone_bench.md 2>/dev/null
    echo "--- Status ---"
    cat bench_status.txt 2>/dev/null
    """
    run_ssh_command(os.environ["PHONE_IP"], int(os.environ.get("PHONE_PORT", "8022")), os.environ["PHONE_USER"], os.environ["PHONE_PASS"], commands)
