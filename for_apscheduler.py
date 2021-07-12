from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import logging
import logging.handlers
logging_file_dir = r"D:\\"


def create_logger():
    trace_handler = logging.FileHandler(os.path.join(logging_file_dir,'logger.txt'))
    trace_handler.setFormatter(logging.Formatter('%(message)s'))
    log_trace = logging.getLogger('logger1')
    log_trace.addHandler(trace_handler)
    log_trace.setLevel(logging.INFO)


def tick():
    logger = logging.getLogger('logger1')
    logger.info("{} info: finish merge aritcle date".format(datetime.now()))
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    create_logger()
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=1)
    print('Press Ctrl+{0} to exit'.format('q' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
