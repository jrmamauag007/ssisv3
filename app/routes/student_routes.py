from flask import Blueprint, request, render_template
from app.models.student_models import StudentModel

student = Blueprint('student', __name__)

@student.route('/students', methods=['GET'])
def get_all_students():
    students = StudentModel.get_students()
    return render_template('students.html', studentlist=students)

@student.route('/student/<student_id>', methods=['GET'])
def get_student(student_id):
    student = StudentModel.get_student_by_id(student_id)
    if student:
        return render_template('student_detail.html', student=student)
    else:
        return render_template('student_not_found.html'), 404

@student.route('/student', methods=['POST'])
def add_new_student():
    data = request.get_json()
    StudentModel.add_student(data)

    return render_template('student_added.html', message='Student added successfully'), 201

@student.route('/student/<student_id>', methods=['PUT'])
def update_existing_student(student_id):
    data = request.get_json()
    StudentModel.update_student(student_id, data)

    return render_template('student_updated.html', message='Student updated successfully')

@student.route('/student/<student_id>', methods=['DELETE'])
def delete_student_route(student_id):
    StudentModel.delete_student(student_id)
    return render_template('student_deleted.html', message='Student deleted successfully')
