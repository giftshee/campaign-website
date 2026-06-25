from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from .models import Gallery

from .models import (
    News,
    Volunteer,
    Contact,
    PageContent,
    ManifestoItem
)

from .forms import (
    NewsForm,
    ManifestoItemForm,
    ContactForm,
    PageContentForm
)

# ================= ADMIN CHECK =================

def admin_only(user):
    return user.is_authenticated and user.is_superuser


# ================= HOME =================

def home(request):
    news = News.objects.all().order_by('-date')[:3]
    volunteers_count = Volunteer.objects.count()

    home_page = get_object_or_404(PageContent, name="home")

    return render(request, "home.html", {
        "news": news,
        "volunteers_count": volunteers_count,
        "home": home_page
    })
@staff_member_required
def delete_home_image(request):

    home = get_object_or_404(PageContent, name="home")

    if request.method == "POST":

        if home.image:
            home.image.delete()

        home.image = None
        home.save()

    return redirect("home")

# ================= ABOUT =================

def about(request):
    about_page = get_object_or_404(PageContent, name="about")
    return render(request, "about.html", {"about": about_page})


# ================= NEWS =================

def news_list(request):
    news = News.objects.all().order_by('-date')
    return render(request, "news.html", {"news": news})


def news_detail(request, pk):
    item = get_object_or_404(News, pk=pk)
    return render(request, "news_detail.html", {"item": item})


@user_passes_test(admin_only)
def add_news(request):
    form = NewsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("news_list")
    return render(request, "news_form.html", {"form": form})


@user_passes_test(admin_only)
def edit_news(request, id):
    news = get_object_or_404(News, id=id)
    form = NewsForm(request.POST or None, request.FILES or None, instance=news)
    if form.is_valid():
        form.save()
        return redirect("news_list")
    return render(request, "news_form.html", {"form": form})


@user_passes_test(admin_only)
def delete_news(request, id):
    news = get_object_or_404(News, id=id)
    if request.method == "POST":
        news.delete()
        return redirect("news_list")
    return render(request, "confirm_delete.html", {"item": news})


# ================= VOLUNTEERS =================

def volunteer(request):
    if request.method == "POST":
        Volunteer.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            message=request.POST["message"]
        )
        messages.success(request, "Application received")
        return redirect("volunteer")

    return render(request, "volunteer.html")
@staff_member_required
def delete_volunteer(request, id):

    volunteer = get_object_or_404(
        Volunteer,
        id=id
    )

    if request.method == "POST":
        volunteer.delete()

    return redirect("dashboard_volunteers")


from django.core.paginator import Paginator

@login_required
def volunteer_dashboard(request):

    query = request.GET.get("q")

    volunteers = Volunteer.objects.all().order_by('-date')

    # SEARCH (optional)
    if query:
        volunteers = volunteers.filter(
            name__icontains=query
        ) | volunteers.filter(
            email__icontains=query
        ) | volunteers.filter(
            phone__icontains=query
        )

    # PAGINATION
    paginator = Paginator(volunteers, 5)  # 5 per page

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "dashboard/volunteers.html", {
        "page_obj": page_obj,
        "query": query
    })


# ================= CONTACT =================

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("contact")
    return render(request, "contact.html", {"form": form})


# ================= MANIFESTO =================

def manifesto(request):
    items = ManifestoItem.objects.all().order_by('-created_at')
    return render(request, "manifesto.html", {"items": items})
from django.shortcuts import render, redirect
from .models import Manifesto
from .forms import ManifestoForm

from django.shortcuts import render, redirect
from .models import Manifesto
from .forms import ManifestoForm

from django.shortcuts import render, redirect
from .models import Manifesto
from .forms import ManifestoForm

def manifesto_page(request):

    posts = Manifesto.objects.all().order_by('-created_at')

    form = ManifestoForm()

    if request.method == "POST":
        form = ManifestoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("manifesto")

    return render(request, "manifesto.html", {
        "form": form,
        "posts": posts
    })


@staff_member_required
def add_manifesto_item(request):
    form = ManifestoItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("manifesto")
    return render(request, "manifesto_form.html", {"form": form})


@staff_member_required
def delete_manifesto_item(request, pk):
    item = get_object_or_404(ManifestoItem, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect("manifesto")
    return render(request, "confirm_delete.html", {"item": item})


# ================= DASHBOARD =================

def dashboard(request):
    return render(request, "dashboard/index.html", {
        "volunteers": Volunteer.objects.count(),
        "news": News.objects.count(),
        "messages": Contact.objects.count(),
        "manifesto": ManifestoItem.objects.count(),
    })


@staff_member_required
def dashboard(request):
    context = {
        "volunteers": Volunteer.objects.count(),
        "news": News.objects.count(),
        "messages": Contact.objects.count(),
        "manifesto": ManifestoItem.objects.count(),
    }

    return render(request, "dashboard/index.html", context)


@staff_member_required
def dashboard_news(request):
    news = News.objects.all().order_by('-date')
    return render(request, "dashboard/news.html", {"news": news})


@staff_member_required
def dashboard_messages(request):
    messages_qs = Contact.objects.all().order_by('-id')
    return render(request, "dashboard/messages.html", {"messages": messages_qs})


@staff_member_required
def dashboard_manifesto(request):
    items = ManifestoItem.objects.all().order_by('-id')
    return render(request, "manifesto.html", {"items": items})
@staff_member_required
def delete_home_image(request):
    home = get_object_or_404(PageContent, name="home")

    if request.method == "POST" and home.image:
        home.image.delete()
        home.image = None
        home.save()

    return redirect("home")
@staff_member_required
def edit_page(request, page_name):
    page = get_object_or_404(PageContent, name=page_name)

    if request.method == "POST" and "delete_image" in request.POST:
        if page.image:
            page.image.delete()
            page.image = None
            page.save()
        return redirect(page_name)

    form = PageContentForm(request.POST or None, request.FILES or None, instance=page)

    if form.is_valid():
        form.save()
        return redirect(page_name)

    return render(request, "edit_page.html", {
        "form": form,
        "page": page
    })
@staff_member_required
def delete_home_image(request):
    home = get_object_or_404(PageContent, name="home")

    if request.method == "POST" and home.image:
        home.image.delete()
        home.image = None
        home.save()

    return redirect("home")
@staff_member_required
def delete_page_image(request, page_name):
    page = get_object_or_404(PageContent, name=page_name)

    if request.method == "POST" and page.image:
        page.image.delete(save=False)
        page.image = None
        page.save()

    return redirect(page_name)
# ================= DASHBOARD SECTIONS =================

@staff_member_required
def dashboard_volunteers(request):
    volunteers = Volunteer.objects.all().order_by("-date")

    return render(
        request,
        "dashboard/volunteers.html",
        {
            "volunteers": volunteers
        }
    )


@staff_member_required
def dashboard_news(request):
    news = News.objects.all().order_by("-date")

    return render(
        request,
        "dashboard/news.html",
        {
            "news": news
        }
    )


@staff_member_required
def dashboard_messages(request):
    contacts = Contact.objects.all().order_by("-id")

    return render(
        request,
        "dashboard/messages.html",
        {
            "messages": contacts
        }
    )


@staff_member_required
def dashboard_manifesto(request):
    items = ManifestoItem.objects.all().order_by("-created_at")

    return render(
        request,
        "manifesto.html",
        {
            "items": items
        }
    )

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Gallery
from .forms import GalleryForm


def gallery(request):
    images = Gallery.objects.all().order_by('-created_at')

    # ADD OR EDIT IN SAME PAGE
    if request.method == "POST":

        # EDIT MODE
        if "edit_id" in request.POST:
            image = get_object_or_404(Gallery, id=request.POST["edit_id"])
            form = GalleryForm(request.POST, request.FILES, instance=image)

        # ADD MODE
        else:
            form = GalleryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("gallery")

    else:
        form = GalleryForm()

    return render(request, "gallery.html", {
        "images": images,
        "form": form
    })


@staff_member_required
def delete_gallery(request, pk):
    image = get_object_or_404(Gallery, pk=pk)

    if request.method == "POST":
        image.delete()
        return redirect("gallery")

    return redirect("gallery")


def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]

        password = request.POST["password"]


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(request,user)

            return redirect("dashboard")


        else:

            messages.error(
                request,
                "Invalid login details"
            )


    return render(request,"login.html")



from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect("home")