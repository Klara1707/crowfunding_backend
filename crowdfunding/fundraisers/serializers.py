
from rest_framework import serializers
from .models import Fundraiser, Pledge


class PledgeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Pledge
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.anonymous:
            rep['owner'] = None
        return rep


class FundraiserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Fundraiser
        fields = '__all__'



class FundraiserDetailSerializer(FundraiserSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    class Meta:
        model = Fundraiser
        fields = [
            'id', 'title', 'description', 'goal', 'image',
            'is_open', 'date_created', 'owner', 'pledges'
        ]

