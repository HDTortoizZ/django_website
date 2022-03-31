from django.forms import ModelForm
from uploads.models import UploadModel


class UploadForm(ModelForm):

    class Meta:
        model = UploadModel
        fields = ['file']
