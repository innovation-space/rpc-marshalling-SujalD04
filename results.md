# RPC Framework Results

- Implemented StudentProfile object.
- Added marshalling layer with validate_types() to check incoming data types.
- Server raises TypeError if types do not match.
- Remote method calculate_grade_average works as expected.


**server.py**

$ python server.py
Server listening...

**client.py**

$ python client.py

Grade Average Calculation Result:
Student Name: Alice
Student ID: 123
Grades: [90, 80, 85, 79, 82, 97, 100, 58, 84, 96]
Average Grade: 85.10
