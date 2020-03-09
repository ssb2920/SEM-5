from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post,Entry
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.core.paginator import Paginator
from .forms import EntryForm

@login_required
def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class UserPostListView(ListView):
    model = Post
    template_name='blog/home.html'
    context_object_name='posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostListView(ListView):
    model = Post
    template_name='blog/user_posts.html'
    context_object_name='posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post                # <app>/<model>_<viewtype>.html

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post  
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post  
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

# class UpdateEntryView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
#     model = Post  
#     fields = ['entries']

#     def form_valid(self,form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         else:
#             return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post 

    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False    

@login_required
def about(request):
    return render(request,'blog/about.html',{'title':'About'})


@login_required
def add_entry_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.post = post
            entry.author = request.user
            entry.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = EntryForm()
    return render(request, 'blog/entry_form.html', {'form': form})
