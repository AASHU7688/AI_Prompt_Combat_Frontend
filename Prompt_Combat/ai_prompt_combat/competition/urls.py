from django.urls import path
from .views import home, signup, login_view, compition_page, leaderboard,rules,level1,level2,contact

urlpatterns = [
    path('', home, name='home'),  # Home Page
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    # path('logout/', user_logout, name='logout'),
    path('compition_page/', compition_page, name='compition_page'),  # Submit Form (Level 1 & Level 2)
    path('contact/', contact, name='contact'),
    path('leaderboard/', leaderboard, name='leaderboard'),  # Leaderboard Page
     path('rules/', rules, name='rules'),
     path('level1/', level1, name='level1'),
    path('level2/', level2, name='level2'),
]