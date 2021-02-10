from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        c = request.form.get('city')
    else:
        c = 'Mumbai'

    url = 'http://api.openweathermap.org/data/2.5/weather?units=metric&q={}&appid=715ae271aba5e6fb65473723fa58e745'

    r = requests.get(url.format(c)).json()
    print(r)


    weather = {
        'city': c.capitalize(),
        'temperature': r['main']['temp'],
        'description':  r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    print(weather)
    return render_template('weather.html', weather = weather)

if __name__ == "__main__":
    app.run(debug=True)
