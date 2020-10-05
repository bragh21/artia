from django import forms
from app_projeto.widgets import FengyuanChenDatePickerInput


class AtividadeForm(forms.Form):
    nome = forms.CharField(max_length=255)
    data_inicio = forms.DateField(
        input_formats = ['%d/%m/%Y'],
        widget = FengyuanChenDatePickerInput
    )
    data_fim = forms.DateField(
        input_formats = ['%d/%m/%Y'],
        widget = FengyuanChenDatePickerInput()
    )
    finalizada = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(AtividadeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != 'finalizada':
                visible.field.widget.attrs['class'] = 'form-control'