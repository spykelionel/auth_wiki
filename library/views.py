
from django.shortcuts import render,redirect
from . models import *
from . forms import CommentForm
# from account import forms

# Create your views here.




def libraries(request):
    all_libraries = Post.objects.all()
    return render(request, 'library_page.html', {'all_libraries' : all_libraries})



def library_detail(request, slug):
    library = Post.objects.get(slug=slug)
    if request.method == 'POST':
        cf = CommentForm(request.POST)
        if cf.is_valid():
          content = request.POST.get('content')
          comment = Comment.objects.create(library = library, user = request.user, content = content)
          comment.save()
          return redirect('library_detail', slug=library.slug)
    else:   
        cf = CommentForm()
    return render(request, 'library_detail.html', {'library' : library, 'comment_form':cf})