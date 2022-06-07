from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import sklearn.metrics
# import dill

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def iris_prediction():
    if request.method == 'GET':
        return render_template('iris-prediction.html')
    elif request.method == 'POST':
        try:
            print('OK')
            print(dict(request.form))

            heart_features = dict(request.form).values()
            heart_features = np.array([float(x) for x in heart_features])

            print(heart_features)
            model = joblib.load('model/model.pkl')
            return 'OK'
            heart_features = std_scaler.transform([heart_features])
            print(heart_features)

            result = model.predict(heart_features)
            heart = {
                '0': 'Engga',
                '1': 'Iyaa',
            }
            result = heart[str(result[0])]
            return render_template('iris-prediction.html', result=result)

        except Exception as e:
            print(e)
            return e

        # iris_features = dict(request.form).values()
        # iris_features = np.array([float(x) for x in iris_features])
        # model, std_scaler = joblib.load('model-development/iris-classification-using-logistic-regression.pkl')
        # iris_features = std_scaler.transform([iris_features])
        # print(iris_features)
        # result = model.predict(iris_features)
        # iris = {
        #     '0': 'Iris Setosa',
        #     '1': 'Iris Versicolor',
        #     '2': 'Iris Virginica'
        # }
        # result = iris[str(result[0])]
        # return render_template('iris-prediction.html', result=result)
    else:
        return 'Unsupported Request Method'


if __name__ == '__main__':
    app.run(port=5000, debug=True)