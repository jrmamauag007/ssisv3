# app/routes/course_routes.py

from flask import Blueprint, request, render_template, jsonify, flash,redirect, url_for
from app.models.course_models import CourseModel

course = Blueprint('course', __name__)

@course.route('/courses', methods=['GET'])
def get_all_courses():
    courses = CourseModel.get_courses()
    return render_template('courses.html', courselist=courses)

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

@course.route('/update_course', methods=['PUT'])
def update_course(course_code):
    data = request.get_json()
    CourseModel.update_course(course_code, data)
    return jsonify({'message': 'Course updated successfully'})

@course.route('/delete_course/<course_code>', methods=['DELETE'])
def delete_course(course_code):
    success = CourseModel.delete_course(course_code)
    
    if success:
        return jsonify({'message': 'Course deleted successfully'})
    else:
        return jsonify({'message': 'Failed to delete course'}), 500
