import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("fake_news_dataset.csv")

# 🧹 CLEAN LABELS PROPERLY
data["label"] = data["label"].astype(str).str.strip().str.lower()

# Convert labels safely
data = data[data["label"].isin(["fake", "real"])]  # remove invalid rows
data["label"] = data["label"].map({"fake": 0, "real": 1})

# 🧹 HANDLE TEXT
data["title"] = data["title"].fillna("")

# Use title (or combine if text exists)
if "text" in data.columns:
    data["text"] = data["text"].fillna("")
    X = data["title"] + " " + data["text"]
else:
    X = data["title"]

y = data["label"]

# 🔍 DEBUG (optional)
print("Label counts:\n", y.value_counts())

# 🎯 VECTORIZER
vectorizer = TfidfVectorizer(
    stop_words='english',
    max_df=0.7,
    min_df=3,
    ngram_range=(1,2)
)

X_vec = vectorizer.fit_transform(X)

# 🤖 MODEL
model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)

# 🔮 PREDICT FUNCTION
def predict_news(news):
    vec = vectorizer.transform([news])
    prob = model.predict_proba(vec)[0]
    result = model.predict(vec)[0]
    
    confidence = max(prob) * 100

    if result == 1:
        return f"REAL ✅ (Confidence: {confidence:.2f}%)"
    else:
        return f"FAKE ❌ (Confidence: {confidence:.2f}%)"