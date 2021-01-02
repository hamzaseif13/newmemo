from django.forms import ModelForm,Textarea,CharField
from .models import Day


class DayForm(ModelForm):
    class Meta():
        model=Day
        fields=('fajr','dohr','aser','maghrib','aisha')
        widgets = {
            'fajr': Textarea(attrs={'class':'prayer','placeholder':'! اكتب هنا '}),
            'dohr': Textarea(attrs={'class':'prayer','placeholder':'! اكتب هنا '}),
            'aser': Textarea(attrs={'class':'prayer','placeholder':'! اكتب هنا '}),
            'maghrib': Textarea(attrs={'class':'prayer','placeholder':'! اكتب هنا '}),
            'aisha': Textarea(attrs={'class':'prayer','placeholder':'! اكتب هنا '}),
        }
        