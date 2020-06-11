from django.http import Http404
from rest_framework import status
from rest_framework import filters
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Feature, Language, Dimension, Word, Lemma, TagSet, Family, Genus, POS
from .serializers import (FeatureSerializer, LanguageSerializer, DimensionSerializer,
                          WordSerializer, TagSetSerializer, LemmaSerializer,
                          FamilySerializer, GenusSerializer, RelatedWordSerializer)

class APIRootList(APIView):
    def get(self, request, format=None):
        data = {
            'languages': reverse('languages', request=request),
            'words': reverse('words', request=request),
            'features': reverse('features', request=request),
            'dimensions': reverse('dimensions', request=request),
            'lemmas': reverse('lemmas', request=request),
            'tagsets': reverse('tagsets', request=request),
            'families': reverse('families', request=request),
            'genuses': reverse('genuses', request=request)
        }
        return Response(data)


class FeatureList(generics.ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    filterset_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'dimension']


class LanguageList(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    filterset_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'family', 'genus', 'walsCode']


class DimensionList(generics.ListAPIView):
    queryset = Dimension.objects.all()
    serializer_class = DimensionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class WordList(generics.ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class LemmaList(generics.ListAPIView):
    queryset = Lemma.objects.all()
    serializer_class = LemmaSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['language', 'animacy', 'transivity', 'author', 'pos', 'date_updated']
    search_fields = ['name']


class GenusList(generics.ListAPIView):
    queryset = Genus.objects.all()
    serializer_class = GenusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class TagSetList(generics.ListAPIView):
    queryset = TagSet.objects.all()
    serializer_class = TagSetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'features']


class FamilyList(generics.ListAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
