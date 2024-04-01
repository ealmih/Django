from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(requst):
    text = """<h1>"Изучаем django"</h1>
<strong>Автор</strong>: <i>Иванов И.П.</i>"""
    return HttpResponse(text)
