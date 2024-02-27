from django.urls import path
from . import views
from photos import views as vi
urlpatterns = [
    path('',vi.gallery,name="gallery"),
    path('document_list/',views.document_list,name='document_list'),
    path('document_view/<str:pk>/',views.document_view,name='document_view'),
    path('displayall/',views.displayall,name='displayall'),
    path('add_doc/',views.add_doc,name='add_doc'),
    path('download_document/<str:pk>/',views.downloadDocument,name='download_document'),
    path('delete_document/<str:pk>/',views.deleteDocument,name='delete_document'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerUser,name='register'),
    path("about/",views.about,name='about'),
]
