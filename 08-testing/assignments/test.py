import pytest
import System


username = 'calyam'
password =  '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
course = 'cloud_computing'
assignment = 'assignment1'
profUser = 'goggins'
profPass = 'augurrox'

#Tests if the program can handle a wrong username
def test_login(grading_system):
    grading_system.login(username, password)
    assert grading_system.usr.name == username

def test_check_password(grading_system):
    test = grading_system.check_password(username,password)
    test2 = grading_system.check_password(username,'#yeet')
    test3 = grading_system.check_password(username,'#YEET')
    if test == test3 or test2 == test3:
        assert False
    if test != test2:
        assert False

def test_change_grade(grading_system):
    grading_system.login(username, password)
    grading_system.usr.change_grade(username, course, assignment, 80)
    assert grading_system.users[username]['courses'][course][assignment]['grade'] == 80

def test_create_assignment(grading_system):
    due_date = '12/31/21'
    grading_system.login(username, password)
    grading_system.usr.create_assignment(assignment, due_date, course)
    assert grading_system.courses[course]['assignments'][assignment]['due_date'] == due_date

# There is an error with the add_student function
def test_add_student(grading_system):
    grading_system.login(username, password)
    grading_system.usr.add_student(username3, course)
    assert grading_system.users[username3]['courses'][-1] == course

def test_drop_student(grading_system):
    grading_system.login(username, password)
    grading_system.usr.drop_student(username2, course)
    assert grading_system.users[username2]['courses'][0] != course

def test_submit_assignment(grading_system):
    user = 'akend3'
    password = '123454321'
    grading_system.login(user, password)
    grading_system.usr.submit_assignment('databases', assignment, 'test-submission', '10/31/21')
    assert grading_system.users[user]['courses']['databases'][assignment]['submission'] == 'test-submission'

def test_check_ontime(grading_system):
    grading_system.login('akend3', '123454321')
    assert grading_system.usr.check_ontime('1/28/20', '2/5/20') == True 
    assert grading_system.usr.check_ontime('2/10/20', '2/15/20') == False

def test_check_grades(grading_system):
    grading_system.login('akend3', '123454321')
    grades = grading_system.usr.check_grades('databases')
    assert grades[1][1] == 46

def test_view_assignments(grading_system):
    grading_system.login('akend3', '123454321')
    assignments = grading_system.usr.view_assignments('databases')
    assert assignments[0][1] == grading_system.courses['databases']['assignments']['assignment1']['due_date'] == '2/8/20'

def test_addStudent(grading_system):
    grading_system.login(profUser, profPass)
    grading_system.usr.add_student(username, 'cloud_computing')
    assert grading_system.users['goggins']['courses'][3] == 'cloud_computing'

def test_dropStudent_error(grading_system):
    grading_system.login(profUser, profPass)
    grading_system.usr.drop_student(username3, 'cloud_computing')
    assert grading_system.users['yted91']['courses'][0] != 'cloud_computing'

def test_changeGrade(grading_system):
    grading_system.login(profUser, profPass)
    grading_system.usr.change_grade(username3, 'databases', assignment, 45)
    assert grading_system.users[username3]['courses']['databases'][assignment]['grade'] == 80



# I'm really not sure what you want me to write tests for when every single function 
# is already being tested.


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
