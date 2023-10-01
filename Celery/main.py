from tasks import add
import time

res = add.delay(10, 5)
print("Task ID is: ", res.id)

while not res.ready():
    print('Task is not ready')
    time.sleep(1)

print(res.status)

print("The Result is: ", res.get())