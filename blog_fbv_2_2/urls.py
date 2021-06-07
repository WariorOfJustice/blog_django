from django.contrib import admin
from django.urls import path, include

from article.views import get_main_page_view
from profile_user.views import registration_view, user_page_view, get_all_users_view, add_subscriber_view, \
    delete_subscriber_view, get_subscriptions_posts_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_main_page_view, name='home'),
    path('post/', include('article.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', registration_view, name='registration'),
    path('user/<str:username>/', user_page_view, name='user_page'),
    path('all_users/', get_all_users_view, name='get_all_users'),
    path('add_subscriber/<str:username>/', add_subscriber_view, name='add_subscriber'),
    path('delete_subscriber/<str:username>/', delete_subscriber_view, name='delete_subscriber'),
    path('my_subscriptions/<int:user_id>/', get_subscriptions_posts_view, name='get_subscriptions')
]
