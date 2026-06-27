from django.db import models


# =========================
# NEWS
# =========================
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# =========================
# VOLUNTEERS
# =========================
class Volunteer(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name


# =========================
# CONTACT
# =========================
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# =========================
# SINGLE PAGE CMS SYSTEM
# (HOME + ABOUT + OTHER PAGES)
# =========================
class PageContent(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True
    )

    title = models.CharField(
        max_length=200
    )

    content = models.TextField()


    # Main page image
    image = models.ImageField(
        upload_to="pages/",
        null=True,
        blank=True
    )


    # Homepage background image
    background_image = models.ImageField(
        upload_to="backgrounds/",
        null=True,
        blank=True
    )


    def __str__(self):
        return self.name


# =========================
# MANIFESTO ITEMS (optional structured section)
# =========================
class ManifestoItem(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=50, default="📌")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Manifesto(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to='manifesto/',
        blank=True,
        null=True
    )

    youtube_link = models.URLField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.title
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from django.db import models


class Gallery(models.Model):

    title = models.CharField(
        max_length=200
    )

    image = models.ImageField(
        upload_to="gallery/"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.title