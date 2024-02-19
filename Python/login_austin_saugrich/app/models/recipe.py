from app.config.mysqlconnection import MySQLConnection
from app.models.user import User
from flask import flash


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under = data['under']
        self.date = data['date']

        self.user = None
        self.author = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id"
        results = MySQLConnection('login_form').query_db(query)
        all_recipes = []
        for row in results:
            recipe = cls(row)
            recipe.user = User({
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password']
            })
            all_recipes.append(recipe)
        return all_recipes

    @classmethod
    def add(cls, data):
        query = """
        INSERT INTO recipes (name, description, instructions, under, date, user_id)
        VALUES (%(name)s, %(description)s, %(instructions)s, %(under)s, %(date)s, %(user_id)s)
        """

        return MySQLConnection('login_form').query_db(query, data)

    @classmethod
    def get_recipe_by_user_id(cls, id):
        query = 'SELECT * FROM recipes WHERE user_id = %(id)s;'

        results = MySQLConnection('login_form').query_db(query, {'id': id})

        all_recipes = []
        for row in results:
            all_recipes.append(Recipe(row))
        return all_recipes

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s"

        results = MySQLConnection('login_form').query_db(query, {'id': id})

        recipe = Recipe(results[0])
        recipe.user = results[0]['user_id']
        recipe.author = results[0]['first_name']
        return recipe

    @classmethod
    def edit(cls, data):
        query = """
        UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, under = %(under)s, date = %(date)s
WHERE recipes.id = %(id)s
        """
        return MySQLConnection('login_form').query_db(query, data)

    @classmethod
    def delete(cls, id):
        query = """
        DELETE FROM recipes WHERE recipes.id = %(id)s
        """
        return MySQLConnection('login_form').query_db(query, {'id': id})

    @staticmethod
    def validate_form(recipe):
        print(recipe)
        is_valid = True
        if len(recipe["name"]) < 3:
            flash('The name must be at least 3 characters!', 'create')
            is_valid = False
        if len(recipe["description"]) < 3:
            flash('The description must be at least 3 characters!', 'create')
            is_valid = False
        if len(recipe["instructions"]) < 3:
            flash('The instructions must be at least 3 characters!', 'create')
            is_valid = False
        try:
            if recipe['under']:
                print()
        except KeyError:
            flash('Was it cooked under 30 minutes?', 'create')
            is_valid = False
        return is_valid
