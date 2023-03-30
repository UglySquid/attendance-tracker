from flask import Blueprint

attendance = Blueprint('attendance', __name__)

@attendance.route('/attendance')
def attendance():
    return "<h1>attendance</h1>"