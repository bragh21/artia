from django import forms
from .widgets import FengyuanChenDatePickerInput


class ProjetoForm(forms.Form):
    nome = forms.CharField(max_length=255)
    data_inicio = forms.DateField(
        input_formats = ['%d/%m/%Y'],
        widget = FengyuanChenDatePickerInput
    )
    data_fim = forms.DateField(
        input_formats = ['%d/%m/%Y'],
        widget = FengyuanChenDatePickerInput()
    )

    def __init__(self, *args, **kwargs):
        super(ProjetoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'