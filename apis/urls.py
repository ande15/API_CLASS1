from django.urls import path
from .views import BookApisView

urlpatterns = [
    path("", BookApisView.as_view(), name="book_list"),
]