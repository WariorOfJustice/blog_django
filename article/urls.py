from django.urls import path

from article.views import create_post_view, article_page_view, add_comment_view, change_post_view, delete_post_view


urlpatterns = [
    path('create/', create_post_view, name='create_post'),
    path('<int:article_id>/', article_page_view, name='article_page'),
    path('comment/add/<int:article_id>/', add_comment_view, name='add_comment'),
    path('change_post/<int:post_id>/', change_post_view, name='change_post'),
    path('delete_post/<int:post_id>/', delete_post_view, name='delete_post')
]
