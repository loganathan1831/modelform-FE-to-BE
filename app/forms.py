from django import forms
from app.models import *



class ModelTopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


class ModelWebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'

class Model_Access(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'
