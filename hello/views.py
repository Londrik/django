from django.shortcuts import render, redirect
from django.utils.timezone import datetime
from django.views.generic import ListView
from hello.forms import LogMessageForm
from hello.models import LogMessage

class HomeListView(ListView):
    model = LogMessage
    template_name = "hello/home.html"
    context_object_name = "message_list"

    def get_queryset(self):
        return LogMessage.objects.order_by("-log_date")[:5]

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    return render(request, "hello/log_message.html", {"form": form})

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")
