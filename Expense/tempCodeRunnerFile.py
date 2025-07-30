from django.utils import timezone
now = timezone.now()  # timezone-aware, Nepal time due to settings
print(now)