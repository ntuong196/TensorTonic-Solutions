import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    X = np.asarray(X)
    y = np.asarray(y)

    # Normal equation: w = (X^T X)^(-1) X^T y
    w = np.linalg.inv(X.T @ X) @ (X.T @ y)
    
    return w
    pass