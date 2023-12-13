# app/routes/course_routes.py

from flask import Blueprint, request, render_template, jsonify, flash,redirect, url_for
from app.models.course_models import CourseModel
from app.models.college_models import CollegeModel

course = Blueprint('course', __name__)

@course.route('/courses', methods=['GET'])
def get_all_courses():

    courses = CourseModel.get_courses()
    colleges = CollegeModel.get_colleges()

    return render_template("courses.html",courselist=courses, collegelist=colleges)
    

@course.route('/add_course', methods=['POST'])
def add_course():
    try:
        data = request.form
        coursecode = data.get('coursecode') 
        coursename = data.get('coursename')
        collegecode = data.get('collegecode')

        course_data = {
            'coursecode': coursecode,
            'coursename': coursename,
            'collegecode': collegecode
        }

        # Call the model function to add a college
        CourseModel.add_course(course_data)
        flash('Course created successfully', 'success')
    except Exception as e:
        flash('Failed to create the Course', 'error')

    return redirect(url_for('course.get_all_courses'))   

@course.route('/update_course', methods=['POST'])
def update_course():

    data = request.form
    coursecode = data.get('editCourseCode')
    coursename = data.get('editCourseName')
    collegecode = data.get('editCollegeCode')

    course_data = {
        'coursecode': coursecode,
        'coursename': coursename,
        'collegecode': collegecode
        }
    try:
        CourseModel.update_course(course_data)
        flash('Course edit successfully', 'success')
        
    except Exception as e:
        flash('Failed to edit course', 'error')
    
    return redirect(url_for('course.get_all_courses')) 

@course.route('/delete_course/<course_code>', methods=['DELETE'])

def delete_course(course_code):
    try:
        # Call the delete_college function from college_models.py
        CourseModel.delete_course(course_code)
        flash('Course deleted successfully', 'success')
        
    except Exception as e:
        flash('Failed to delete Course', 'error')
    
    return redirect(url_for('course.get_all_courses')) 
