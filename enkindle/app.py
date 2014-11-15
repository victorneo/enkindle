from flask import Flask, request, render_template
from flask.ext.assets import Environment


app = Flask(__name__)
assets = Environment()
assets.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
