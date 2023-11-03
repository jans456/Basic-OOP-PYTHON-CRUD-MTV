# app.py
from flask import Flask
from routes.DosenRoute import app_dosen
app = Flask(__name__)

app.register_blueprint(app_dosen, url_prefix='/dosen')

if __name__ == '__main__':
    app.run(debug=True)