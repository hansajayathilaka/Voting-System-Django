from django.urls import path, include
from rest_framework import routers

from vote.views import ElectionViewSet, CandidateViewSet, VoteViewSet, ElectionOptionsViewSet

router = routers.DefaultRouter()
router.register('election', ElectionViewSet)
router.register('candidate', CandidateViewSet)
router.register('vote', VoteViewSet)
router.register('election/register', ElectionOptionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
