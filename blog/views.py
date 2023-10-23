from django.views.generic import DetailView
from blog.models import Post


class PostDetailView(DetailView):
    model = Post