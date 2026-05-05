from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "data science is fun",
    "data mining is fun",
    "machine learning is cool"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

cos_sim = cosine_similarity(X)

print("\n=== NOMOR 3 ===")
print("Cosine Similarity Matrix:")
print(cos_sim)

print("\nD1-D2 :", cos_sim[0][1])
print("D1-D3 :", cos_sim[0][2])
