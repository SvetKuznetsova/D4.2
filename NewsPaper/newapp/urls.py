from django.urls import path
from .views import PostList, PostDetail, News, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'newapp'
urlpatterns = [
    path('', PostList.as_view()), # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', PostDetail.as_view(), name='new_detail'),  # pk — это первичный ключ
    path('search/', News.as_view()),  # Не забываем добавить эндпойнт для нового класса-представления.
    path('new/create/', PostCreateView.as_view(), name='new_create'), # Ссылка на создание товара
    path('new/update/<int:pk>/', PostUpdateView.as_view(), name='new_update'), # Ссылка на редактирование товара
    path('new/delete/<int:pk>/', PostDeleteView.as_view(), name='new_delete'), # Ссылка на удаеление товара
]