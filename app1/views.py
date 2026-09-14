from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>مرحباً بك في app1 - الصفحة الرئيسية</h1>")

def about(request):
    return HttpResponse("<h1>عن app1</h1>")

def contact(request):
    return HttpResponse("<h1>تواصل معنا في app1</h1>")