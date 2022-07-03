from django.urls import path, include
from rest_framework import routers

from vote.views import ElectionViewSet, CandidateViewSet, VoteView

router = routers.DefaultRouter()
router.register('election', ElectionViewSet)
router.register('candidate', CandidateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('vote/', VoteView.as_view()),
]
