from celery import shared_task
from datetime import *
import random
import json

@shared_task(name = "sum_of_2_nums")
def adder():
    now = datetime.now()
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    sum = n1+n2
    sjson = {}
    sjson["number1"] = str(n1)
    sjson["number2"] = str(n2)
    sjson["sum"] = str(sum)
    sjson["pubDate"] = str(now)
    print(str(sjson))
    f = open("currentval.txt","w")
    json.dump(sjson,f)
    f.close()
    return sjson