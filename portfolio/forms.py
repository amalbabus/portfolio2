from django.forms import ModelForm
from portfolio.models import MessageModel

class NewMessages(ModelForm):
    class Meta:
        model = MessageModel

        fields = '__all__'