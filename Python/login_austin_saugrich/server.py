from app import app
from app.controllers import users
from app.controllers import recipes


if __name__ == "__main__":
    app.run(debug=True)
