from django.shortcuts import render
from blogpage.models import BlogPostTable
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

# Create your views here.
def blogPage(request):
    allPosts = BlogPostTable.objects.all()
    items_per_page = 2

    paginator = Paginator(allPosts, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'allPosts': allPosts
    }
    return render(request, 'blog/blog.html', context)


def blogPost(request,author):
    print(author)
    post = BlogPostTable.objects.filter(author=author).first()
    return render(request, 'blog/blogPost.html', {'post': post})
