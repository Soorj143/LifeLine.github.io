from django.shortcuts import render,redirect
from .models import BlogModel

# Create your views here.


def home_view(request):

    blogs = BlogModel.objects.all()
    # print(blogs)
    context = {'blogs' : blogs} 

    return render(request , 'BlogApp/home.html' , context)



def addblog_view(request):

    if request.method == 'POST':
        title1 = request.POST['title']
        desc1 = request.POST['desc']
        # print(title)
        # print(desc)

        blogs = BlogModel(title = title1 , desc = desc1)
        blogs.save()
        return redirect('home')

    return render(request , 'BlogApp/addblog.html')



def deleteblog_view(request , id):

    # print('id is',id)
    record = BlogModel.objects.get(id = id)
    record.delete()

    return redirect('home')



def updateblog_view(request , id):

    # print('id is',id)
    record = BlogModel.objects.get(id = id)
    context = {'record' : record}

    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        # print(title)
        # print(desc)

        record.title = title
        record.desc = desc
        record.save()

        return redirect('home')

    return render(request , 'BlogApp/updateblog.html' , context)

