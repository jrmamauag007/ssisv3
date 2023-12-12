from flask import Flask, session
from flask_mysql_connector import MySQL
from flask_bootstrap import Bootstrap
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL
from datetime import timedelta
from flask_wtf.csrf import CSRFProtect


mysql = MySQL()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST,
        #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
        PERMANENT_SESSION_LIFETIME=timedelta(days=1).total_seconds()
    )

    bootstrap.init_app(app)
    mysql.init_app(app)
    #CSRFProtect(app)
    

    from .routes.college_routes import college
    from .routes.course_routes import course
    from .routes.student_routes import student
    from .routes.home_routes import home

    app.register_blueprint(home)
    app.register_blueprint(college, url_prefix='/')
    app.register_blueprint(course, url_prefix='/')
    app.register_blueprint(student, url_prefix='/')

    return app
