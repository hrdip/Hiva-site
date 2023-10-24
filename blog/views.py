from django.shortcuts import render

def blog_view (request):
    return render(request,'blog/blog_home.html')

def blog_single (request):
    return render(request,'blog/blog_single.html')
 
