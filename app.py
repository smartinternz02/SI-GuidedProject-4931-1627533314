

from flask import Flask, request, render_template
from joblib import load

column = load('onehot.save')
model = load('model.save')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict', methods=['POST'])
def y_predict():
    x_test = [[x for x in request.form.values()]]
    print(x_test)
    
    x_test = column.transform(x_test)
    print(x_test)
    
    pred = model.predict(x_test)
    output = pred[0]
    print('Price predicted', output)
    
    return render_template('index1.html', prediction_text = 'Price (In INR): {}'.format(output))
    
if (__name__ == '__main__'):
    app.run(debug=True)