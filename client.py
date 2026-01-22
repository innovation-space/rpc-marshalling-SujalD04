import socket
import json
from models import StudentProfile
from marshalling import marshal_student_profile

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

# ...existing code...
if __name__ == "__main__":
    profile = StudentProfile("Alice", 123, [90, 80, 85, 79, 82, 97, 100, 58, 84, 96])
    response = remote_calculate_grade_average(profile)
    if "result" in response:
        print("\nGrade Average Calculation Result:")
        print(f"Student Name: {profile.name}")
        print(f"Student ID: {profile.id}")
        print(f"Grades: {profile.grades}")
        print(f"Average Grade: {response['result']:.2f}")
    elif "error" in response:
        print("\n*** ERROR ***")
        print(response["error"])
        print("*************\n")
# ...existing code...