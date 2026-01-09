import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Create dummy data
# Features: social_energy (0-10), talkativeness (0-10), likes_party (0-1), books_read (0-50)
# Target: 'Introvert' or 'Extrovert'

data = {
    'social_energy': [],
    'talkativeness': [],
    'likes_party': [],
    'books_read': [],
    'personality': []
}

for _ in range(1000):
    se = np.random.randint(0, 11)
    talk = np.random.randint(0, 11)
    party = np.random.randint(0, 2)
    books = np.random.randint(0, 51)
    
    # Simple logic for ground truth
    score = se + talk + (party * 5) - (books * 0.2)
    if score > 12:
        p = 'Extrovert'
    else:
        p = 'Introvert'
        
    data['social_energy'].append(se)
    data['talkativeness'].append(talk)
    data['likes_party'].append(party)
    data['books_read'].append(books)
    data['personality'].append(p)

df = pd.DataFrame(data)

# Train model
X = df[['social_energy', 'talkativeness', 'likes_party', 'books_read']]
y = df['personality']

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Save model
os.makedirs('ml_model', exist_ok=True)
joblib.dump(clf, 'ml_model/model.pkl')
print("Model trained and saved to ml_model/model.pkl")
