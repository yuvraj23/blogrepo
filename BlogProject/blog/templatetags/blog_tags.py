from blog.models import Post
from django import template
register = template.Library()

@register.simple_tag(name='my_tag')
def total_post():
    return Post.objects.count()


@register.inclusion_tag('blog/latest_post.html')
def show_latest_posts():
    latest_post=Post.objects.order_by('-publish')[:3]
    return {'latest_post':latest_post}

from django.db.models import Count
@register.simple_tag
def get_most_commented_post(count=5):
    most_commented_post= Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
    return {'most_commented_post':most_commented_post}
