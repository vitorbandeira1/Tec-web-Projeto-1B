from django.forms import ModelForm
from django import forms
from .models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


        # title = forms.CharField()
        # content = forms.CharField()

    #     tag = forms.ModelMultipleChoiceField(
    #     queryset= title.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )
        widgets={
            'title': forms.TextInput(attrs={
                'class':'input',
                'placeholder': 'Título',


                 }),
            'content': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Conteúdo',
                }),
            'tag': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Tag',
                }),

        }