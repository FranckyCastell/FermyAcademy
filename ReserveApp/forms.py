from django import forms
import datetime
from django.utils.timezone import now


# COURSES
COURSES = (
    ("1º ESO", "1º ESO"),
    ("2º ESO", "2º ESO"),
    ("3º ESO", "3º ESO"),
    ("4º ESO", "4º ESO"),
    ("1º Bachillerato", "1º Bachillerato"),
    ("2º Bachillerato", "2º Bachillerato"),
    ("Universidad / FP", "Universidad / FP"),
)


class Reserves(forms.Form):
    courses = forms.ChoiceField(choices=COURSES, label='Curso', required=True)

    date = forms.DateField(label='Data', initial=datetime.datetime.today,
                           widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=True)

    time = forms.DateField(label='Hora', initial='12:30',
                           widget=forms.DateInput(attrs={'type': 'time'}), required=True)

    observations = forms.CharField(label='Observaciones',
                                   required=True, widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))

    def __init__(self, *args, **kwargs):
        super(Reserves, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
