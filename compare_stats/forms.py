from django import forms
from compare_stats.models import State, Galapagos

class ChooseState(forms.Form):
    choice = forms.ModelChoiceField(queryset=State.objects.all())