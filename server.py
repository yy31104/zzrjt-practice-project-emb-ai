"""Flask server for Sentiment Analysis web application."""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """Analyze sentiment for the given text passed as a query parameter."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = sentiment_analyzer(text_to_analyze)

    label = response["label"]
    score = response["score"]

    if label is None:
        return "Invalid input! Try again."

    sentiment = label.split("_")[1]
    return (
        f"The given text has been identified as {sentiment} "
        f"with a score of {score}."
    )


@app.route("/")
def render_index_page():
    """Render the home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
