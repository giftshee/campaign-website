from django.contrib import admin
from .models import News, Volunteer
def admin_only(user):
    return user.is_superuser

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
from .models import Contact

admin.site.register(Contact)
from django.contrib import admin
from .models import PageContent

admin.site.register(PageContent)


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'status', 'date')
    list_filter = ('status',)
    search_fields = ('name', 'phone', 'email')
    from django.contrib import admin
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'created_at'
    )
from .models import Manifesto


@admin.register(Manifesto)
class ManifestoAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'created_at'
    )
