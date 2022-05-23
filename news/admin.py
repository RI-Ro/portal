from django.contrib import admin

# Register your models here.
from .models import UserPortal, Razdel, NewsPost, Comment, TypeNews, \
                    FotoGalery, Foto

admin.site.register(UserPortal)
admin.site.register(Razdel)
admin.site.register(NewsPost)
admin.site.register(Comment)
admin.site.register(TypeNews)
admin.site.register(FotoGalery)
admin.site.register(Foto)
