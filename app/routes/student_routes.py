# app/routes/student_routes.py

from flask import Blueprint, request, render_template, jsonify, flash,redirect, url_for
from app.models.student_models import StudentModel
from app.models.course_models import CourseModel

student = Blueprint('student', __name__)

@student.route('/students', methods=['GET'])
def get_all_students():

    students = StudentModel.get_students()
    courses = CourseModel.get_courses()

    return render_template("students.html", studentlist=students, courselist=courses)


@student.route('/add_student', methods=['POST'])
def add_student():
    try:
        data = request.form
        id = data.get('studentid') 
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        studentyear = data.get('studentyear')
        gender = data.get('gender')
        coursecode = data.get('coursecode')

        student_data = {
            'id': id,
            'firstname': firstname,
            'lastname': lastname,
            'studentyear': studentyear,
            'gender': gender,
            'coursecode': coursecode
        }

        # Call the model function to add a student
        StudentModel.add_student(student_data)
        flash('Student created successfully', 'success')
    except Exception as e:
        flash('Failed to create the Student', 'error')

    return redirect(url_for('student.get_all_students'))   

@student.route('/student/<student_id>', methods=['GET'])

def get_student(student_id):
    student = StudentModel.get_student_by_id(student_id)
    if student:
        return render_template('student_detail.html', student=student)
    else:
        flash('Failed to load Student', 'error')
    
    
@student.route('/update_student', methods=['POST'])
def update_student():
    try:
        data = request.form
        id = data.get('editStudentID') 
        firstname = data.get('editFirstName')
        lastname = data.get('editLastName')
        studentyear = data.get('editStudentYear')
        gender = data.get('editGender')
        coursecode = data.get('editCourseCode')

        student_data = {
            'id': id,
            'firstname': firstname,
            'lastname': lastname,
            'studentyear': studentyear,
            'gender': gender,
            'coursecode': coursecode
        }

        # Call the model function to add a student
        StudentModel.update_student(student_data)
        flash('Student edit successfully', 'success')
    except Exception as e:
        flash('Failed to edit Student', 'error')

    return redirect(url_for('student.get_all_students'))

@student.route('/delete_student/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        # Call the delete_student function from student_models.py
        StudentModel.delete_student(student_id)
        flash('Student deleted successfully', 'success')
        
    except Exception as e:
        flash('Failed to delete Student', 'error')
    
    return redirect(url_for('student.get_all_students'))
