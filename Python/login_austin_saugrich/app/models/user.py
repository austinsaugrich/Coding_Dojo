from app.config.mysqlconnection import MySQLConnection
from flask import flash
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

        self.recipes = []

    @classmethod
    def add(cls, data):
        query = """
        INSERT INTO users(first_name, last_name, email, password)
VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        print(data)

        return MySQLConnection('login_form').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'

        results = MySQLConnection('login_form').query_db(query)

        all_users = []
        for row in results:
            all_users.append(User(row))
        return all_users

    @classmethod
    def get_by_id(cls, id):
        from app.models.recipe import Recipe
        query = """
        SELECT * FROM users 
        LEFT JOIN recipes ON recipes.user_id = users.id
        WHERE users.id = %(id)s;
        """

        results = MySQLConnection('login_form').query_db(query, {'id': id})

        user = cls(results[0])

        for row in results:
            if row['recipes.id'] is not None:
                user.recipes.append(Recipe({
                    'id': row['recipes.id'],
                    'name': row['name'],
                    'description': row['description'],
                    'instructions': row['instructions'],
                    'under': row['under'],
                    'date': row['date'],

                }))
            return user

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = MySQLConnection("login_form").query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_user_info(user):
        is_valid = True
        if len(user["first_name"]) < 2:
            flash('First name must be at least 2 characters!', 'register')
            is_valid = False
        if len(user["last_name"]) < 2:
            flash('Last name must be at least 2 characters!', 'register')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address!', 'register')
            is_valid = False
        if not PASSWORD_REGEX.match(user['password']):
            flash(
                'Password must be at least 8 characters, including one uppercase and a number!', 'register')
            is_valid = False
        if not user['password'] == user['confirm_password']:
            flash('Passwords dont match', 'register')
            is_valid = False
        return is_valid

    @staticmethod
    def validate_user_login(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address!', 'login')
            is_valid = False
        return is_valid
