from django.views.generic import View
from django.shortcuts import render
from django.contrib import messages
from ..methods import send_wa
class TestSend(View):
    def get(self,request):
        return render(request, "test-send.html")

    def post(self,request):
        sender = request.POST.get("sender")
        recepiant = request.POST.get("recepiant")
        message = request.POST.get("message")

        if not sender or not recepiant or not message:
            messages.error(request, "All filed is required")
            return render(request, "test-send.html")
        send_wa(sender,recepiant,message)
        return render(request, "test-send.html")
