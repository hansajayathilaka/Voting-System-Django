from django.contrib.auth.models import User
from rest_framework import serializers

from vote.models import Election, Candidate


class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class VoteSerializer(serializers.Serializer):
    candidate = serializers.IntegerField(
        label='Candidate ID',
        write_only=True,
        required=True,
    )
    election = serializers.IntegerField(
        label='Election ID',
        write_only=True,
        required=True,
    )

    def validate(self, attrs):
        candidate = attrs['candidate']
        election = attrs['election']

        _voter = self.context['request'].user
        _candidate = Candidate.objects.get(id=candidate)
        _election = Election.objects.get(id=election)

        attrs['_voter'] = _voter
        attrs['_candidate'] = _candidate
        attrs['_election'] = _election
        return attrs
