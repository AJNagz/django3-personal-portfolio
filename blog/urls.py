from django.urls import path
from . import views

# Below code will only target detail.html belonging to blog app
# if we change the app_name to something else it breaks the blogs 
# it show namespace error
# app_name attribute in the included URLconf module
app_name = 'blog'

urlpatterns = [
    # below code will take the all_blogs to main blog site
    path('', views.all_blogs, name='all_blogs'),
    # to get the real path for the page use the below code
    # path('all_blogs', views.all_blogs, name='all_blogs'),
    # below path is for the blog posts
    # after this create a detail() function in blog/views.py
    # <int:blog_id> will grab the id from the url and send to detail()
    path('<int:blog_id>/', views.detail, name='detail'),
    
]