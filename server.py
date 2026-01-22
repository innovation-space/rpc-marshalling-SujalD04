import socket
import json
from models import StudentProfile
from marshalling import unmarshal_student_profile

def calculate_grade_average(profile: StudentProfile) -> float:
    if not profile.grades:
        return 0.0
    return sum(profile.grades) / len(profile.grades)

def handle_request(request):
    data = json.loads(request)
    if data["method"] == "calculate_grade_average":
        profile = unmarshal_student_profile(data["params"])
        result = calculate_grade_average(profile)
        return json.dumps({"result": result})

def start_server(host="localhost", port=5000):
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    print("Server listening...")
    while True:
        conn, _ = s.accept()
        request = conn.recv(4096).decode()
        try:
            response = handle_request(request)
        except TypeError as e:
            response = json.dumps({"error": str(e)})
        conn.send(response.encode())
        conn.close()

if __name__ == "__main__":
    start_server()