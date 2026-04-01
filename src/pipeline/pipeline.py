from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

def create_pipeline():
    return Pipeline([
        ('scaler', StandardScaler()),
        ('model', LinearRegression())
    ])