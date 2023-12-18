# app/routes/student_routes.py

from flask import Blueprint, request, render_template, jsonify, flash,redirect, url_for
from app.models.student_models import StudentModel
from app.models.course_models import CourseModel

import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from urllib.parse import urlparse
from werkzeug.utils import secure_filename

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

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@student.route('/student/upload-image', methods=['POST'])
def upload_image():
    try:
        # Assuming you have a form with an input field named 'file'
        student_id = request.form['student_id']
        cropped_image_data = request.form['croppedImageData']

        # Check if a file was provided
        if cropped_image_data:
            # Convert image data size from bytes to megabytes
            image_size_mb = len(cropped_image_data) / (1024 * 1024)

            # Check if the image size exceeds the limit
            if image_size_mb > 5:
                flash(f'Image size exceeds the maximum limit of {5} MB', 'error')
                return redirect(url_for('student.get_student', student_id=student_id))
            
            # Check if the file extension is allowed
            filename = secure_filename(request.files['file'].filename)
            if not allowed_file(filename):
                flash(f'Invalid file extension. Allowed extensions are: {", ".join(ALLOWED_EXTENSIONS)}', 'error')
                return redirect(url_for('student.get_student', student_id=student_id))
            
            # Upload the file to Cloudinary
            oldimage = StudentModel.get_student_image_url(student_id)
            if oldimage:
                parsed_url = urlparse(oldimage)
                public_id = parsed_url.path.split("/")[-1].split(".")[0]
                cloudinary.uploader.destroy(public_id)
                print(public_id)

            upload_result = cloudinary.uploader.upload(cropped_image_data)
            image_url = upload_result['url']
            StudentModel.associate_image_url(image_url, student_id)
            flash('Image uploaded successfully', 'success')
            return redirect(url_for('student_bp.get_student', student_id=student_id))
        else:
            flash('No or Invalid File detected', 'error')
            return redirect(url_for('student.get_student', student_id=student_id))

    except Exception as e:
        flash('Failed to upload image', 'error')
        print(str(e))  # Log the exception for debugging

    return redirect(url_for('student.get_all_students'))
