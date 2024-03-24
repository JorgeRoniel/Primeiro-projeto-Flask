from flask import Flask
from configure import configureAll

app = Flask(__name__)
configureAll(app)


app.run(debug=True)