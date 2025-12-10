from django.shortcuts import render # type: ignore
from django.views.generic import CreateView , UpdateView ,ListView ,TemplateView ,DeleteView  # type: ignore
from App_Blog.models import Blog , Comment , Likes
from django.urls import reverse , reverse_lazy # type: ignore
from django.contrib.auth.decorators import login_required   # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin   # type: ignore
from django.http import HttpResponseRedirect # type: ignore
from App_Blog.forms import CommentForm
from django.utils.text import slugify
import uuid
from django.utils.text import slugify



# Create your views here.
# def blog_list(request) :
#     return render(request , 'App_blog/blog_list.html' , context= {})


class MyBlogs(LoginRequiredMixin , TemplateView ) :
    template_name = 'App_Blog/my_blogs.html'

class UpdateBlog(LoginRequiredMixin,UpdateView) :
    model = Blog
    fields = ('blog_title' , 'blog_content' , 'blog_image')
    template_name = 'App_Blog/edit_blog.html'

    def get_success_url(self,**kwargs):
        # Change this line:
        return reverse_lazy('App_Blog:blog_details', kwargs={'slug':self.object.slug})
        #                          ↑ Use colon, not slash!

class BlogList(ListView) :
    model=Blog
    template_name = 'App_Blog/blog_list.html'
    context_object_name = 'blogs'
    # queryset = Blog.objects.order_by('-publish_date')  in models add in meta class i.e. ordering = ['-publish_date']

class CreateBlog(LoginRequiredMixin, CreateView) :
    model = Blog
    template_name = "App_Blog/create_blog.html"
    fields = ('blog_title' , 'blog_content' ,'blog_image')

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        base_slug = slugify(blog_obj.blog_title)
        blog_obj.slug = f"{base_slug}-{uuid.uuid4()}"
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

def blog_details(request, slug) :
    blog= Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    already_liked = Likes.objects.filter( blog=blog , user = request.user  )
    if already_liked :
        liked=True
    else :
        liked=False

    if request.method=="POST" :
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) 
            comment.user = request.user
            comment.blog = blog
            comment.save() 
            return HttpResponseRedirect(reverse('App_Blog:blog_details',kwargs={'slug': slug}))

    return render(request , 'App_Blog/blog_details.html' , context={'blog':blog , 'comment_form':comment_form , 'liked':liked})


@login_required
def liked(request , pk ):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog , user = user)
    if not already_liked :
        liked_post = Likes(blog=blog,user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('App_Blog:blog_details',kwargs={'slug': blog.slug}))

@login_required
def unliked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    like_obj = Likes.objects.filter(blog=blog, user=user).first()
    if like_obj:
        like_obj.delete()
    return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug': blog.slug}))
