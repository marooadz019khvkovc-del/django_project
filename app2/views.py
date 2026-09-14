from django.http import HttpResponse

def services_list(request):
    return HttpResponse("<h1>قائمة الخدمات - app2</h1>")

def pricing(request):
    return HttpResponse("<h1>أسعار الخدمات - app2</h1>")

def order(request):
    return HttpResponse("<h1>طلب خدمة - app2</h1>")