from api.models import Feature, Language, Dimension, Word, TagSet, Family, Genus, Lemma, POS
from rest_framework import serializers


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class DimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dimension
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'


class TagSetSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)

    class Meta:
        model = TagSet
        fields = '__all__'


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'


class GenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genus
        fields = '__all__'


class LemmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lemma
        fields = '__all__'


class PosSerializer(serializers.ModelSerializer):
    class Meta:
        model = POS
        fields = '__all__'


class RelatedWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'name']
