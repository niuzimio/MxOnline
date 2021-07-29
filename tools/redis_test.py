import redis
import time
r = redis.Redis(host='localhost', port=6379, db=0, charset="utf8", decode_responses=True)

r.set("15991030771", "1234")
# 设置过期时间
r.expire('mobile', 60*10000)

time.sleep(1)
print(r.get("15991030771"))
