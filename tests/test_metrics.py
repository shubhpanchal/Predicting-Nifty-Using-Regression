from metrics import compute_accuracy

def test_compute_accuracy():
    predicted = [1, -1, 1, 0]
    actual = [1, 1, 1, 0]
    assert compute_accuracy(predicted, actual) == 75.0
