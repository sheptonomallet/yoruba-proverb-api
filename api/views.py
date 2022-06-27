# from django.http import JsonResponse
# from cleantext import clean
# # Create your views here.


# def index(request):

#     context = {
#         'yoruba': 'Ti asín yé asín kó tó ṣẹnu gbọọrọ; ti ọ̀kùn yé ọ̀kùn kó tó fi igba ẹsẹ̀ rìn.',
#         'english': 'The moonrat has its reasons for having a long mouth; the millipede has its reasons for moving with hundreds of legs.',
#         'wisdom': 'People have their reasons: give them the benefit of the doubt.'}
#     clean(context,fix_unicode=True, to_ascii=True, )
#     return JsonResponse(context)


from rest_framework import viewsets
from .models import Proverb
from .serializers import ProverbSerializer



class ProverbViewSet(viewsets.ModelViewSet):
    queryset = Proverb.objects.order_by('yoruba')[:5]
    # queryset = Proverb.objects.all()
    serializer_class = ProverbSerializer

# 10 random proverbs

