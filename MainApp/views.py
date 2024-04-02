from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound

# items = [
#    {"id": 1, "name": "Кроссовки abibas"},
#    {"id": 2, "name": "Куртка кожаная"},
#    {"id": 3, "name": "Coca-cola 1 литр"},
#    {"id": 4, "name": "Картофель фри"},
#    {"id": 5, "name": "Кепка"},
# ]

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 4, "name": "Картофель фри" ,"quantity":0},
   {"id": 5, "name": "Кепка" ,"quantity":124},
]



# Create your views here.
def home(request):
    context = {
        "name" : "Ivan Petrov",
        "email" : "ma@mail.ru"
    }
    return render(request, "index.html", context)
    #return render(request, "index.html")
#     text = """<h1>"Изучаем django"</h1>
# <strong>Автор</strong>: <i>Иванов И.П.</i>
# <p><a href="/about">обо мне</a></p>
# <p><a href="/items">к списку товаров</a></p>"""
#     return HttpResponse(text)


def about(requst):
    text = """Имя: Иван
Отчество: Петрович
Фамилия: Иванов
телефон: 8-923-600-01-02
email: vasya@mail.ru"""
    return HttpResponse(text)

# def item(request, id):
#     if 0<id<=len(items):
#         text = f"""<p>{items[id-1]['name']}</p>
#         <p><a href="/items">назад к списку товаров</a></p>"""
#     else:
#         text = f"""<p>Товар с id={id} не найден</p>
#         <p><a href="/items">назад к списку товаров</a></p>"""
#     return HttpResponse(text)

def get_item(request, id):
    for item in items:
        if item['id'] == id:
            # if item["quantity"] == 0:
            #     item["quantity"] = 'товар отсутствует'
            context = {
                'item': item
            }
            return render(request, "item-page.html", context)
    return HttpResponseNotFound(f'Item with id={id} not found')

def allitems(request):
    text = ""
    for i in range(len(items)):
        text += f"""<p><a href="/item/{i+1}/"{i+1}. {items[i]['name']}</a></p>"""
        text += f"<h1>{i+1}. {items[i]['name']}</h1>"
    return HttpResponse(text)

def allitems2(request):
    text = "<h2>Список товаров</h2><ol>"
    for item in items:
        text += f"<li><a href='/item/{item['id']}'>{item['name']}</li>"
    text += '</ol>'
    return HttpResponse(text)

def items_list(request):
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)