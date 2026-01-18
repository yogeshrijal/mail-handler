
from rest_framework.serializers import ModelSerializer
from mailhandler_app.models import Mailhandler 


class MailHandlerSerializers(ModelSerializer):
    class Meta:
        model=Mailhandler
        fields='__all__'
        read_only_fields=['sent_at','sent_count']