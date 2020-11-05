from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class APIRootList(APIView):
    def get(self, request, lang, format=None):
        data = {
            'languages': reverse('languages', request=request, kwargs={"lang": lang}),
            'words': reverse('words', request=request, kwargs={"lang": lang}),
            'features': reverse('features', request=request, kwargs={"lang": lang}),
            'dimensions': reverse('dimensions', request=request, kwargs={"lang": lang}),
            'lemmas': reverse('lemmas', request=request, kwargs={"lang": lang}),
            'tagsets': reverse('tagsets', request=request, kwargs={"lang": lang}),
            'families': reverse('families', request=request, kwargs={"lang": lang}),
            'genera': reverse('genera', request=request)
        }
        return Response(data)
