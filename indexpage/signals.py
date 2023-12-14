import json

from django.db.models.signals import Signal
from django.dispatch import receiver
from django.contrib import messages

# Определите сигнал
my_signal = Signal()


from django.http import HttpResponse

@receiver(my_signal)
def my_signal_handler(sender, request, **kwargs):
    messages.success(request, f"Объект {sender} был изменен")

    # Отправка события SSE
    event_data = {'message': f"Объект {sender} был изменен"}
    sse_response = HttpResponse(json.dumps(event_data), content_type='text/event-stream')
    sse_response['Cache-Control'] = 'no-cache'
    sse_response['Connection'] = 'keep-alive'
    return sse_response