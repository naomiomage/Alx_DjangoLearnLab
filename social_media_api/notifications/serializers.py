# notifications/serializers.py
from rest_framework import serializers
from .models import Notification
from django.contrib.contenttypes.models import ContentType

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    recipient = serializers.ReadOnlyField(source='recipient.username')
    target_repr = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target_content_type', 'target_object_id', 'target_repr', 'unread', 'timestamp']
        read_only_fields = ['id', 'recipient', 'actor', 'verb', 'target_content_type', 'target_object_id', 'target_repr', 'timestamp']

    def get_target_repr(self, obj):
        if obj.target is None:
            return None
        return str(obj.target)
