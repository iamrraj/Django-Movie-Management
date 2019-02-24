from django import forms
from tinymce import TinyMCE
from .models import Moviee

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class PostForm(forms.ModelForm):
    description = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    maincast= forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 15, 'rows': 10}
        )
    )

    class Meta:
        model = Moviee
        fields =('name','mdate','rating','murl','movietime','mtype','director','maincast','description','body','ytube')

    