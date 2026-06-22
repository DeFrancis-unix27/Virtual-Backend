from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from core.models import Home, About, Service, Testimonails, Gallery
from django_apps.blog.models import Blog
from django_apps.contact.models import ContactMessage
from django_apps.projects.models import Project, Certificate


def dashboard_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard-home")
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user and user.is_superuser:
            login(request, user)
            next_url = request.GET.get("next") or reverse("dashboard-home")
            return redirect(next_url)
        messages.error(request, "Invalid credentials or not an admin.")
    return render(request, "dashboard/login.html")


@login_required
def dashboard_logout(request):
    logout(request)
    return redirect("dashboard-login")


@login_required
def dashboard_home(request):
    ctx = {
        "home_count": Home.objects.count(),
        "about_count": About.objects.count(),
        "service_count": Service.objects.count(),
        "testimonial_count": Testimonails.objects.count(),
        "blog_count": Blog.objects.count(),
        "project_count": Project.objects.count(),
        "gallery_count": Gallery.objects.count(),
        "certificate_count": Certificate.objects.count(),
        "message_count": ContactMessage.objects.count(),
        "recent_messages": ContactMessage.objects.all().order_by("-created_at")[:5],
    }
    return render(request, "dashboard/home.html", ctx)


@login_required
def dashboard_home_edit(request):
    instance = Home.objects.first()
    if request.method == "POST":
        title = request.POST.get("title")
        subtitle = request.POST.get("subtitle")
        welcome_message = request.POST.get("welcome_message")
        if instance:
            instance.title = title
            instance.subtitle = subtitle
            instance.welcome_message = welcome_message
            instance.save()
        else:
            Home.objects.create(title=title, subtitle=subtitle, welcome_message=welcome_message)
        messages.success(request, "Home section updated.")
        return redirect("dashboard-home-edit")
    return render(request, "dashboard/form.html", {
        "title": "Edit Home",
        "fields": [
            {"name": "title", "label": "Title", "value": instance.title if instance else "", "type": "text"},
            {"name": "subtitle", "label": "Subtitle", "value": instance.subtitle if instance else "", "type": "text"},
            {"name": "welcome_message", "label": "Welcome Message", "value": instance.welcome_message if instance else "", "type": "textarea"},
        ],
        "action": "dashboard-home-edit",
    })


@login_required
def dashboard_about_edit(request):
    instance = About.objects.first()
    if request.method == "POST":
        heading = request.POST.get("heading")
        description = request.POST.get("description")
        tech_stack = request.POST.get("tech_stack", "")
        if instance:
            instance.heading = heading
            instance.description = description
            instance.tech_stack = [t.strip() for t in tech_stack.split(",") if t.strip()]
            instance.save()
        else:
            About.objects.create(heading=heading, description=description, tech_stack=[t.strip() for t in tech_stack.split(",") if t.strip()])
        messages.success(request, "About section updated.")
        return redirect("dashboard-about-edit")
    return render(request, "dashboard/form.html", {
        "title": "Edit About",
        "fields": [
            {"name": "heading", "label": "Heading", "value": instance.heading if instance else "", "type": "text"},
            {"name": "description", "label": "Description", "value": instance.description if instance else "", "type": "textarea"},
            {"name": "tech_stack", "label": "Tech Stack (comma separated)", "value": ", ".join(instance.tech_stack) if instance and instance.tech_stack else "", "type": "text"},
        ],
        "action": "dashboard-about-edit",
    })


@login_required
def dashboard_services(request):
    if request.method == "POST":
        Service.objects.create(
            title=request.POST.get("title"),
            icon=request.POST.get("icon"),
            description=request.POST.get("description"),
        )
        messages.success(request, "Service added.")
        return redirect("dashboard-services")
    services = Service.objects.all()
    return render(request, "dashboard/list.html", {
        "title": "Services",
        "items": services,
        "fields": ["title", "icon"],
        "delete_url": "dashboard-service-delete",
        "show_add": True,
    })


@login_required
def dashboard_service_delete(request, pk):
    get_object_or_404(Service, pk=pk).delete()
    messages.success(request, "Service deleted.")
    return redirect("dashboard-services")


@login_required
def dashboard_testimonials(request):
    if request.method == "POST":
        Testimonails.objects.create(
            name=request.POST.get("name"),
            role=request.POST.get("role"),
            testimonial=request.POST.get("testimonial"),
        )
        messages.success(request, "Testimonial added.")
        return redirect("dashboard-testimonials")
    testimonials = Testimonails.objects.all()
    return render(request, "dashboard/list.html", {
        "title": "Testimonials",
        "items": testimonials,
        "fields": ["name", "role"],
        "delete_url": "dashboard-testimonial-delete",
        "show_add": True,
    })


@login_required
def dashboard_testimonial_delete(request, pk):
    get_object_or_404(Testimonails, pk=pk).delete()
    messages.success(request, "Testimonial deleted.")
    return redirect("dashboard-testimonials")


@login_required
def dashboard_blog(request):
    if request.method == "POST":
        Blog.objects.create(
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            status=request.POST.get("status", "draft"),
        )
        messages.success(request, "Blog post added.")
        return redirect("dashboard-blog")
    blogs = Blog.objects.all().order_by("-created_at")
    return render(request, "dashboard/list.html", {
        "title": "Blog Posts",
        "items": blogs,
        "fields": ["title", "status"],
        "delete_url": "dashboard-blog-delete",
        "show_add": True,
    })


@login_required
def dashboard_blog_delete(request, pk):
    get_object_or_404(Blog, pk=pk).delete()
    messages.success(request, "Blog post deleted.")
    return redirect("dashboard-blog")


@login_required
def dashboard_projects(request):
    if request.method == "POST":
        Project.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            github_link=request.POST.get("github_link", ""),
            live_link=request.POST.get("live_link", ""),
            tech_stack=[t.strip() for t in request.POST.get("tech_stack", "").split(",") if t.strip()],
            state=request.POST.get("state", "not_started"),
        )
        messages.success(request, "Project added.")
        return redirect("dashboard-projects")
    projects = Project.objects.all().order_by("-created_at")
    return render(request, "dashboard/list.html", {
        "title": "Projects",
        "items": projects,
        "fields": ["title", "state"],
        "delete_url": "dashboard-project-delete",
        "show_add": True,
    })


@login_required
def dashboard_project_delete(request, pk):
    get_object_or_404(Project, pk=pk).delete()
    messages.success(request, "Project deleted.")
    return redirect("dashboard-projects")


@login_required
def dashboard_gallery(request):
    if request.method == "POST":
        Gallery.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description", ""),
        )
        messages.success(request, "Gallery item added.")
        return redirect("dashboard-gallery")
    items = Gallery.objects.all().order_by("-created_at")
    return render(request, "dashboard/list.html", {
        "title": "Gallery",
        "items": items,
        "fields": ["title", "created_at"],
        "delete_url": "dashboard-gallery-delete",
        "show_add": True,
    })


@login_required
def dashboard_gallery_delete(request, pk):
    get_object_or_404(Gallery, pk=pk).delete()
    messages.success(request, "Gallery item deleted.")
    return redirect("dashboard-gallery")


@login_required
def dashboard_messages(request):
    msgs = ContactMessage.objects.all().order_by("-created_at")
    return render(request, "dashboard/list.html", {
        "title": "Contact Messages",
        "items": msgs,
        "fields": ["name", "email", "created_at"],
        "show_add": False,
    })
