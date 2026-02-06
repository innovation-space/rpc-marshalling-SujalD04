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


# RPC vs Local Calculation Comparison

Student Name: Alice
Student ID: 123
Grades: [90, 80, 85, 79, 82, 97, 100, 58, 84, 96]

| Metric                | RPC           | Local         |
|-----------------------|---------------|---------------|
| Average Grade         | 85.10         | 85.10         |
| Correctness           | Match         | Match         |
| Execution Time (sec)  | 0.006914      | 0.000006      |
| Peak Memory (bytes)   | 47            | 24            |

**Summary:**
- Both RPC and local calculations produce the same result (correctness: Match).
- Local execution is significantly faster and uses less memory, as expected.
- RPC introduces overhead due to network and serialization.
