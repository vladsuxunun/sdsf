from apscheduler.schedulers.blocking import BlockingScheduler
import requests
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=140)
def timed_job():
    requests.get("https://vkbacktask.herokuapp.com/task1")
    



sched.start()
