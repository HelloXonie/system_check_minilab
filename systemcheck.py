import psutil
import subprocess

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_available_memory_mb():
    return psutil.virtual_memory().available / (1024 ** 2)

def ping_localhost():
    result = subprocess.run(["ping", "-c", "1", "127.0.0.1"], capture_output=True)
    return result.returncode == o
