from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('detailed_page/<int:post_id>/',views.detailed_page,name='detailed_page'),
    path('create/',views.create,name='create'),
    path('login/',views.Login,name='login'),
    path('register/',views.register,name='register'),
    path('categories/',views.categories,name='categories'),
    path('status_filter/',views.status_filter,name='status_filter'),
    path('logout/',views.Logout,name='logout'),
    path('update/<int:post_id>/',views.update,name='update'),
    path('detailed_page/<int:post_id>/delete/', views.delete, name='delete'),
 
]