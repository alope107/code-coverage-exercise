from student.student import add_course, make_student, get_student_with_more_classes, summary, get_num_classes, get_student_with_more_classes

def test_make_student():
    name = 'Ada Lovelace'
    level = 'sophomore'
    courses = ['mathematics', 'foundations of computing']

    ada = make_student(name, level, courses)

    assert ada['name'] == name
    assert ada['level'] == level
    assert ada['courses'] == courses

def test_add_course():
    new_course = 'Intro to Feminism'
    charles = make_student('Charles Babbage', 'senior', ['mechanical engineering'])
    add_course(charles, new_course)

    assert len(charles['courses']) == 2
    assert new_course in charles['courses']

def test_get_num_classes():
    george = make_student('George Byron', 'senior', ['advanced poetry'])

    assert get_num_classes(george) == 1

def test_summary():
    anne = make_student(
        'Anne Byron',
        'senior',
        ['theory of religion', 'theory of morality']
    )

    assert summary(anne) == 'Anne Byron is a senior enrolled in 2 classes'

def test_get_student_with_more_classes():
    charles = make_student('Charles Babbage', 'senior', ['mechanical engineering'])
    ada = make_student(
        'Ada Lovelace',
        'sophomore',
        ['mathematics', 'foundations of computing']
    )

    # TODO: write assertions
