from django.http import HttpResponse

def index(request):
    return HttpResponse('\
        <img \
            src="http://www.ku.ac.th/kunews/news59/12/bannerking10_5.jpg" \
            width="100%" \
            border="0"> \
    ')
