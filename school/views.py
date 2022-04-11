from django import forms
from django import views
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import ContactFrom
# Create your views here.

# function based views
def myview(request):
    # return HttpResponse('<h1>function based views</h1>')
    return render(request, 'school/home.html')

def about(request):
    context = {'msg':'Welcome to the Rakesh Gain\'s function based About page.'}
    return render(request,'school/about.html',context)

# Class based views
class MyView(View): 
    name = 'sonam'
    def get(self, request):
        # return HttpResponse('<h1>Class based views-GET</h1>')
        # return HttpResponse(self.name)
        return render(request, 'school/home.html')

class MyChildView(MyView):
    def get(self, request):
        return HttpResponse(self.name)

class MyAbout(View):
    def get(self, request):
        context = {'msg':'Welcome to the Rakesh Gain\'s Class about view. '}
        return render(request, 'school/about.html',context)

##################################################################################

def contactform(request):
    if request.method == "POST":
        form = ContactFrom(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You Form Submitted successfully...!')

    else:
        form = ContactFrom()
    return render(request, 'school/contact.html',{'form':form})    

class MyContact(View):
    def get(self, request):
        form = ContactFrom()
        return render(request, 'school/contact.html' ,{'form':form})

    def post(self, request):
        if request.method == "POST":
            form = ContactFrom(request.POST)
            if form.is_valid():
                print(form.cleaned_data['name'])
                return HttpResponse('Thank You form Submitted Successfully...!')

####################################################################        

def news(request,template_name):
    template_name = template_name
    context = {'info':'Some context information were given here.'}
    return render(request,template_name,context)

class NewsClassView(View):
    template_name = ''
    def get(self, request):
        context = {'info':'Add anything here in Newsclassview'}
        return render(request,self.template_name,context)
