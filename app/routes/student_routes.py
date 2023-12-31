# app/routes/student_routes.py

from flask import Blueprint, request, render_template, jsonify, flash,redirect, url_for
from app.models.student_models import StudentModel
from app.models.course_models import CourseModel

import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from urllib.parse import urlparse
from werkzeug.utils import secure_filename
import re 

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

        image = request.files.get('addFile')
        student_id = id
        image_url = None
    
        if not_valid_id(id):
            flash('Not Valid ID(YYYY-NNNN)', 'error')
            return redirect(url_for('student.get_all_students'))
        # Check if a file was provided
        if image:
            # Get the size of the file in bytes
            image_size_bytes = len(image.read())
            
            # Reset the file cursor back to the beginning for further processing
            image.seek(0)

            image_size_mb = image_size_bytes / (1024 * 1024)

            # Check if the image size exceeds the limit
            if image_size_mb > 1:
                flash(f'Image size exceeds the maximum limit of {1} MB', 'error')
                return redirect(url_for('student.get_all_students'))
            
            filename = secure_filename(request.files['addFile'].filename)
            if not allowed_file(filename):
                flash(f'Invalid file extension. Allowed extensions are: {", ".join(ALLOWED_EXTENSIONS)}', 'error')
                return redirect(url_for('student.get_all_students'))

            upload_result = cloudinary.uploader.upload(image)
            image_url = upload_result['url']

            student_model_instance = StudentModel()
            student_model_instance.associate_image_url(image_url, student_id)
            print("1")


            print("2")
            print(image_url)
        student_data = {
            'id': id,
            'firstname': firstname,
            'lastname': lastname,
            'studentyear': studentyear,
            'gender': gender,
            'coursecode': coursecode,
            'image_url': image_url
        }
        StudentModel.add_student(student_data)
        
        flash('Student created successfully', 'success')
    except Exception as e:
        print(e)
        flash('Failed to create the Student. Error: {}'.format(str(e)), 'error')

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
        
        image = request.files.get('editFile')
        student_id = id
        image_url = None
    

        # Check if a file was provided
        if image:
            # Convert image data size from bytes to megabytes

            # Get the size of the file in bytes
            image_size_bytes = len(image.read())
            
            # Reset the file cursor back to the beginning for further processing
            image.seek(0)

            image_size_mb = image_size_bytes / (1024 * 1024)
            print(image_size_mb)

            # Check if the image size exceeds the limit
            if image_size_mb > 1:
                flash(f'Image size exceeds the maximum limit of {1} MB', 'error')
                return redirect(url_for('student.get_all_students'))


            # Check if the file extension is allowed
            filename = secure_filename(request.files['editFile'].filename)
            if not allowed_file(filename):
                flash(f'Invalid file extension. Allowed extensions are: {", ".join(ALLOWED_EXTENSIONS)}', 'error')
                return redirect(url_for('student.get_all_students'))
            
            # Upload the file to Cloudinary
            oldimage = StudentModel.get_student_image_url(student_id)
            if oldimage:
                parsed_url = urlparse(oldimage)
                public_id = parsed_url.path.split("/")[-1].split(".")[0]
                cloudinary.uploader.destroy(public_id)
                print(public_id)

            
            upload_result = cloudinary.uploader.upload(image)
        
            image_url = upload_result['url']
        
            student_model_instance = StudentModel()
            student_model_instance.associate_image_url(image_url, student_id)

        student_data = {
            'id': id,
            'firstname': firstname,
            'lastname': lastname,
            'studentyear': studentyear,
            'gender': gender,
            'coursecode': coursecode,
            'image_url': image_url
        }

        StudentModel.update_student(student_data)
        flash('Student edit successfully', 'success')
    except Exception as e:
        print(e)
        flash('Failed to edit Student. Error: {}'.format(str(e)), 'error')

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

def not_valid_id(id):
    pattern = re.compile(r'^\d{4}-\d{4}$')
    return not bool(pattern.match(id))

@student.route('/student/upload-image', methods=['POST'])
def upload_image():
    try:
        # Assuming you have a form with an input field named 'file'
        student_id = request.form['student_id']
        image = request.files['file']
        
        # Check if a file was provided
        if image:
            # Get the size of the file in bytes
            image_size_bytes = len(image.read())
            
            # Reset the file cursor back to the beginning for further processing
            image.seek(0)

            image_size_mb = image_size_bytes / (1024 * 1024)

            # Check if the image size exceeds the limit
            if image_size_mb > 1:
                flash(f'Image size exceeds the maximum limit of {1} MB', 'error')
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

            upload_result = cloudinary.uploader.upload(image)
            image_url = upload_result['url']
        

            student_model_instance = StudentModel()
            student_model_instance.associate_image_url(image_url, student_id)
            flash('Image uploaded successfully', 'success')
            return redirect(url_for('student.get_student', student_id=student_id))
        else:
            flash('No or Invalid File detected', 'error')
            return redirect(url_for('student.get_student', student_id=student_id))

    except Exception as e:
        flash('Failed to upload image. Error: {}'.format(str(e)), 'error')
        print(str(e))  # Log the exception for debugging

    return redirect(url_for('student.get_all_students'))
