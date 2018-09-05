from django.shortcuts import render, get_object_or_404,redirect
from blog.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.utils import timezone
from blog.forms import PostForm, CommitForm

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def query_set(self):
        return  Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = 'login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'login/'
    model = Post
    success_url = reverse_lazy('post_list')

class DraftPostList(LoginRequiredMixin, ListView):
    model = Post
    login_url = '/login/'

    def get_query_set(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

@login_required()
def add_comment_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommitForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommitForm
    return render(request,'blog/comment_form.html',{'form':form})

@login_required()
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk)
    comment.approved()
    return redirect('post_detail',pk=comment.post.pk)

@login_required()
def comment_delete(request,pk):
    comment = get_object_or_404(Comment,pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

@login_required()
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)