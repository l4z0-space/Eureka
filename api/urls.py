from django.urls import path
# flake8: noqa
import api.views as views
from urllib import parse

urlpatterns = [
    path('<str:lang>/', views.APIRootList.as_view(), name='root'),
    # All-models views
    # path('users/', views.UserList.as_view(), name='users'),
    path('<str:lang>/families/', views.FamilyList.as_view(), name='families'),
    path('<str:lang>/languages/', views.LanguageList.as_view(), name='languages'),
    path('<str:lang>/dimensions/', views.DimensionList.as_view(),name='dimensions'),
    path('<str:lang>/features/', views.FeatureList.as_view(), name='features'),
    path('genera/', views.GenusList.as_view(), name='genera'),
    path('<str:lang>/tagsets/', views.TagSetList.as_view(), name='tagsets'),
    path('<str:lang>/lemmas/', views.LemmaList.as_view(), name='lemmas'),
    path('<str:lang>/words/', views.WordList.as_view(), name='words'),
    # Detail-Views
    path('<str:lang>/dimensions/<str:name>/', views.DimensionDetail.as_view(), name='dimensionDetail'),
    path('<str:lang>/features/<str:name>/', views.FeatureDetail.as_view(),name='featureDetail'),
    path('<str:lang>/words/<str:name>/', views.WordDetail.as_view(),name='wordDetail'),
    path('<str:lang>/lemmas/<str:name>/', views.LemmaDetail.as_view(), name='lemmaDetail'),
    path('<str:lang>/tagsets/<str:name>/', views.TagSetDetail.as_view(),name='tagsetDetail'),
    # Download Views
    path('download/dimensions/', views.DimensionDownload.as_view(),name='dim-down'),
    path('download/features/', views.FeatureDownload.as_view(),name='feat-down'),
    path('download/languages/', views.LanguageDownload.as_view(),name='lang-down'),
    path('download/genera/', views.GenusDownload.as_view(),name='gen-down'),
    path('download/families/', views.FamilyDownload.as_view(),name='fam-down'),
    path('download/words/<str:languageName>/', views.WordDownload.as_view()),
    path('download/families/<str:familyName>/', views.FamilyQueryDownload.as_view()),
    path('download/genera/<str:genusName>/', views.GenusQueryDownload.as_view()),
    path('download/all/', views.AllLanguagesDownload.as_view()),
]
