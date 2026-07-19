import paramiko
import sys

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
    run_ssh_command('10.88.85.133', 8022, 'u0_a346', '1234567890', commands)
