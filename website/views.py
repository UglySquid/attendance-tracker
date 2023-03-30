from flask import Blueprint
from flask import render_template, request, url_for, flash, redirect
import json


views = Blueprint('views', __name__,  template_folder='templates')

with open("website/attend_list.txt", "r") as f:
    attend = json.loads(f.read())
    f.close()

@views.route('/', methods=('GET', 'POST'))
def views():
    if request.method == 'POST':
        pass_code = request.form['pass_code']
        name = request.form['name']

        if not pass_code:
            flash('Pass code is required!')
        elif not name:
            flash('Name is required!')
        elif name not in attend:
            attend[name] = 1

            new_attend = json.dumps(attend)
            attendance_edit = open("attendance.txt", "w")
            attendance_edit.write(str(new_attend))
            attendance_edit.close()
            flash('Hello👋! You have been added to the attendance!')


        elif attend[name] < attend["meeting"]:
            new_attend = json.dumps(attend)
            attendance_edit = open("attendance.txt", "w")
            attendance_edit.write(str(new_attend))
            attendance_edit.close()
            flash('Hello👋! You have been added to the attendance! You can now close this tab')

        else:
            'Dingus! You have already been counted today.'

        if not pass_code:
            flash('Pass code is required!')
        elif not name:
            flash('Name is required!')
        else:
            return redirect(url_for('home'))

    return render_template('home.html')