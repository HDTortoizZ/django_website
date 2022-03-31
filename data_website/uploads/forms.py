from django import forms


class UploadForm(forms.Form):
    file = forms.FileField()

    def clean(self):
        cleaned_data = super().clean()
        file = cleaned_data.get('file')
        filename = file.name

        dot_count = 0
        for char in filename:
            if char == '.':
                dot_count = dot_count + 1
        if dot_count == 0:
            raise forms.ValidationError("This file has no extension.")
        if dot_count > 1:
            raise forms.ValidationError("You cannot have two extensions!")
        else:
            return cleaned_data
