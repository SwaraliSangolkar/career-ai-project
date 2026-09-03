def detect_lead(student):
    if student.preferred_degree_mode.lower() in ["online degree", "distance learning"]:
        return True

    if student.counseling_interest.lower() in [
        "yes, i want counseling",
        "yes, i want more information"
    ]:
        return True

    return False


def generate_report(student):
    return f"""
=== AI CAREER REPORT ===

Name: {student.name}

Career Paths:
- Software Developer
- Data Analyst
- Web Developer

Why:
Based on your interest in {student.interests} and skills in {student.skills}

Skills to Learn:
- Python
- Data Structures
- Communication

Degree Recommendation:
- B.Tech Computer Science
- BCA / MCA

Short Term Plan (3-6 months):
- Learn Python
- Build projects
- Practice coding

Long Term Plan (1-3 years):
- Complete degree
- Get internship
- Apply for jobs

Final Recommendation:
Stay consistent and focus on skill building.
"""