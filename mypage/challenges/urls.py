from django.urls import path

from . import views

urlpatterns = [
    # path("january", views.index),
    # path("febuary", views.index2)
    path("<int:months>", views.monthly_challanges_num),
    #path("<str:months>", views.monthly_challenges)
    path("<str:months>", views.monthly_challenges, name="month_challenge"),
    path("", views.index, name="index")
]
