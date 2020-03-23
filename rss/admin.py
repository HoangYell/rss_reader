from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User, Group
from rss.models import Rss
admin.site.site_header = 'RSS Reader Dashboard'
admin.site.site_title = 'RSS Reader Dashboard'
admin.site.index_title = 'RSS Reader Dashboard'


class AnonymousUser(User):
    has_module_perms = has_perm = __getattr__ = lambda s,*a,**kw: True


class RssAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'author', 'category', 'pub_date')
    list_filter = ('category',)
    search_fields = ('title', 'link', 'author', 'category', 'pub_date')
    list_per_page = settings.PAGINATION_ADMIN_DASHBOARD


# show, hire app in dashboard
admin.site.register(Rss, RssAdmin)
admin.site.unregister((User, Group))
# allow access from anyone
anonymous_user = User.objects.all().first() or AnonymousUser()
admin.site.has_permission = lambda r: setattr(r, 'user', anonymous_user) or True
