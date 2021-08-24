from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from . models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic  import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)

#def home(request):
#	content={
#	'contents':Post.objects.all()
#	}
#	return render(request,'blog/home.html',content)



class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'contents'
	ordering = ['-date']
	paginate_by='2'


class UserPostListView(ListView):
	model = Post
	template_name = 'blog/blog_user.html'
	context_object_name = 'contents'
	paginate_by='2'

	def get_queryset(self):
		username=get_object_or_404(User,username=self.kwargs.get('username'))
		return Post.objects.filter(author=username).order_by('-date')






class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/blog_detail.html'

class Post_Delete_View(DetailView):
	model = Post
	template_name = 'blog/blog_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields =['title','body','date']
	template_name = 'blog/blog_create.html'

	def form_valid(self, form):
		form.instance.author=self.request.user
		return super().form_valid(form)

class PostupdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields =['title','body','date']
	template_name = 'blog/blog_create.html'

	def form_valid(self, form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False



class PostdeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post 
	success_url='/'
	template_name = 'blog/blog_delete.html'

	def form_valid(self, form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False



def about(request):
	return render( request, "blog/about.html",{'title':'About us'})



