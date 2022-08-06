from django.shortcuts import render
# add models
from .models import Post

# Create your views here.
from django.views import generic
from django.views.generic import TemplateView, DetailView
from rest_framework.views import APIView
from .models import Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse


def BlogPostLike(request, pk):
    print(request," *************** ")
    post = get_object_or_404(Post, id=request.POST.get('blogpost_id'))
    print(post, pk, "!!!!!!!!!!!!")
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('user_post_detail', args=[str(pk)]))


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutView(TemplateView):
    template_name = 'about/about.html'

class AddPost(APIView):
    """
    eAdd post and show all post of user
    """

    def get(self, request, format= None):
        pass


class UserPostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def post(request):
        pass
    def get(request):
        pass

class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data