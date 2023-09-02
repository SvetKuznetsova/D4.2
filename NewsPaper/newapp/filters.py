from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post, Category
import django_filters as filters
from django_filters import CharFilter

# создаём фильтр
class PostFilter(FilterSet):
    author = filters.CharFilter(label='Автор', lookup_expr='exact')
    title = filters.CharFilter(label='Заголовок', lookup_expr='icontains')
    dateCreation = filters.DateFilter(label='Дата', lookup_expr='gt')

    class Meta:
        model = Post
        fields = ['author', 'title', 'dateCreation']  # поля, которые мы будем фильтровать (т.е. отбирать по каким-то критериям, имена берутся из моделей)
        #fields = {
      #      'author': ['exact'],
       #     'title': ['icontains'],
        #    'dateCreation': ['gt']
       # }