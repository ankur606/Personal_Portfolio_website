from django.shortcuts import render
from django.views import View
from .models import *
from django.shortcuts import render


# from .utils import match_audio
# Create your views here.


class IndexPageView(View):
    def get(self, request):
        return render(request, 'index.html')
    
    
class AboutsPageView(View):
    def get(self, request):
        return render(request, 'about.html')    
    
    
class GalleryPageView(View):
    def get(self, request):
        return render(request, 'gallery.html')    
    
    
class AyushAboutsPageView(View):
    def get(self, request):
        return render(request, 'ayush-about-page.html')    

class AnshikaPhotosView(View):
    def get(self, request):
        return render (request, 'anshika_photos.html')        
       

class DeveloperAboutsPageView(View):
    def get(self, request):
        return render(request, 'developer-about.html')    
       
       
class BlogsPageView(View):
    def get(self, request):
        return render(request, 'blogs.html')    
                
       
class FirstBlogsDetails(View):
    def get(self, request):
        return render(request, 'blogs-details-page1.html')        
    
    
    
       
class SecondBlogsDetails(View):
    def get(self, request):
        return render(request, 'blogs-details-page2.html')        
    

       
class ThirdBlogsDetails(View):
    def get(self, request):
        return render(request, 'blogs-details-page3.html')                

class UserDetails(View):
    def get(self, request):
        data = AccountsUser.objects.all()
        for data in data :
            # print(data.id)
            data.username = "Ankur"
            data.save()
        dat = AccountsUser.objects.filter(id=60)   
        for f in dat:
            f.username = "Django"
            f.save()
        d = AccountsUser.objects.all()
        return render(request, 'show_user.html', {'data':d})                

class MenuItemsViews(View):
    def get(self, request):
        about = FoodCategories.objects.all()
        return render(request, 'menu.html', {'about':about})

