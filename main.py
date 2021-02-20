from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def main():
    style = str(render_template('style.css'))
    return render_template('index.html', css=style)

@app.route('/<string:var>')
def result(var):
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    api_weather = '780c80b5359ef7a22a6af533bff3b43c'

    params = {'APPID': api_weather, 'q':   var, 'units': 'metric', 'lang': 'uz'}
    result = requests.get(url, params=params)
    weather = result.json()
    print(weather)
    if weather["main"]['temp'] < 3:
        status = "Hozir sovuq!"
    elif weather["main"]['temp'] < 15:
        status = "Hozir salqin!"
    elif weather["main"]['temp'] < 38 and weather["main"]['temp'] > 20:
        status = "Hozir Issiq!"
    else:
        status = "Endi harorat juda yaxshi!"
          
    res = {'temp': str(float(weather["main"]['temp'])), #Harorat
           'wind_speed': str(float(weather["wind"]['speed'])), #Shamol tezligi
           'pressure': str(float(weather['main']['pressure'])), #Bosim
           'humidity': str(int(weather['main']['humidity'])), #Namlik
           'vis': str(weather['visibility']), #Ko'rinish
           'status': status}

    style = str(render_template('style2.css'))
    return render_template('results.html',city=var,css=style,
    res1=res['temp'], res2=res['wind_speed'], res3=res['pressure'], res4=res['humidity'],
    res5=res['vis'], res6=res['status'])

if __name__ == '__main__':
    app.run()
