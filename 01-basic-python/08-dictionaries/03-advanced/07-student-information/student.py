# Write your code here
def process_data(string_data):
    students = {}
    for item in string_data:
        name, age, *courses = item.split(",")

        students[name] = { 'age': int(age), 'courses': courses }

    return students

def average_age(data):
    total_age = 0
    for item in data.values():
        total_age += item['age']

    return total_age / data.__len__()

def courses(data):
    courses_list = []
    for item in data.values():
        for course in item['courses']:
            courses_list.append(course)

    return set(courses_list)

def most_common_courses(data):
    counted_courses = {}

    for item in data.values():
        for course in item['courses']:
            if course not in counted_courses:
                counted_courses[course] = 1
            
            counted_courses[course] += 1
    
    most_common_course_count = max(counted_courses.values())
    common_courses = []

    for course, value in counted_courses.items():
        if value >= most_common_course_count:
            common_courses.append(course)

    return set(common_courses)    