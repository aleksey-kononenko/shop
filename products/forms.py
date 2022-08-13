from django import forms


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()
    csv_upload.label = 'Файл для загрузки'
    csv_upload.widget.attrs.update({
        'title': 'Выберите файл для загрузки',
        'class': 'form-control custom-file-upload',
    })
