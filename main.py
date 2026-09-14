from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    url = 'https://zenquotes.io/api/random'

    response = requests.get(url)
    data = response.json()

    quote = data[0]['q']
    author = data[0]['a']

    return render_template(
        'index.html',
        quote=quote,
        author=author
    )


if __name__ == '__main__':
    app.run(debug=True)