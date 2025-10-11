from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)


class CallsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calls'
    verbose_name = "Hospital Nurse Call System"

    def ready(self):
        """
        This method runs when the app is fully loaded.
        Use it to import signals or perform app initialization tasks.
        """
        try:
            import calls.signals  # noqa
            logger.info("✅ Calls app initialized successfully with signals.")
        except ImportError:
            logger.warning("⚠️ No signals module found in calls app.")
