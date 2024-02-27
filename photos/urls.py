from django.urls import path
from . import views
from documents import views as vi
urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path("document_list/",vi.document_list,name="document_list"),
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('displayall/', views.displayall, name='displayall'),
    path('add/', views.addPhoto, name='add'),
    path('delete/<str:pk>/', views.deletePhoto, name='delete'),
    path('download/<str:pk>/', views.downloadPhoto, name='download'),
    path('about/', views.about, name='about'),
]
