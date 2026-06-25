from django import forms
from .models import News, Contact, ManifestoItem, PageContent


# ================= CONTACT =================

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


# ================= NEWS =================

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image']


# ================= MANIFESTO =================

class ManifestoItemForm(forms.ModelForm):
    class Meta:
        model = ManifestoItem
        fields = ['title', 'icon', 'description']


# ================= PAGE CONTENT (HOME / ABOUT / ETC) =================

class PageContentForm(forms.ModelForm):
    class Meta:
        model = PageContent
        fields = ['title', 'content', 'image']
        from django import forms
from .models import Manifesto

class ManifestoForm(forms.ModelForm):
    class Meta:
        model = Manifesto
        fields = ['title', 'description', 'video', 'youtube_link']
        from django import forms
from .models import Gallery

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image']