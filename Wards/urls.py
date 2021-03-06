from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'signup/', views.signup, name="signup"),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^$',views.home_index, name="homePage"),
    url(r'profile/(\d+)',views.profile_path, name='profile'),
    url(r'edit/',views.editprofile, name='edit'),
    url(r'^search/', views.search_project, name='search_results'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^review/(?P<pk>\d+)',views.add_review,name='review'),
    url(r'^all/(?P<pk>\d+)', views.all, name='all'),
    url(r'single/(\d+)',views.single,name ='single'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view())
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
