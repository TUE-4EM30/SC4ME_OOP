import json, gitlab, Levenshtein, os
from canvasapi import Canvas
from keys import canvas_key, gitlab_key

with open('course.json', 'r') as json_file:
  course_details = json.load(json_file)
  students_file  = f'students_{course_details["year"]}.json'

# open canvas and gitlab
canvas = Canvas('https://canvas.tue.nl', canvas_key)
gl = gitlab.Gitlab('https://gitlab.tue.nl', private_token=gitlab_key)

# get the course
course   = canvas.get_course(course_details['id'])
students = course.get_users(enrollment_type=['student'])

# get the students dictionary
if os.path.isfile(students_file):
  with open(students_file, 'r') as json_file:
     students_dict = json.load(json_file)
else:
  students_dict = {}

⋮