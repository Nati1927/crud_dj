from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name="index"),
    path('add/',views.add,name="add"),
    path("add_member",views.add_member,name="add_member"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/', views.update, name='update'),
    path('update/upp/<int:id>/', views.upp, name='upp'), 
]
