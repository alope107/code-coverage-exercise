def make_student(name, level, courses = None):
    student = {}
    student['name'] = name
    student['level'] = level
    if not courses:
        corses = []
    student['courses'] = courses
    return student

def add_course(student, course_name):
    student['courses'].append(course_name)

def get_num_classes(student):
    return len(student['courses'])

def summary(student):
    return f"{student['name']} is a {student['level']} enrolled in {get_num_classes(student)} classes"

def get_student_with_more_classes(student_a, student_b):
    if get_num_classes(student_a) > get_num_classes(student_b):
        return student_b
    return student_b
