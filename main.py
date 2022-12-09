from flask import Flask, render_template


app = Flask('Cinco latidos')


@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404


@app.route('/')
def home():
    return render_template('index.html', video='https://www.youtube.com/embed/2zfofAtcoJs')


@app.route('/amazonia')
def amazonia():
    return render_template('region.html', title='Amazonía', imagen='../static/src/amazonia.png', video='https://www.youtube.com/embed/TxCm8KSZKkw')


@app.route('/andina')
def andina():
    return render_template('region.html', title='Andina', imagen='../static/src/andina.png', video='https://www.youtube.com/embed/v7MWUfG1VPU')


@app.route('/caribe')
def caribe():
    return render_template('region.html', title='Caribe', imagen='../static/src/caribe.png', video='https://www.youtube.com/embed/DonE1EtkM6M')


@app.route('/orinoquia')
def orinoquia():
    return render_template('region.html', title='Orinoquía', imagen='../static/src/orinoquia.png', video='https://www.youtube.com/embed/l6NPEJlJfSs')


@app.route('/pacifico')
def pacifico():
    return render_template('region.html', title='Pacífico', imagen='../static/src/pacifico.png', video='https://www.youtube.com/embed/Ek7NHfJc4-k')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=81)
