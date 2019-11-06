from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy

from .models import ImagePost
from .forms import PostForm

class IndexView(generic.ListView):
    template_name = 'image_post/index.html'
    context_object_name = 'image_posts'

    def get_queryset(self):
        return ImagePost.objects.all().order_by('-votes')


class DetailView(generic.DetailView):
    model = ImagePost
    template_name = 'image_post/detail.html'

class CreatePost(generic.edit.CreateView):
    model = ImagePost
    form_class = PostForm
    template_name = 'image_post/new.html'
    success_url = '/image_post/'

def vote(request, image_post_id):
    image_post = get_object_or_404(ImagePost, pk=image_post_id)
    image_post.votes += 1
    image_post.save()
    return HttpResponseRedirect(reverse('image_post:detail', args=(image_post.id,)))