from django.shortcuts import render
from .forms import PredictionForm
from .models import PredictionResult
import joblib
import pandas as pd
import os
from django.conf import settings

MODEL_PATH = os.path.join(settings.BASE_DIR, 'ml_model', 'model.pkl')

def home(request):
    form = PredictionForm()
    return render(request, 'personality/home.html', {'form': form})

def predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Extract data
            social_energy = form.cleaned_data['social_energy']
            talkativeness = form.cleaned_data['talkativeness']
            likes_party = int(form.cleaned_data['likes_party'])
            books_read = form.cleaned_data['books_read']
            
            # Prepare for model
            input_data = pd.DataFrame([{
                'social_energy': social_energy,
                'talkativeness': talkativeness,
                'likes_party': likes_party,
                'books_read': books_read
            }])
            
            # Load model and predict
            try:
                model = joblib.load(MODEL_PATH)
                prediction = model.predict(input_data)[0]
                proba = model.predict_proba(input_data)[0]
                confidence = max(proba) * 100
                
                # Save to History
                PredictionResult.objects.create(
                    social_energy=social_energy,
                    talkativeness=talkativeness,
                    likes_party=likes_party,
                    books_read=books_read,
                    prediction=prediction,
                    probability=confidence
                )
                
                # Fetch recent history
                history = PredictionResult.objects.order_by('-created_at')[:5]

                context = {
                    'prediction': prediction,
                    'confidence': f"{confidence:.1f}",
                    'data': {
                        'social_energy': social_energy,
                        'talkativeness': talkativeness,
                        'likes_party': 'Yes' if likes_party == 1 else 'No',
                        'books_read': books_read
                    },
                    'history': history
                }
                return render(request, 'personality/result.html', context)
            except Exception as e:
                return render(request, 'personality/home.html', {
                    'form': form, 
                    'error': f"Error loading model: {str(e)}"
                })
    
    return home(request)
