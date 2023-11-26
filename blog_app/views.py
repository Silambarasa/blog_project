from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . models import Post,Category
from .forms import PostForm
from django.urls import reverse_lazy
# Create your views here.


def CategoryListView(request):
   cat_menu_list = Category.objects.all()
   return render(request,'category_list.html',{'cat_menu_list':cat_menu_list})

# def CategoryView(request, cats):
#     category_posts = Post.objects.filter(category=cats.replace('-',' '))
#     return render(request,'categories.html',{'cats':cats.title().replace('-',' '), 'category_posts':category_posts})

class CategoryView(ListView):
    template_name = 'categories.html'
    context_object_name = 'category_posts'

    def get_queryset(self):
        return Post.objects.filter(category=self.kwargs['cats'].replace('-',' '))
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CategoryView, self).get_context_data(*args, **kwargs)   
        context["cat_menu"] = cat_menu
        return context
    


#listview puts puts more blogs(lists) on one page multiple
class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-id']
    #ordering = ['-post_date']


    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)   
        context["cat_menu"] = cat_menu
        return context
    

#deatilview puts one details on one page
class ArticleDetailView(DetailView):

    model = Post
    template_name = "article_details.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all() 
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    #fields = ('title','body')
    #fields = '__all__'


class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = "add_category.html"
    fields = '__all__'

class UPdatePostView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = "__all__"

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    fields = "__all__"
    success_url = reverse_lazy('home')
