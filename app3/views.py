from django.http import HttpResponse

def news_list(request):
    return HttpResponse("<h1>قائمة الأخبار - app3</h1>")

def updates(request):
    return HttpResponse("<h1>آخر التحديثات - app3</h1>")

def details(request):
    return HttpResponse("<h1>تفاصيل الخبر - app3</h1>")