from django.urls import path

from blog.views import AboutMeView

app_name = 'blog'

urlpatterns = [
    path('about-me/', AboutMeView.as_view(), name='about_me')
]
