from django.views.generic import ListView, \
    DetailView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Post
from datetime import datetime
from django.utils import timezone
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator # Импортируем класс, позволяющий удобно осуществлять постраничный вывод
from .filters import PostFilter # импортируем недавно написанный фильтр

class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'newapp/news.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    #queryset = Post.objects.order_by('-dateCreation')
    ordering = ['-dateCreation']  # сортировка по цене в порядке убывания
    paginate_by = 1  # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = timezone.localtime(timezone.now()) # добавим переменную текущей даты time_now
        context['value1'] = None # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'newapp/new.html'
    context_object_name = 'new'
    queryset = Post.objects.all()

class News(View):

    def get(self, request):
        news = Post.objects.order_by('-dateCreation')
        p = Paginator(news, 1)  # Создаём объект класса пагинатор, передаём ему список наших товаров и их количество для одной страницы
        news = p.get_page(
            request.GET.get('page', 1))  # Берём номер страницы из get-запроса. Если ничего не передали, будем показывать первую страницу
        # Теперь вместо всех объектов в списке товаров хранится только нужная нам страница с товарами

        data = {
            'news': news,
        }

        return render(request, 'newapp/search.html', data)


