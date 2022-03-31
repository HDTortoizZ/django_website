from django.shortcuts import render
from django.views.generic import TemplateView
from libraries.handlers.uploads import handle_uploaded_file
from uploads.forms import UploadForm


class UploadView(TemplateView):
    def get(self, request):
        form = UploadForm()
        return render(request, 'uploads/upload.html', {'form': form})

    def post(self, request):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'uploads/upload.html', {'form': UploadForm()})

        return render(request, 'uploads/upload.html', {'form': form})
