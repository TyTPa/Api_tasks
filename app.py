import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def get_random_quote():
    try:
        response = requests.get('https://api.quotable.io/random', verify=False)
        response.raise_for_status()  # Проверка наличия ошибок HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quote: {e}")
        return None

@app.route('/')
def index():
    quote = get_random_quote()
    return render_template('ind.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
