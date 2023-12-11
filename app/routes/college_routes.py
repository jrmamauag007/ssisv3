from flask import Blueprint, request, render_template
from app.models.college_models import CollegeModel

college = Blueprint('college', __name__)

@college.route('/colleges', methods=['GET'])
def get_all_colleges():
    colleges = CollegeModel.get_colleges()
    return render_template('colleges.html', collegelist=colleges)

@college.route('/college/<collegecode>', methods=['GET'])
def get_college(collegecode):
    college = CollegeModel.get_college_by_code(collegecode)
    if college:
        return render_template('college_detail.html', college=college)
    else:
        return render_template('college_not_found.html'), 404

@college.route('/college', methods=['POST'])
def add_new_college():
    data = request.get_json()
    collegecode = data.get('collegecode')
    collegename = data.get('collegename')

    CollegeModel.add_college(collegecode, collegename)

    return render_template('college_added.html', message='College added successfully'), 201

@college.route('/college/<collegecode>', methods=['PUT'])
def update_existing_college(collegecode):
    data = request.get_json()
    collegename = data.get('collegename')

    CollegeModel.update_college(collegecode, collegename)

    return render_template('college_updated.html', message='College updated successfully')

@college.route('/college/<collegecode>', methods=['DELETE'])
def delete_college_route(collegecode):
    CollegeModel.delete_college(collegecode)
    return render_template('college_deleted.html', message='College deleted successfully')
