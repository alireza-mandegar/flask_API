from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

scheduler = BlockingScheduler()


@scheduler.scheduled_job(IntervalTrigger(seconds=1))
def train_model():
    print("hello dude!")


scheduler.start()
