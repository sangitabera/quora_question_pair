from app.services.prediction_service import predict_duplicate

def test_prediction():

    pred, prob = predict_duplicate(
        "How to learn Python?",
        "What is the best way to learn Python?"
    )

    assert pred in [0, 1]
    assert 0 <= prob <= 1