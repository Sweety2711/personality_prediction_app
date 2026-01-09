from django import forms

class PredictionForm(forms.Form):
    social_energy = forms.IntegerField(
        label='Social Energy (0-10)', 
        min_value=0, 
        max_value=10,
        initial=5,
        widget=forms.NumberInput(attrs={
            'type': 'range', 
            'class': 'form-range custom-range', 
            'step': '1',
            'oninput': 'document.getElementById("se_val").innerText = this.value'
        })
    )
    talkativeness = forms.IntegerField(
        label='Talkativeness (0-10)', 
        min_value=0, 
        max_value=10,
        initial=5,
        widget=forms.NumberInput(attrs={
            'type': 'range', 
            'class': 'form-range custom-range', 
            'step': '1',
            'oninput': 'document.getElementById("talk_val").innerText = this.value'
        })
    )
    likes_party = forms.ChoiceField(
        label='Do you like parties?',
        choices=[(1, 'Yes 🥳'), (0, 'No 🏠')],
        widget=forms.Select(attrs={'class': 'form-select custom-select'})
    )
    books_read = forms.IntegerField(
        label='Books read per year', 
        min_value=0, 
        max_value=100,
        initial=10,
        widget=forms.NumberInput(attrs={'class': 'form-control custom-input', 'placeholder': 'e.g., 12'})
    )
