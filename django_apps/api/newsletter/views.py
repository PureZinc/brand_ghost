from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from newsletter.models import Subscriber, Newsletter
from .serializers import SubscribersSer, NewsletterSer
from newsletter.utils.utils import send_newsletter


class SubscribersView(APIView):
    def get(self, request):
        subs = Subscriber.objects.all()
        serializer = SubscribersSer(subs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class NewslettersView(APIView):
    def get(self, request):
        newsletters = Newsletter.objects.all()
        serializer = NewsletterSer(newsletters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SendNewsletterView(APIView):
    def get(self, request, id):
        try:
            newsletter = Newsletter.objects.get(id=id)
        except Newsletter.DoesNotExist:
            return Response({'error': "Newsletter doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = NewsletterSer(newsletter)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, id):
        try:
            newsletter = Newsletter.objects.get(id=id)
        except Newsletter.DoesNotExist:
            return Response({'error': "Newsletter doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        
        subject = newsletter.subject
        html = newsletter.html_message
        
        subs = Subscriber.objects.all()
        recipients = [sub.email for sub in subs]
        
        try:
            send_newsletter(subject, html, recipients=recipients)
        except Exception as e:
            return Response({'error': f"Error removing product from cart: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'message': "Successfully sent newsletter!"}, status=status.HTTP_200_OK)
