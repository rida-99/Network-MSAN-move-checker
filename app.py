from flask import Flask, render_template, request
from utils.predictor import can_move_ne

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        my_bw = float(request.form['my_bw'])
        my_charge = float(request.form['my_charge'])

        peer1_bw = float(request.form['peer1_bw'])
        peer1_charge = float(request.form['peer1_charge'])

        peer2_bw = float(request.form['peer2_bw'])
        peer2_charge = float(request.form['peer2_charge'])

        result = can_move_ne(my_bw, my_charge, peer1_bw, peer1_charge, peer2_bw, peer2_charge)

        return render_template("result.html", result=result)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
