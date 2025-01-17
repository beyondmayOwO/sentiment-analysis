import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result1['Label'], 'positive')

        result2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result2['Label'], 'negative')

        result3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result3['Label'], 'neutral')

unittest.main()