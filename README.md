# 💰 Salary Prediction Using Simple Linear Regression

## 📌 Project Overview

This project demonstrates the implementation of **Simple Linear Regression** using **Machine Learning with Python** to predict employee salaries based on their years of experience.

The objective of this project is to understand the complete Machine Learning lifecycle, including:

* Data Collection
* Data Preprocessing
* Model Training
* Model Evaluation
* Model Serialization using Pickle
* Flask Web Application Development
* Deployment to Render Cloud

The model is trained using a salary dataset containing:

| Feature             | Description              |
| ------------------- | ------------------------ |
| Years of Experience | Independent Variable (X) |
| Salary              | Dependent Variable (Y)   |

The dataset contains **30 records**, where:

* Training Data = 24 Records (80%)
* Testing Data = 6 Records (20%)

---

# 📊 Dataset Description

The dataset consists of:

| Years of Experience | Salary |
| ------------------- | ------ |
| 1.1                 | 39343  |
| 1.3                 | 46205  |
| 1.5                 | 37731  |
| ...                 | ...    |

The goal is to predict the salary of a person based on their years of experience.

---

# 🧠 Machine Learning Algorithm Used

## Simple Linear Regression

Simple Linear Regression is a supervised machine learning algorithm used to establish a relationship between:

* One Independent Variable (X)
* One Dependent Variable (Y)

In this project:

**X = Years of Experience**

**Y = Salary**

The algorithm learns the relationship between experience and salary and generates a mathematical equation.

---

# 📐 Linear Regression Formula

The Simple Linear Regression equation is:

[
Y = mX + c
]

Where:

* **Y** = Predicted Salary
* **X** = Years of Experience
* **m** = Slope of the Line
* **c** = Intercept

### Understanding the Formula

#### Slope (m)

Represents how much salary increases for every additional year of experience.

[
m = \frac{\sum (X-\bar X)(Y-\bar Y)}
{\sum (X-\bar X)^2}
]

#### Intercept (c)

Represents the starting salary when years of experience are zero.

[
c = \bar Y - m\bar X
]

The model automatically calculates these values during training.

---

# 🎯 Model Training

The dataset was divided into:

```python
train_size = 80%
test_size = 20%
```

Training Records:

```text
24 Rows
```

Testing Records:

```text
6 Rows
```

The model was trained using Scikit-Learn's Linear Regression algorithm.

Example:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)
```

---

# 📈 Model Performance

The trained model produced the following results:

| Metric                       | Value |
| ---------------------------- | ----- |
| Training Accuracy (R² Score) | 96%   |
| Testing Accuracy (R² Score)  | 90%   |
| Training Loss                | 115   |
| Testing Loss                 | 189   |

These results indicate that the model generalizes well and can accurately predict salaries for unseen data.

---

# 📊 R² Score (Coefficient of Determination)

R² Score measures how well the regression model explains the variance in the target variable.

## Formula

[
R^2 =
1 -
\frac{\sum(y_i-\hat y_i)^2}
{\sum(y_i-\bar y)^2}
]

Where:

* (y_i) = Actual Value
* (\hat y_i) = Predicted Value
* (\bar y) = Mean of Actual Values

---

## Interpretation

| R² Score  | Meaning            |
| --------- | ------------------ |
| 1.0       | Perfect Prediction |
| 0.9+      | Excellent Model    |
| 0.8+      | Good Model         |
| 0.5+      | Average Model      |
| Below 0.5 | Poor Model         |

### Our Results

```text
Training R² Score = 96%
Testing R² Score = 90%
```

This means the model explains most of the salary variation based on years of experience.

---

# 📉 Mean Squared Error (MSE)

MSE calculates the average squared difference between actual and predicted values.

## Formula

[
MSE =
\frac{1}{n}
\sum_{i=1}^{n}
(y_i-\hat y_i)^2
]

Where:

* (y_i) = Actual Value
* (\hat y_i) = Predicted Value
* n = Number of Samples

### Advantages

* Penalizes larger errors heavily.
* Widely used loss function for regression.

### Project Results

```text
Train Loss = 115
Test Loss = 189
```

Lower values indicate better model performance.

---

# 📉 Root Mean Squared Error (RMSE)

RMSE is the square root of MSE.

## Formula

[
RMSE = \sqrt{MSE}
]

Expanded Formula:

[
RMSE =
\sqrt{
\frac{1}{n}
\sum_{i=1}^{n}
(y_i-\hat y_i)^2
}
]

### Advantages

* Easier to interpret than MSE.
* Measured in the same unit as the target variable.

A lower RMSE indicates higher prediction accuracy.

---

# 💾 Saving the Model Using Pickle

After training the model, it was serialized using Python Pickle.

Example:

```python
import pickle

pickle.dump(model,
open("salary_prediction.pkl","wb"))
```

This creates a file:

```text
salary_prediction.pkl
```

which stores the trained machine learning model.

---

# 🚀 Flask Web Application

To make the model accessible through a web interface, a Flask application was developed.

## app.py

The Flask application performs the following tasks:

### 1. Load the Trained Model

```python
pickle.load()
```

### 2. Accept User Input

User enters:

```text
Years of Experience
```

### 3. Send Input to Model

```python
model.predict()
```

### 4. Generate Salary Prediction

The model predicts the salary.

### 5. Display Result

The predicted salary is displayed back on the webpage.

---

## Application Flow

```text
User Input
      ↓
HTML Form
      ↓
Flask Backend
      ↓
Pickle Model
      ↓
Prediction
      ↓
Display Result
```

---

# 🌐 Frontend (HTML)

The frontend is developed using HTML.

### Responsibilities

* Collect years of experience from users.
* Submit data to Flask backend.
* Display predicted salary.

Example UI:

```text
Enter Years of Experience
[________]

[Predict Salary]

Predicted Salary: ₹XXXXX
```

### Benefits

* Lightweight
* Fast Loading
* Easy to Maintain
* User Friendly

---

# 📦 requirements.txt

The `requirements.txt` file contains all Python dependencies required to run the project.

Example:

```txt
Flask
numpy
pandas
scikit-learn
gunicorn
```

---

## Advantages of requirements.txt

### Reproducibility

Anyone can recreate the same environment.

### Easy Installation

```bash
pip install -r requirements.txt
```

### Version Control

Maintains consistent package versions.

### Deployment Friendly

Cloud platforms such as:

* Render
* Heroku
* Railway
* AWS

automatically install dependencies using this file.

---

# ⚙️ gunicorn Configuration

Gunicorn is a production-grade WSGI server used for deploying Flask applications.

Example Start Command:

```bash
gunicorn app:app
```

---

## Advantages of Gunicorn

### Production Ready

Handles multiple requests efficiently.

### Better Performance

Faster and more scalable than Flask's development server.

### Reliable Deployment

Used in production environments.

### Render Compatibility

Render Cloud uses Gunicorn to serve Flask applications efficiently.

---

# ☁️ Deployment on Render

The application is deployed on Render Cloud.

Deployment Steps:

### Step 1

Push project to GitHub.

### Step 2

Create a new Web Service in Render.

### Step 3

Connect GitHub Repository.

### Step 4

Set Build Command

```bash
pip install -r requirements.txt
```

### Step 5

Set Start Command

```bash
gunicorn app:app
```

### Step 6

Deploy Application

Render automatically builds and hosts the application.

---

# 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Scikit-Learn
* Pickle
* Flask
* HTML
* Gunicorn
* Render Cloud

---

# 📂 Project Structure

```text
Salary-Prediction-Project/
│
├── app.py
├── SLR_MODEL.pkl
├── requirements.txt
├── templates/
│   └── index.html
│
│
├── notebook/
│   └── salary_prediction.ipynb
│
└── README.md
```

---

# 🎯 Future Enhancements

* Improved User Interface
* CSS Styling
* Bootstrap Integration
* Docker Containerization
* CI/CD Pipeline
* Cloud Monitoring
* Model Versioning

---

# 👨‍💻 Author

**Sai Kamal**

Founder & Managing Director
Vihara Tech Education Organization

📧 Email: [saikamal9797@gmail.com](mailto:saikamal9797@gmail.com)

🔗 LinkedIn: https://www.linkedin.com/in/saikamal9797

---

# ⭐ Conclusion

This project demonstrates a complete end-to-end Machine Learning workflow using Simple Linear Regression. The model successfully predicts employee salaries based on years of experience, achieves strong training and testing performance, and is deployed as a web application using Flask and Render Cloud.

The project serves as an excellent beginner-to-intermediate level example of integrating Machine Learning, Model Serialization, Web Development, and Cloud Deployment into a single production-ready application.
