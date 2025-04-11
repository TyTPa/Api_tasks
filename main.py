# импортируем Flask и библиотеку Request
from flask import Flask, render_template, request
import requests

# импортируем объект класса Flask
app = Flask(__name__)

# формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        # прописываем переменную, куда будет сохраняться результат и функцию weather с указанием города, который берём из формы
        weather = get_weather(city)
    # передаем информацию о погоде в index.html
    return render_template("index.html", weather=weather)
#        news = get_news()
#   return render_template("index.html", weather=weather, news=news)

# в функции прописываем город, который мы будем вводить в форме
def get_weather(city):
    api_key = "01d60d241916f5d850574139c275f457"
    # адрес, по которому мы будем отправлять запрос. Не забываем указывать f строку.
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    # для получения результата нам понадобится модуль requests
    response = requests.get(url)
    # прописываем формат возврата результата
    return response.json()

# Переходим на сайт newsapi.org  и новости с него
def get_news():
   api_key = "a617b533135849c1b9cf361a6b4b84ea"
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
   response = requests.get(url)
   return response.json().get('articles', [])

# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
