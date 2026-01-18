from platform import node
from django.shortcuts import render
from django.conf import settings
from mailhandler_app import serializers
from mailhandler_app.serializers import MailHandlerSerializers
from mailhandler_app.models import Mailhandler
from rest_framework import viewsets 
from django.core.mail import send_mass_mail
from rest_framework.response import Response
from rest_framework import status
import asyncio
from asgiref.sync import sync_to_async
from  rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class mailHandlerViewsets(viewsets.ModelViewSet):
    queryset=Mailhandler.objects.all()
    serializer_class=MailHandlerSerializers

    def create(self,request,*args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject=serializer.validated_data['subject']
        message=serializer.validated_data['message']
        recipient_list=serializer.validated_data['recipient_list']
        from_email=settings.DEFAULT_FROM_EMAIL
        email_data=[
            (subject,message,from_email,[email])
            for  email in recipient_list
        ] 
        async def send_emails(): 
            await sync_to_async(send_mass_mail)(email_data,fail_silently=False)
        
        try:
            loop=asyncio.get_event_loop()
            if loop.is_running():
                loop.create_task(send_emails())
            else:
                loop.run_until_complete(send_emails())
        except RuntimeError:
            asyncio.run(send_emails())
        
        serializer.save(sent_count=len(recipient_list))
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]


   