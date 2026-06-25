from django.contrib import admin
from .models import QueueToken


@admin.register(QueueToken)
class QueueTokenAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'token_number',
        'status',
        'created_at'
    )

    list_filter = ('status',)

    search_fields = (
        'token_number',
        'user__username'
    )