import logging
from datetime import datetime
from for_apscheduler import create_logger
from apscheduler.schedulers.blocking import BlockingScheduler
import os

def tick1():
    logger = logging.getLogger('logger1')
    logger.info("{} info: finish merge aritcle date---------------".format(datetime.now()))
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    create_logger()
    scheduler = BlockingScheduler()
    scheduler.add_job(tick1, 'interval', seconds=2)
    print('Press Ctrl+{0} to exit'.format('q' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass