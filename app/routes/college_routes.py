from flask import Blueprint, request, render_template, jsonify, flash,redirect, url_for

from app.models.college_models import CollegeModel

college = Blueprint('college', __name__)

@college.route('/colleges', methods=['GET'])
def get_all_colleges():
    colleges = CollegeModel.get_colleges()
    return render_template('colleges.html', collegelist=colleges)

@college.route('/add_college', methods=['POST'])
def add_college():
    try:
        data = request.form
        collegecode = data.get('collegecode')
        collegename = data.get('collegename')

        college_data = {
            'collegecode': collegecode,
            'collegename': collegename,
        }

        # Call the model function to add a college
        CollegeModel.add_college(college_data)
        flash('College created successfully', 'success')
    except Exception as e:
        flash('Failed to create College. Error: {}'.format(str(e)), 'error')

    return redirect(url_for('college.get_all_colleges'))   


@college.route('/update_college', methods=['POST'])
def update_college():

    data = request.form
    collegecode = data.get('editCollegeCode')
    collegename = data.get('editCollegeName')

    college_data = {
            'collegecode': collegecode,
            'collegename': collegename,
        }
    try:
        CollegeModel.update_college(college_data)
        flash('College edit successfully', 'success')
        
    except Exception as e:
        flash('Failed to edit college', 'error')
    
    return redirect(url_for('college.get_all_colleges'))  


@college.route('/delete_college/<string:collegecode>', methods=['DELETE'])
def delete_college(collegecode):
    try:
        # Call the delete_college function from college_models.py
        CollegeModel.delete_college(collegecode)
        flash('College deleted successfully', 'success')
        
    except Exception as e:
        flash('Failed to delete college', 'error')
    
    return redirect(url_for('college.get_all_colleges'))  