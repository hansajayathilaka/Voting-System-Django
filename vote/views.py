from rest_framework import viewsets, generics, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from vote.models import Election, Candidate, Vote
from vote.serializers import ElectionSerializer, CandidateSerializer, VoteSerializer


class ElectionViewSet(viewsets.ModelViewSet):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny, ]
        else:
            self.permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
        return super().get_permissions()

    def list(self, request):
        return super().list(request)

    def create(self, request):
        return super().create(request)

    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk)

    def update(self, request, pk=None):
        return super().update(request, pk)

    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk)

    def destroy(self, request, pk=None):
        return super().destroy(request, pk)


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny, ]
        else:
            self.permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
        return super().get_permissions()

    def list(self, request):
        return super().list(request)

    def create(self, request):
        return super().create(request)

    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk)

    def update(self, request, pk=None):
        return super().update(request, pk)

    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk)

    def destroy(self, request, pk=None):
        return super().destroy(request, pk)


class VoteView(generics.GenericAPIView):
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)

    def get(self):
        res = {
            'status': True,
            'results': [
                {
                    'id': 1,  # Candidate ID
                    'count': 50,  # Number of votes
                },
                {
                    'id': 2,  # Candidate ID
                    'count': 150,  # Number of votes
                },
            ],
        }
        return Response(res, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        serializer = VoteSerializer(data=self.request.data,
                                    context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        vote = Vote.objects.filter(Voter=data['_voter'],
                                   Election=data['_election'])
        if vote.count():
            res = {
                'status': False,
                'message': 'You have already voted for this election',
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

        vote = Vote(Voter=data['_voter'],
                    Candidate=data['_candidate'],
                    Election=data['_election'])
        vote.save()
        res = {
            'status': True,
            'id': vote.id,
            'created_at': vote.Created_At,
            'message': 'Vote successfully casted',
        }
        return Response(res, status=status.HTTP_202_ACCEPTED)