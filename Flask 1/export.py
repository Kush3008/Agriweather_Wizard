import pandas as pd
import os
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load your data and preprocess it
data_directory = r'D:\Code Stuff\Agriweather Wizard\Data'

# Load your data
data1 = pd.read_csv(os.path.join(data_directory, 'Crop_Yield_Data_challenge_2.csv'))
data2 = pd.read_csv(os.path.join(data_directory, 'ndvi.csv'))
data3 = pd.read_csv(os.path.join(data_directory, 'Sentinel_1.csv'))
data4 = pd.read_csv(os.path.join(data_directory, 'Weather_Data.csv'))
data4 = data4.drop(['Lattitude', 'Longtitude', 'Season'], axis=1)
data = pd.concat([data1, data2, data3, data4], axis=1)

# One-hot encoding
data = pd.get_dummies(data, columns=['District'])
data = pd.get_dummies(data, columns=['Season(SA = Summer Autumn, WS = Winter Spring)'])
data = pd.get_dummies(data, columns=['Rice Crop Intensity(D=Double, T=Triple)'])

# Convert date to columns
data['Date of Harvest'] = pd.to_datetime(data['Date of Harvest'], format='%d-%m-%Y')
data['Year'] = data['Date of Harvest'].dt.year
data['Quarter'] = data['Date of Harvest'].dt.quarter
data['Month'] = data['Date of Harvest'].dt.month
data['Day of Year'] = data['Date of Harvest'].dt.dayofyear
data['Day of Month'] = data['Date of Harvest'].dt.day
data['Day of Week'] = data['Date of Harvest'].dt.dayofweek
data['Week of Year'] = data['Date of Harvest'].dt.isocalendar().week
data = data.drop(columns=['Date of Harvest'])

# Perform KNN Imputation
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=5)
df_imputed = imputer.fit_transform(data)
data = pd.DataFrame(df_imputed, columns=data.columns)

# Split the dataset into features and target variable
X = data.drop('Rice Yield (kg/ha)', axis=1)
y = data['Rice Yield (kg/ha)']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Extra Trees regression model
et_model = ExtraTreesRegressor()

# Fit the model to the training data
et_model.fit(X_train, y_train)

# Define the file path where you want to save the model
model_file_path = r'D:\Code Stuff\Agriweather Wizard\Model\model.pkl'

# Save the model using joblib.dump()
joblib.dump(et_model, model_file_path)

print("Model exported successfully!")
