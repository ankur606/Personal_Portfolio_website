from django import views
from django.urls import path
from .views import*

urlpatterns = [
    
    path('', IndexPageView.as_view(), name="indexpage"),
    path('about/', AboutsPageView.as_view(), name="aboutPage"),
    path('ayush-abouts-page/', AyushAboutsPageView.as_view(), name="ayushaboutPage"),
    path('developer-abouts-page/', DeveloperAboutsPageView.as_view(), name="developeraboutPage"),
    path('anurag-blogs-page/', BlogsPageView.as_view(), name="blogsPage"),
    path('anurag-first-blogs-details-page/', FirstBlogsDetails.as_view(), name="firstblogsPage"),
    path('anurag-second-blogs-details-page/', SecondBlogsDetails.as_view(), name="secondblogsPage"),
    path('anurag-third-blogs-details-page/', ThirdBlogsDetails.as_view(), name="thirdblogsPage"),
    path("user-details", UserDetails.as_view(), name="userDetails"),
    path('menu-items', MenuItemsViews.as_view(), name="Menu"),


    
]