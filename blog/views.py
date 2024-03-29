from django.shortcuts import render,get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail
from django.contrib.postgres.search import SearchVector
from .forms import EmailPostForm, CommentForm, SearchForm
from django.db.models import Count


def post_list(request):
    object_list = Post.published.all()
    
   
    paginator = Paginator(object_list, 3) #3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the firstpage
        posts = paginator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page of results
        posts = Paginator.page(Paginator.num_pages)
    return render(request, 'blog/post/list.html',{'page':page,'posts':posts})
        
def post_detail(request,year, month, day, post):
    """a view to display a single post"""
    post = get_object_or_404(Post, slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    #List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        Comment_form = CommentForm(data=request.POST)
        if Comment_form.is_valid():
            #create comment object but dont save to database yet
            new_comment = Comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # save the comment to the database
            new_comment.save()
    else:
        Comment_form = CommentForm()
    #List of similar posts
    
    return render(request,'blog/post/detail.html',{'post':post,'comments':comments,'new_comment':new_comment,'comment_form':Comment_form})

def post_share(request, post_id):
    #retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        #form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = '{} ({}) recommends you reading " {}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com',[cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request,'blog/post/share.html',{'post':post,'form':form,'sent':sent})
    
def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.annotate(
                search=SearchVector('title', 'body'),
            ).filter(search=query)
    return render(request,
                  'blog/post/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})

                   