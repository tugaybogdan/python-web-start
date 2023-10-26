from django.forms import ModelForm

from .models import BoardMessage

class BoardMessageForm(ModelForm):
    class Meta:
        model = BoardMessage
        fields = ('title', 'content', 'price', 'rubric')
        