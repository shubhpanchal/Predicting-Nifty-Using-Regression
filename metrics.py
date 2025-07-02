
def compute_accuracy(predicted_signal, y_test):
    """Compute prediction accuracy percentage.

    Parameters
    ----------
    predicted_signal : array-like
        Predicted labels or signals.
    y_test : array-like
        True labels.

    Returns
    -------
    float
        Accuracy percentage rounded to two decimals.
    """
    predicted = list(predicted_signal)
    actual = list(y_test)
    if len(predicted) != len(actual):
        raise ValueError("predicted_signal and y_test must be the same length")

    correct = sum(p == a for p, a in zip(predicted, actual))
    accuracy_percentage = round(100 * correct / len(predicted), 2)
    return accuracy_percentage
