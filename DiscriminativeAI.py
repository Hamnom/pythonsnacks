from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
'''
First run these on your terminal
pip install numpy
pip install scipy
then 
pip install scikit-learn
'''



# Sample data
texts = ["Win a free ticket now", "Hi, how are you?", "Limited time offer", "Let's meet tomorrow"]
labels = [1, 0, 1, 0]  # 1 = spam, 0 = not spam

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train classifier
model = MultinomialNB()
model.fit(X, labels)

# Predict new text
new_text = ["Win a free offer now!"]
X_new = vectorizer.transform(new_text)
prediction = model.predict(X_new)

print("Spam" if prediction[0] == 1 else "Not Spam")