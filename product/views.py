from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import (
    JSONRenderer,
    TemplateHTMLRenderer
)
from rest_framework.response import Response
import stripe
stripe.api_key = "pk_test_51OQ6b4HjieNRHn3Stkh9MFWM7x4laX45AeOvCgG2MFTPihREx6wA5JZdWyXH0opUVUhvVJKd8cDzvB5I4RKHMdT200RQlC4iLn"

@api_view(('GET',))

def get_buy(request, pk):
    return Response({
        "message": True
    })
