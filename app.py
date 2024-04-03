from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/model_comparison')
def model_comparison():
    # Sample data (replace with your actual data)
    models = ['KNN', 'Random Forest', 'Extra Trees']
    val_rmse = [404.63, 381.18, 349.14]
    test_rmse = [508.12, 435.15, 413.11]
    val_r2 = [0.70, 0.73, 0.77]
    test_r2 = [0.61, 0.72, 0.75]

    return render_template('model_comparison.html', models=models, val_rmse=val_rmse, test_rmse=test_rmse, val_r2=val_r2, test_r2=test_r2)

if __name__ == '__main__':
    app.run(debug=True)
