from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
filename = 'file_breastcancer.pkl'
model = pickle.load(open(filename, 'rb'))    # load the model
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])  # The user input is processed here
def predict():
    Bare_Nuclei = request.form['bare_nuclei']
    Uniformity_of_cell_shape = request.form['uniformity_cell_shape']
    Uniformity_of_cell_size = request.form['uniformity_cell_size']
    Bland_Chromatin = request.form['bland_chromatin']
    pred = model.predict(np.array([[Bare_Nuclei, Uniformity_of_cell_shape, Uniformity_of_cell_size, Bland_Chromatin ]]))
    #print(pred)
    return render_template('index.html', predict=str(pred))
if __name__ == '__main__':
    app.run(host="127.0.0.9",port=8080, debug=True)
