from django.shortcuts import render

# Create your views here. A view is a place to put the logic in the application

def post_list(request):
    return render(request,'blog/template/post_list.html',{})