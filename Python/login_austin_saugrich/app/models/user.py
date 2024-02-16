from app.config.mysqlconnection import MySQLConnection
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def add(cls, data):
        query = """
        INSERT INTO users(first_name, email, password)
VALUES(%(first_name)s, %(email)s, %(password)s);
        """

        return MySQLConnection('login_form').query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = """
        UPDATE users SET first_name = %(first_name)s, email = %(email)s, password = %(password)s
WHERE users.id = %(id)s
        """
        return MySQLConnection('login_form').query_db(query, data)

    @classmethod
    def delete(cls, id):
        query = """
        DELETE FROM users WHERE users.id = %(id)s
        """
        return MySQLConnection('login_form').query_db(query, {'id': id})

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
        query = 'SELECT * from users WHERE users.id = %(id)s;'

        results = MySQLConnection('login_form').query_db(query, {'id': id})

        return User(results[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = MySQLConnection("login_form").query_db(query, data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_user_info(user):
        is_valid = True
        if len(user["first_name"]) < 2:
            flash('First name must be at least 2 characters!')
            is_valid = False
        if len(user["last_name"]) < 2:
            flash('Last name must be at least 2 characters!')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address!')
            is_valid = False
        if len(user["password"]) < 8:
            flash('Password must be at least 8 characters!')
            is_valid = False
        if not user['password'] == user['confirm_password']:
            flash('Passwords dont match')
            is_valid = False
        return is_valid

    @staticmethod
    def validate_user_login(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid email address!')
            is_valid = False
        return is_valid
