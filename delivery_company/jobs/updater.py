from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import battery_log


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(battery_log, 'interval', minutes=30)
    scheduler.start()


