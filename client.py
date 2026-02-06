import socket
import json
from models import StudentProfile
from marshalling import marshal_student_profile
import time
import tracemalloc

def remote_calculate_grade_average(profile: StudentProfile, host="localhost", port=5000):
    s = socket.socket()
    s.connect((host, port))
    request = {
        "method": "calculate_grade_average",
        "params": marshal_student_profile(profile)
    }
    s.send(json.dumps(request).encode())
    response = s.recv(4096).decode()
    s.close()
    return json.loads(response)

def local_calculate_grade_average(profile: StudentProfile):
    if not profile.grades:
        return 0.0
    return sum(profile.grades) / len(profile.grades)

# ...existing code...
if __name__ == "__main__":
    profile = StudentProfile("Alice", 123, [90, 80, 85, 79, 82, 97, 100, 58, 84, 96])

    # --- RPC call ---
    tracemalloc.start()
    start_time = time.perf_counter()
    response = remote_calculate_grade_average(profile)
    rpc_time = time.perf_counter() - start_time
    rpc_mem, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # --- Local call ---
    tracemalloc.start()
    start_time = time.perf_counter()
    local_result = local_calculate_grade_average(profile)
    local_time = time.perf_counter() - start_time
    local_mem, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # --- Output ---
    print("\nComparison: RPC vs Local Calculation")
    print(f"Student Name: {profile.name}")
    print(f"Student ID: {profile.id}")
    print(f"Grades: {profile.grades}")

    if "result" in response:
        print(f"\n[RPC] Average Grade: {response['result']:.2f}")
    elif "error" in response:
        print("\n*** RPC ERROR ***")
        print(response["error"])
    print(f"[Local] Average Grade: {local_result:.2f}")

    # Correctness
    if "result" in response:
        correct = abs(response["result"] - local_result) < 1e-6
        print(f"\nCorrectness: {'Match' if correct else 'Mismatch'}")
    else:
        print("\nCorrectness: Cannot determine (RPC error)")

    # Timing
    print(f"\nExecution Time (seconds):")
    print(f"  RPC:   {rpc_time:.6f}")
    print(f"  Local: {local_time:.6f}")

    # Resource usage (peak memory in bytes)
    print(f"\nPeak Memory Usage (bytes):")
    print(f"  RPC:   {rpc_mem}")
    print(f"  Local: {local_mem}")
# ...existing code...