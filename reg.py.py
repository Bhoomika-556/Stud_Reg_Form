from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'example.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'replace-with-a-secure-random-key'

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    course = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Student {self.name}>'


# CREATE + READ (list all students)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        course = request.form.get('course')
        age = request.form.get('age')

        if not name or not email or not course or not age:
            flash('All fields are required.', 'error')
            return redirect(url_for('index'))

        new_student = Student(name=name, email=email, course=course, age=age)
        try:
            db.session.add(new_student)
            db.session.commit()
            flash('Student registered successfully.', 'success')
        except Exception:
            db.session.rollback()
            flash('Error: email may already be registered.', 'error')

        return redirect(url_for('index'))

    students = Student.query.all()
    return render_template('index.html', students=students)


# UPDATE (edit an existing student)
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    student = Student.query.get_or_404(id)

    if request.method == 'POST':
        student.name = request.form.get('name')
        student.email = request.form.get('email')
        student.course = request.form.get('course')
        student.age = request.form.get('age')

        try:
            db.session.commit()
            flash('Student updated successfully.', 'success')
        except Exception:
            db.session.rollback()
            flash('Error updating student.', 'error')

        return redirect(url_for('index'))

    students = Student.query.all()
    return render_template('index.html', students=students, edit_student=student)


# DELETE
@app.route('/delete/<int:id>')
def delete(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted successfully.', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)