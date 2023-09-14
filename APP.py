import flask
import numpy as np
from flask import Flask
from flask import render_template
from tensorflow import keras



app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])


def main():
    if flask.request.method == 'GET':
        return render_template('test.html')
    if flask.request.method == 'POST':
        value1 = float(flask.request.form['value1'])
        value2 = float(flask.request.form['value2'])
        value3 = float(flask.request.form['value3'])
        value4 = float(flask.request.form['value4'])
        value5 = float(flask.request.form['value5'])
        value6 = float(flask.request.form['value6'])
        value7 = float(flask.request.form['value7'])
        value8 = float(flask.request.form['value8'])
        value9 = float(flask.request.form['value9'])
        value10 = float(flask.request.form['value10'])
        value11 = float(flask.request.form['value11'])
        value12 = float(flask.request.form['value12'])
        data = np.array([value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12])
        print(data)
        model = keras.models.load_model('models')
        prediction = model.predict(data)
        print(prediction)



        val = float(flask.request.form['value1'])
        #val2 = float(flask.request.form['value2'])
        return render_template('test.html', result = prediction[0][0])

if __name__ == '__main__':
    app.run()




