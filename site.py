from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    context = {'title': 'Main'}
    return render_template('index.html', **context)


@app.route('/barbells/')
def barbells():
    context = {'title': 'Barbells'}
    return render_template('barbells.html', **context)


@app.route('/weights/')
def weights():
    context = {'title': 'Weights'}
    return render_template('weights.html', **context)

@app.route('/dumbbells/')
def dumbbells():
    context = {'title': 'Dumbbels'}
    return render_template('dumbbells.html', **context)



if __name__ == '__main__':
    app.run()

