from systemcheck import get_cpu_usage, get_available_memory_mb, ping_localhost

def test_cpu_usage():
    usage = get_cpu_usage()
    assert usage < 90, f"CPU usage is too high: {usage}%"

def test_memory_available():
    mem = get_available_memory_mb()
    assert mem > 200, f"Not enough memory available: {mem:.2f}MB"

def test_can_ping_localhost():
    assert ping_localhost(), "Failed to ping local host."
