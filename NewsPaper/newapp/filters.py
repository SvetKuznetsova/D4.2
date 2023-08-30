from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post, Category
import django_filters as filters
from django_filters import CharFilter

# создаём фильтр
class PostFilter(FilterSet):
    author = filters.CharFilter(label='Автор')
    title = filters.CharFilter(label='Заголовок')
    categoryType = filters.ModelChoiceFilter(label='Категория', queryset=Category.objects.all())

    class Meta:
        model = Post
      #  fields = ('author', 'categoryType', 'title', 'dateCreation')  # поля, которые мы будем фильтровать (т.е. отбирать по каким-то критериям, имена берутся из моделей)
        fields = {
            'author': ['exact'],
            'title': ['icontains'],
            'dateCreation': ['gt']
        }