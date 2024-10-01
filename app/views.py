from django.shortcuts import render, redirect
from django.views import View
from .forms import MessageForm
from .models import Message


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        form = MessageForm()
        messages = Message.objects.all().order_by('-date')
        context = {
            'form': form,
            'messages': messages,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        messages = Message.objects.all().order_by('-date')
        context = {
            'form': form,
            'messages': messages,
        }
        return render(request, self.template_name, context)
