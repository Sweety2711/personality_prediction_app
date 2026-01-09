from django.db import models

class PredictionResult(models.Model):
    social_energy = models.IntegerField()
    talkativeness = models.IntegerField()
    likes_party = models.IntegerField() # 0 or 1
    books_read = models.IntegerField()
    prediction = models.CharField(max_length=20) # 'Introvert' or 'Extrovert'
    probability = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prediction} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
