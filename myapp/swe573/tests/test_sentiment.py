import personal.backends.analyse.sentiment_analysis as se
import pytest

@pytest.mark.django_db
class TestSentiment:

    def test_sentiment(self):
        response = se.sentiment("happy")
        assert response is not None