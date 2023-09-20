from django.urls import path
from . import views
from .views import MyLoginView
from .views import PostCreate,PostUpdate,PostDelete,PostList,RegisterView
from my_project.settings import DEBUG,STATIC_URL,STATIC_ROOT,MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.index , name='index'),
    path('post_list/',PostList.as_view(),name='post_list'),
    path('post_create/' , PostCreate.as_view(), name= 'post_create'),
	path('post_update/<slug:pk>/' , PostUpdate.as_view(), name= 'post_update'),
	path('post_delete/<slug:pk>/' , PostDelete.as_view(), name= 'post_delete'),
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', MyLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
]
if DEBUG:
   urlpatterns+= static(STATIC_URL,document_root=STATIC_ROOT)
   urlpatterns+= static(MEDIA_URL,document_root=MEDIA_ROOT)
