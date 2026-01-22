from models import StudentProfile

def validate_types(data, schema):
    """
    Validates types of incoming data against schema.
    Raises TypeError if types do not match.
    """
    for key, expected_type in schema.items():
        value = data.get(key)
        if expected_type == list:
            if not isinstance(value, list):
                raise TypeError(f"{key} must be a list")
        elif not isinstance(value, expected_type):
            raise TypeError(f"{key} must be {expected_type.__name__}, got {type(value).__name__}")

def marshal_student_profile(profile: StudentProfile):
    return {
        "name": profile.name,
        "id": profile.id,
        "grades": profile.grades
    }

def unmarshal_student_profile(data):
    schema = {"name": str, "id": int, "grades": list}
    validate_types(data, schema)
    return StudentProfile(data["name"], data["id"], data["grades"])