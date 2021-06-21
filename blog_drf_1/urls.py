from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from article.views import CreateArticleView, ListArticleView, DetailArticleView, CreateCommentView, \
    ListFollowsArticlesView
from profile_user.views import RegistrationView, ProfileListView, ProfileDetailView, ProfileAddFollowView, \
    ProfileDestroyFollowView


urlpatterns = [
    path('admin/', admin.site.urls),
    # urls associated with Profile
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', RegistrationView.as_view(), name='auth_register'),
    path('all_users/', ProfileListView.as_view(), name='profiles_list'),
    path('profile/<int:id_profile>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('add_follow/<int:id_follow_profile>/', ProfileAddFollowView.as_view(), name='add_follow'),
    path('destroy_follow/<int:id_follow_profile>/', ProfileDestroyFollowView.as_view(), name='destroy_follow'),
    # urls associated with Article, Comment
    path('create_article/', CreateArticleView.as_view(), name='create_article'),
    path('all_articles/', ListArticleView.as_view(), name='all_articles'),
    path('article/<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    path('create_comment/', CreateCommentView.as_view(), name='create_comment'),
    path('follows_articles/', ListFollowsArticlesView.as_view(), name='get_follows_articles')
]
