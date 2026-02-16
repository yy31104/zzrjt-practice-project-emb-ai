```markdown
# NLP – Sentiment Analysis using BERT (Flask Web App)

This project is a simple **Flask web application** that performs **sentiment analysis** (POSITIVE / NEGATIVE / NEUTRAL) using the **Watson NLP BERT SentimentPredict** service.  
Users can input text in the browser, click a button, and view the sentiment label and confidence score.

---

## ✅ Features

- Web UI (HTML + JavaScript) for entering text and viewing results
- Flask backend endpoint: `/sentimentAnalyzer`
- Calls Watson NLP BERT SentimentPredict via HTTP POST (`requests`)
- Error handling for invalid/nonsense input (prevents server crash)
- Unit tests included (`unittest`)
- PEP8/static analysis using `pylint`

````

---

## ⚙️ Requirements

- Python 3.11
- Libraries:
  - `flask`
  - `requests`
  - `pylint` (optional, for static analysis)

If needed:

```bash
python3.11 -m pip install flask requests
````

---

## 🚀 Run the Web App

From the project root directory:

```bash
python3.11 server.py
```

Then open in your browser:

* [http://127.0.0.1:5000](http://127.0.0.1:5000)

(If you are using a Cloud IDE, open the provided preview URL.)

---

## 🌐 API Endpoint

### `GET /sentimentAnalyzer`

**Query parameter:**

* `textToAnalyze` (string)

Example:

```bash
curl "http://127.0.0.1:5000/sentimentAnalyzer?textToAnalyze=I%20love%20Python"
```

Expected response format:

* For valid input:

  * `The given text has been identified as POSITIVE with a score of 0.99...`
* For invalid input:

  * `Invalid input! Try again.`

---

## 🧪 Run Unit Tests

```bash
python3.11 test_sentiment_analysis.py
```

Expected output includes:

* `OK`

---

## ✅ Static Code Analysis (PEP8 / pylint)

Install pylint:

```bash
python3.11 -m pip install pylint
```

Run pylint on the Flask server:

```bash
pylint server.py
```

A score close to **10/10** indicates good code style compliance.

---

## 📝 Notes

* This project uses an external Watson NLP endpoint.
  If the service returns an error (e.g., HTTP 500), the app handles it gracefully and returns:
  **"Invalid input! Try again."**
* The Flask warning about “development server” is normal for local development.

---

```
```
