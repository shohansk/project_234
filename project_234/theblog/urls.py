
from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from project_234.settings import MEDIA_ROOT ,MEDIA_URL
from .views import HomeView , ArticleDetailView ,AddPostView ,UpdatePostView ,DeletePostView,AddCategoryView ,CategoryView,LikeView,AddCommentView

urlpatterns = [
    
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-detail'),

    path('add_post/',AddPostView.as_view() , name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view() , name='update_post'),
    path('article/<int:pk>/remove',DeletePostView.as_view() , name='delete_post'),
    path('add_category/',AddCategoryView.as_view() , name='add_category'),
    path('category/<str:cats>/',CategoryView , name='category'),
    path('like/<int:pk>',LikeView ,name = 'like_post'),
    path('article/<int:pk>/comment/',AddCommentView.as_view(), name = 'add_comment'),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)