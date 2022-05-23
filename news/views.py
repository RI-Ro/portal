from django.shortcuts import render, redirect

# Create your views here.
from .models import NewsPost, Foto, Comment, UserPortal


def index(request):
    last_news = NewsPost.objects.last()
    sluj = NewsPost.objects.filter(type__slug='sluj').exclude(id=last_news.id)[:6]
    vosp = NewsPost.objects.filter(type__slug='vosp').exclude(id=last_news.id)[:6]
    all_foto = Foto.objects.all()
    banner = Foto.objects.get(id=207)

    content = {
        'sluj'  :   sluj,
        'vosp'  :   vosp,
        'last_news' :   last_news,
        'all_foto'  :   all_foto,
        'banner'    :   banner,
    }
    return render(request, 'news/index.html', content)


def detail_post(request, post_id):
    news_post = NewsPost.objects.filter(id=post_id)
    all_foto = Foto.objects.all()
    banner = Foto.objects.get(id=207)

    if len(news_post) > 0:
        comments = news_post[0].get_all_comment()
        content = {
                'news_post' :   news_post[0],
                'all_foto'  :   all_foto,
                'banner'    :   banner,
                'comments'  :   comments,
            }
        return render(request, 'news/detail_post.html', content )
    else:
        return render(request, 'news/error_search_post.html', {"post_id" : post_id})

def add_comment(request):
    try:
        c = Comment()
        c.message=request.POST['comment']
        c.user=UserPortal.objects.get(id=request.user.id)
        c.post=NewsPost.objects.get(id=request.POST['post-id'])
        c.save()
    except:
        pass
    return redirect('/post-id={}'.format(request.POST['post-id']))
