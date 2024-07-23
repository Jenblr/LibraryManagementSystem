# This file contains the routes (endpoints) for Flask application
# app/routes.py
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from . import db
from .models import Book, User, Loan

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

# Routes for books
@main.route('/books')
def get_books():
    books = Book.query.all()
    return render_template('books.html', books=books)

@main.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        data = request.form
        new_book = Book(title=data['title'], author=data['author'], published_date=data['published_date'], isbn=data['isbn'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('main.get_books'))
    return render_template('add_book.html')

@main.route('/update_book/<int:id>', methods=['GET', 'POST'])
def update_book(id):
    book = Book.query.get(id)
    if request.method == 'POST':
        data = request.form
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        book.published_date = data.get('published_date', book.published_date)
        book.isbn = data.get('isbn', book.isbn)
        db.session.commit()
        return redirect(url_for('main.get_books'))
    return render_template('update_book.html', book=book)

@main.route('/delete_book/<int:id>', methods=['GET', 'POST'])
def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('main.get_books'))

# Routes for users
@main.route('/users')
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@main.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        data = request.form
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.get_users'))
    return render_template('add_user.html')

@main.route('/update_user/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    user = User.query.get(id)
    if request.method == 'POST':
        data = request.form
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        db.session.commit()
        return redirect(url_for('main.get_users'))
    return render_template('update_user.html', user=user)

@main.route('/delete_user/<int:id>', methods=['GET', 'POST'])
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('main.get_users'))

# Routes for loaning books
@main.route('/loans')
def get_loans():
    loans = Loan.query.all()
    return render_template('loans.html', loans=loans)

@main.route('/add_loan', methods=['GET', 'POST'])
def add_loan():
    if request.method == 'POST':
        data = request.form
        new_loan = Loan(book_id=data['book_id'], user_id=data['user_id'], loan_date=data['loan_date'], return_date=data.get('return_date'))
        db.session.add(new_loan)
        db.session.commit()
        return redirect(url_for('main.get_loans'))
    return render_template('add_loan.html')

@main.route('/update_loan/<int:id>', methods=['GET', 'POST'])
def update_loan(id):
    loan = Loan.query.get(id)
    if request.method == 'POST':
        data = request.form
        loan.book_id = data.get('book_id', loan.book_id)
        loan.user_id = data.get('user_id', loan.user_id)
        loan.loan_date = data.get('loan_date', loan.loan_date)
        loan.return_date = data.get('return_date', loan.return_date)
        db.session.commit()
        return redirect(url_for('main.get_loans'))
    return render_template('update_loan.html', loan=loan)

@main.route('/delete_loan/<int:id>', methods=['GET', 'POST'])
def delete_loan(id):
    loan = Loan.query.get(id)
    if loan:
        db.session.delete(loan)
        db.session.commit()
    return redirect(url_for('main.get_loans'))