# Importing Dependencies #
from APIs import *
from flask_cors import CORS


# Creating Flask App #
app = Flask(__name__)
CORS(app)

# ---------------- APIs ---------------- #
app.add_url_rule(rule='/create/', endpoint='create', methods=['POST'], view_func=create)


# For Local Testing #
if __name__ == '__main__':
    app.run(debug=True)