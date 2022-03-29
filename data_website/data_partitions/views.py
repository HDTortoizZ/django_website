from django.shortcuts import render
from django.views.generic import TemplateView


class CreatePartitionsView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render('data_partitions/partition', request)
