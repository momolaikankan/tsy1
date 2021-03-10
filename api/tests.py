LOCK_TIMEOUT = 3
lock = 0
lock_timeout = 0
lock_key = 'lock.foo'

# 获取锁
while lock != 1:
    now = int(time.time())
    lock_timeout = now + LOCK_TIMEOUT + 1
    lock = redis_client.setnx(lock_key, lock_timeout)
    if lock == 1 or (now > int(redis_client.get(lock_key))) and now > int(redis_client.getset(lock_key, lock_timeout)):
        break
    else:
        time.sleep(0.001)

# 已获得锁
do_job()

# 释放锁
now = int(time.time())
if now < lock_timeout:
    redis_client.delete(lock_key)
