from flask import Blueprint, render_template, redirect, url_for, flash, request
from .db import db, User      # Import db and User from db.py
from .forms import RegistrationForm, UpdateForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already registered.', 'danger')
            return render_template('register.html', form=form)
        user = User(
            username=form.username.data,
            email=form.email.data,
            bio=form.bio.data,
            age=form.age.data,
            location=form.location.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('main.profile', user_id=user.id))
    return render_template('register.html', form=form)

@main.route('/profile/<int:user_id>')
def profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('profile.html', user=user)

@main.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update(user_id):
    user = User.query.get_or_404(user_id)
    form = UpdateForm(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.bio = form.bio.data
        user.age = form.age.data
        user.location = form.location.data
        db.session.commit()
        flash('Profile updated!', 'success')
        return redirect(url_for('main.profile', user_id=user.id))
    return render_template('update.html', form=form, user=user)
