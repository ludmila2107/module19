from django.shortcuts import render, redirect

from django.shortcuts import render
from task1.forms import UserRegister

from .models import Buyer, Game, News
from django.core.paginator import Paginator

# Create your views here.
def platform_view(request):
    return render(request, 'fouth_task/menu.html')

def news(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 10)  # Показываем 10 новостей на странице

    page_number = request.GET.get('page')
    news_page = paginator.get_page(page_number)

    return render(request, 'fifth_task/news.html', {'news': news_page})


def shop_view(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'fouth_task/shop.html', context)


def cart_view(request):
    return render(request, 'fouth_task/cart.html')


def process_registration(request):
    # Пустой словарь для информации
    info = {}

    form = UserRegister(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            repeat_password = form.cleaned_data.get('repeat_password')
            age = form.cleaned_data.get('age')
            balance = form.cleaned_data.get('balance')

            if Buyer.objects.filter(name=username).exists():
                info['error'] = "Пользователь с таким именем уже существует."
            elif password != repeat_password:
                info['error'] = "Пароли не совпадают."
            else:
                # Создание нового пользователя в таблице Buyer
                Buyer.objects.create(name=username, balance=balance, age=age)
                info['success'] = "Вы успешно зарегистрированы!"
                # return redirect('login')
                return render(request, 'fifth_task/registration_page.html', {'form': UserRegister(), 'info': info})
    return render(request, 'fifth_task/registration_page.html', {'form': form, 'info': info})


def sign_up_by_django(request):
    return process_registration(request)


def sign_up_by_html(request):
    return process_registration(request)

