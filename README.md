# Medical Cost Prediction

A machine learning project that predicts medical insurance charges based on patient information.

## Dataset
- Source: Kaggle - Medical Cost Personal Dataset
- 1338 records, 7 features (age, sex, bmi, children, smoker, region, charges)

## Models Used
- Linear Regression
- Ridge Regression
- Lasso Regression

## Results
| Model | MAE | R2 Score |
|-------|-----|----------|
| Linear Regression | $4,181 | 0.7836 |
| Ridge | $4,193 | 0.7833 |
| Lasso | $4,182 | 0.7835 |

## Key Finding
Smoking is the most significant factor affecting medical charges.

## How to Run
```bash
streamlit run app.py
```

## Tech Stack
Python, Pandas, Scikit-learn, Matplotlib, Seaborn, Streamlit