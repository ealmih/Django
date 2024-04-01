from django.shortcuts import render
from django.http import HttpResponse

items = [
   {"id": 1, "name": "Кроссовки abibas"},
   {"id": 2, "name": "Куртка кожаная"},
   {"id": 3, "name": "Coca-cola 1 литр"},
   {"id": 4, "name": "Картофель фри"},
   {"id": 5, "name": "Кепка"},
]


# Create your views here.
def home(requst):
    text = """<h1>"Изучаем django"</h1>
<strong>Автор</strong>: <i>Иванов И.П.</i>
<p><a href="http://127.0.0.1:8000/about/">обо мне</a></p>
<p><a href="http://127.0.0.1:8000/items/">к списку товаров</a></p>"""
    return HttpResponse(text)

def about(requst):
    text = """Имя: Иван
Отчество: Петрович
Фамилия: Иванов
телефон: 8-923-600-01-02
email: vasya@mail.ru"""
    return HttpResponse(text)

def item(request, id):
    if 0<id<=len(items):
        text = f"""<p>{items[id-1]['name']}</p>
        <p><a href="http://127.0.0.1:8000/items/">назад к списку товаров</a></p>"""
    else:
        text = f"""<p>Товар с id={id} не найден</p>
        <p><a href="http://127.0.0.1:8000/items/">назад к списку товаров</a></p>"""
    return HttpResponse(text)

def allitems(request):
    text = ""
    for i in range(len(items)):
        text += f"""<p><a href="http://127.0.0.1:8000/item/{i+1}/"{i+1}. {items[i]['name']}</a></p>"""
        text += f"<h1>{i+1}. {items[i]['name']}</h1>"
    return HttpResponse(text)