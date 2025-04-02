#app.py
from flask import Flask, render_template, request
from key import key
from main import get_symbol, render_chart

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  chart_created = False
  chart_filename = None
  symbol = None
  frame = None

  if request.method == 'POST':
    symbol = request.form['symbol']
    chart_type = int(request.form['chart_type'])
    time_series = int(request.form['time_series'])
    frame = request.form.get('frame')

    opens, highs, lows, closes, frame = get_symbol(symbol, time_series)
    chart_filename = render_chart(chart_type, opens, highs, lows, closes)
    chart_created = True

  return render_template('index.html', chart_created=chart_created, chart_filename=chart_filename, symbol=symbol, frame=frame)

if __name__ == '__main__':
  app.run(debug=True)
