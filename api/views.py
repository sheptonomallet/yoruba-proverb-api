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


from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import Proverb
from .serializers import ProverbSerializer


class ProverbListAPI(ListAPIView):
    queryset = Proverb.objects.order_by("yoruba")[:5]
    serializer_class = ProverbSerializer


class ProverbDetailAPI(RetrieveAPIView):
    queryset = Proverb
    serializer_class = ProverbSerializer


class ProverbCreateAPI(CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Proverb
    serializer_class = ProverbSerializer


class ProverbUpdateAPI(UpdateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Proverb
    serializer_class = ProverbSerializer


class ProverbDeleteAPI(DestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Proverb
    serializer_class = ProverbSerializer
