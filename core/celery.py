import os
from celery import Celery
import logging

# Initialize logger
logger = logging.getLogger(__name__)

# Set default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Create Celery app
app = Celery("core")

# Load config from Django settings with 'CELERY_' prefix
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks from all installed apps
app.autodiscover_tasks()

# Optional: log when Celery is ready
@app.on_after_configure.connect
def setup_logger(sender, **kwargs):
    logger.info("✅ Celery is configured and ready")
