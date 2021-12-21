from django.urls import path

from .import views

urlpatterns =[
    path('',views.PlannerView,name='planners'),
    path('plandetail/<int:pk>/', views.PlanDetail),
]