from flask import Blueprint, request, jsonify
from app.models.course_models import CourseModel

course = Blueprint('course', __name__)

@course.route('/courses', methods=['GET'])
def get_all_courses():
    courses = CourseModel.get_courses()
    return jsonify(courses)

@course.route('/course/<course_code>', methods=['GET'])
def get_course(course_code):
    course = CourseModel.get_course_by_code(course_code)
    if course:
        return jsonify(course)
    else:
        return jsonify({'message': 'Course not found'}), 404

@course.route('/course', methods=['POST'])
def add_new_course():
    data = request.get_json()
    CourseModel.add_course(data)

    return jsonify({'message': 'Course added successfully'}), 201

@course.route('/course/<course_code>', methods=['PUT'])
def update_existing_course(course_code):
    data = request.get_json()
    CourseModel.update_course(course_code, data)

    return jsonify({'message': 'Course updated successfully'})

@course.route('/course/<course_code>', methods=['DELETE'])
def delete_course_route(course_code):
    CourseModel.delete_course(course_code)
    return jsonify({'message': 'Course deleted successfully'})
