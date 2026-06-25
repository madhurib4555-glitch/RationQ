from django.shortcuts import render
from .models import QueueToken

import qrcode


def join_queue(request):

    total_tokens = QueueToken.objects.count()

    token_number = f"RQ{100 + total_tokens + 1}"

    token = QueueToken.objects.create(
        user=request.user,
        token_number=token_number
    )

    people_ahead = total_tokens

    estimated_time = people_ahead * 5

    # QR Code Generation

    qr_data = f"Token: {token.token_number}"

    qr = qrcode.make(qr_data)

    qr_path = f"media/qr_codes/{token.token_number}.png"

    qr.save(qr_path)

    context = {

        'token_number': token.token_number,

        'people_ahead': people_ahead,

        'estimated_time': estimated_time,

        'qr_code': f"/media/qr_codes/{token.token_number}.png"

    }

    return render(request,
                  'queue_status.html',
                  context)
def my_queue(request):

    tokens = QueueToken.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request,
                  'my_queue.html',
                  {'tokens': tokens})
def live_queue(request):

    waiting_tokens = QueueToken.objects.filter(
        status='Waiting'
    ).order_by('created_at')

    current_token = None

    if waiting_tokens.exists():

        current_token = waiting_tokens.first()

    context = {

        'waiting_tokens': waiting_tokens,

        'current_token': current_token

    }

    return render(request,
                  'live_queue.html',
                  context)