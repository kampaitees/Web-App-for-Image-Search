
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views 
urlpatterns = [

    path('',                views.home,               name = 'home'),
    path('home',            views.home,               name = 'home'),
    path('team',            views.team,               name = 'team'),
    path('about',           views.about,              name = 'about'),
    path('contact',         views.contact,            name = 'contact'),
    path('blog-home',       views.blogs,              name = 'blog-home'),
    path('elements',        views.element,            name = 'elements'),
    path('blog-single',     views.blog_single,        name = 'blog-single'),
    path('image-uploader',  views.search_image,       name = 'image-uploader'),
    path('clean_up_search', views.clean_up_search,    name = 'clean_up_search'),
    path('clean_up_database', views.clean_up_database,    name = 'clean_up_database'),
    path('upload-database', views.upload_to_database, name='upload-database'),
    path('res', views.res, name = 'res')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# path('search_image',views.search_image,name = 'search_image'),
# path('clean_up_database', views.clean_up_database, name = 'clean_up_database'),