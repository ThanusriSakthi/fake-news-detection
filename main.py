import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("fake_news_dataset.csv")

# Convert labels properly
data["label"] = data["label"].str.lower()
data["label"] = data["label"].map({"fake": 0, "real": 1})

# Fill missing values
data["title"] = data["title"].fillna("")

# (If text column exists, use it too)
if "text" in data.columns:
    data["text"] = data["text"].fillna("")
    X = data["title"] + " " + data["text"]
else:
    X = data["title"]

y = data["label"]

# Better vectorizer
vectorizer = TfidfVectorizer(
    stop_words='english',
    max_df=0.7,
    min_df=3,
    ngram_range=(1,2)
)

X_vec = vectorizer.fit_transform(X)

# Better model
model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)

# Prediction function
def predict_news(news):
    vec = vectorizer.transform([news])
    prob = model.predict_proba(vec)[0]
    result = model.predict(vec)[0]
    
    confidence = max(prob) * 100

    if result == 1:
        return f"REAL ✅ (Confidence: {confidence:.2f}%)"
    else:
        return f"FAKE ❌ (Confidence: {confidence:.2f}%)"