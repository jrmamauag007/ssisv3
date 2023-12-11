from flask import Blueprint, request, jsonify
from app.models.student_models import StudentModel


student = Blueprint('student', __name__)

@student.route('/students', methods=['GET'])
def get_all_students():
    students = StudentModel.get_students()
    return jsonify(students)

@student.route('/student/<student_id>', methods=['GET'])
def get_student(student_id):
    student = StudentModel.get_student_by_id(student_id)
    if student:
        return jsonify(student)
    else:
        return jsonify({'message': 'Student not found'}), 404

@student.route('/student', methods=['POST'])
def add_new_student():
    data = request.get_json()
    StudentModel.add_student(data)

    return jsonify({'message': 'Student added successfully'}), 201

@student.route('/student/<student_id>', methods=['PUT'])
def update_existing_student(student_id):
    data = request.get_json()
    StudentModel.update_student(student_id, data)

    return jsonify({'message': 'Student updated successfully'})

@student.route('/student/<student_id>', methods=['DELETE'])
def delete_student_route(student_id):
    StudentModel.delete_student(student_id)
    return jsonify({'message': 'Student deleted successfully'})
