import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    area = 0.0
    for i in range(1, len(fpr)):
        width = fpr[i] - fpr[i - 1]
        height = (tpr[i] + tpr[i - 1]) / 2.0
        area += width * height
    return area