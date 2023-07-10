from flask import Flask,render_template,jsonify,request
from src.piplines.prediction_pipline import CustomData, PredictPipeline


application = Flask(__name__)


@application.route('/')
def home_page():
    return render_template('index.html')

@application.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data = CustomData(
            carat = float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
        )

        pred_df = data.get_data_as_dataframe()
        
        # print(pred_df)

        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(pred_df)
        results = round(pred[0],2)
        return render_template('index.html',results=results,pred_df = pred_df)
    



if __name__ == '__main__':
    application.run(host="0.0.0.0", debug=True)