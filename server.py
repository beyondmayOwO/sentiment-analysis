"""Flask server to grab the user input from the client side and return the score and label"""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    # Get the input that was sent as the query parameter from the client
    text_to_analyze = request.args.get('textToAnalyze')

    result = sentiment_analyzer(text_to_analyze)
    label = result['Label']
    score = result['Score']

    if label is None:
        return "Invalid input! Try again."
    else:
        return f"The given text has been identified as {label} with a score of {score}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
