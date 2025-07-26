import logging

logger = logging.getLogger(__name__)


class CronManager:
    def __init__(self, sessions):
        logger.debug('Initializing cron')
        self.sessions = sessions

    def run(self):
        logger.debug('Running cron')
        self.cron_check_running_sessions()
        self.cron_send_notifications()
        return True

    def cron_check_running_sessions(self):
        logger.debug('Checking running sessions')
        self.sessions.terminate_past_sessions()
        return True

    def cron_send_notifications(self):
        self.sessions.send_notifications()
        return True
