from rest_framework import viewsets, generics, status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ethereum.scripts.election import create_election, create_vote, get_result
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

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super().retrieve(request, pk, *args, **kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        return super().update(request, pk, *args, **kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        return super().partial_update(request, pk, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        return super().destroy(request, pk, *args, **kwargs)


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny, ]
        else:
            self.permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        return super().retrieve(request, pk, *args, **kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        return super().update(request, pk, *args, **kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        return super().partial_update(request, pk, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        return super().destroy(request, pk, *args, **kwargs)


class VoteViewSet(GenericViewSet):
    serializer_class = VoteSerializer
    queryset = Election.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def retrieve(self, request, pk):
        results = []
        election = self.get_object()
        candidates = Candidate.objects.filter(Election=election)
        for candidate in candidates:
            vote_count = get_result(election.id, candidate.id)
            results.append({
                'id': candidate.id,
                'count': vote_count,
            })
        res = {
            'status': True,
            'results': results,
        }
        return Response(res, status=status.HTTP_200_OK)

    def create(self, request):
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

        create_vote(data['_election'].id, data['_voter'].id, data['_candidate'].id)
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


class ElectionOptionsViewSet(GenericViewSet):
    serializer_class = ElectionSerializer
    queryset = Election.objects.all()

    def retrieve(self, request, pk):
        election = self.get_object()
        candidates = Candidate.objects.filter(Election=election)
        candidate_ids = [candidate.id for candidate in candidates]
        tx = create_election(election.id, election.StartDate, election.EndDate, candidate_ids)
        res = {
            'status': True,
            'message': 'Election registered successfully',
        }
        return Response(res, status=status.HTTP_200_OK)
