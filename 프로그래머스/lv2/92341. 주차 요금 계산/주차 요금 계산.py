from collections import defaultdict
import math

def get_dict():
    return {
        "time": 0,
        "status": ""
    }

def solution(fees, records):
    answer = []
    d = defaultdict(get_dict)
    for record in records:
        l = record.split()
        h = l[0].split(":")
        th = int(h[0]) * 60 + int(h[1])
        if l[2] == "IN":
            d[l[1]]["time"] -= th
        else:
            d[l[1]]["time"] += th
        d[l[1]]["status"] = l[2]
    for k, v in d.items():
        time = v["time"]
        if v["status"] == "IN":
            time += 1439
        payment = fees[1]
        if (x:=time - fees[0]) > 0:
            payment += math.ceil(x / fees[2]) * fees[3]
        answer.append((k, payment))
    answer.sort(key=lambda x: x[0])
    return [x[1] for x in answer]