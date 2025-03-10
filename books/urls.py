from django.urls import path
from .views import CreateBooksAPIView


urlpatterns = [
    path('', CreateBooksAPIView.as_view(), name='create_books')
]
