from flask import Blueprint, request, jsonify
from app.models.college_models import CollegeModel

college = Blueprint('college', __name__)

@college.route('/colleges', methods=['GET'])
def get_all_colleges():
    colleges = CollegeModel.get_colleges()
    return jsonify(colleges)

@college.route('/college/<collegecode>', methods=['GET'])
def get_college(collegecode):
    college = CollegeModel.get_college_by_code(collegecode)
    if college:
        return jsonify(college)
    else:
        return jsonify({'message': 'College not found'}), 404

@college.route('/college', methods=['POST'])
def add_new_college():
    data = request.get_json()
    collegecode = data.get('collegecode')
    collegename = data.get('collegename')

    CollegeModel.add_college(collegecode, collegename)

    return jsonify({'message': 'College added successfully'}), 201

@college.route('/college/<collegecode>', methods=['PUT'])
def update_existing_college(collegecode):
    data = request.get_json()
    collegename = data.get('collegename')

    CollegeModel.update_college(collegecode, collegename)

    return jsonify({'message': 'College updated successfully'})

@college.route('/college/<collegecode>', methods=['DELETE'])
def delete_college_route(collegecode):
    CollegeModel.delete_college(collegecode)
    return jsonify({'message': 'College deleted successfully'})
