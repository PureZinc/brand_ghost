from rest_framework import serializers as ser
from newsletter.models import Subscriber, Newsletter


date_format = "Date: %m/%d/%Y | Time: %I:%M %p"

class SubscribersSer(ser.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['id', 'email', 'subscribed_at']
    
    subscribed_at = ser.DateTimeField(format=date_format)
    

class NewsletterSer(ser.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['id', 'subject', 'html_message', 'sent_date', 'recipients']
    
    sent_date = ser.DateTimeField(format=date_format)
