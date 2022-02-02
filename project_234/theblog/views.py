

from django.shortcuts import render,get_list_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView,UpdateView ,DeleteView
from .forms import PostForm,EditForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

from .models import Category, Post,Comment

# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ('title','title_tag','body')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
   # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

def CategoryView(request,cats):
    category_post = Post.objects.filter(category = cats.replace('-',' '))
    return render(request, 'categories.html',{'cats': cats.title().replace('-',' ') ,'category_post':category_post})

     
def LikeView(request,pk):
    post = get_list_or_404(Post,id = request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args = [str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')

  
    #fields = '__all__'