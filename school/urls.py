from unicodedata import name
from django.urls import path
from . import views



urlpatterns = [
    path('funv/',views.myview, name="myfunview"),
    path('aboutv/',views.about, name="myaboutv"),
    # path('clv/',views.MyView.as_view(), name="myclsview"),
    path('clv/',views.MyView.as_view(name='Rahul'), name="myclsview"),
    path('subclv/',views.MyView.as_view(), name="mysubclsview"),
    path('aboutclv/',views.MyAbout.as_view(), name="myaboutcl"),
    path('contfunv/',views.contactform, name="contfun"),
    path('contclv/',views.MyContact.as_view(), name="contclv"),
    path('news/',views.news, {'template_name':'school/news.html',}, name="news"),
    path('news2/',views.news, {'template_name':'school/news2.html'}, name="news2"),
    path('newsclv/',views.NewsClassView.as_view(template_name='school/news.html'),name="newsclv"),
    path('newsclv2/',views.NewsClassView.as_view(template_name='school/news2.html'),name="newsclv2"),
]
