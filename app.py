from flask import Flask, render_template
import requests
from dotenv import load_dotenv, dotenv_values

config = dotenv_values('.env')

app = Flask(__name__)

def get_weather_data(city):
    API_KEY = config['API_KEY']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=es&appid={API_KEY}'
    r = requests.get(url).json()
    print(r)
    return r

@app.route('/prueba')
def prueba():
    clima = get_weather_data('Guayaquil')
    temperatura = str(clima['main']['temp'])
    descripcion = str(clima['weather'][0]['description'])
    icono = str(clima['weather'][0]['icon'])
    r_json = {
        'ciudad': 'Guayaquil',
        'temperatura': temperatura,
        'descripcion': descripcion,
        'icono': icono}
    return render_template("weather.html", clima=r_json)

@app.route('/becker')
def becker():
    get_weather_data('Guayaquil')
    return get_weather_data('Guayaquil')

@app.route('/about')
def about():
    return render_template('CV.html')

@app.route('/clima')
def clima():
    return 'Obten la información del clima'

if __name__ == '__main__':
    app.run(debug=True)