from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load the trained model
model_path = os.path.join('Model', 'model.pkl')
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the form data
        data = request.form.to_dict()

        # Preprocess the input data
        # For example, convert form data to a pandas DataFrame
        input_data = pd.DataFrame(data, index=[0])

        # Make predictions using the model
        predictions = model.predict(input_data)

        # Pass the predictions to the result page
        return render_template('result.html', predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)
