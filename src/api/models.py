from django.db import models


class RequestLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    ipaddress = models.CharField(max_length=24, blank=True, default="")

    class Meta:
        db_table = "request_log"
