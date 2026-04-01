from sklearn.metrics import mean_squared_error

def evaluate(y_true, y_pred):
    return mean_squared_error(y_true, y_pred)