from django.http import HttpResponse, Http404
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Prop


def index(request):
    props = Prop.objects.all()
    return render(request, 'props/index.html', {'props': props})


def detail(request, prop_id):
    prop = get_object_or_404(Prop, pk=prop_id)
    return render(request, 'props/detail.html', {'prop': prop})


