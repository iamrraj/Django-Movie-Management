from django import forms
# from tinymce import TinyMCE
from .models import Moviee

# class TinyMCEWidget(TinyMCE):
#     def use_required_attribute(self, *args):
#         return False

class MovieForm(forms.ModelForm):
    # description = forms.CharField(
    #     widget=TinyMCEWidget(
    #         attrs={'required': False, 'cols': 30, 'rows': 10}
    #     )
    # )

    class Meta:
        model = Moviee
        fields = '__all__'

    class Media:
        js = ('/media/tinymce/jscripts/tiny_mce/tiny_mce.js',
                '',)