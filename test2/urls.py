from django.urls import path
from .views import get_person, detail_person, create_person, deleat_person, update_person

urlpatterns = [
    path('all_people/', get_person),
    path('detail_person/<int:pk>/', detail_person),
    path('create_person/', create_person),
    path('deleat_person/<int:pk>/', deleat_person),
    path('update_person/<int:pk>/', update_person)
]
