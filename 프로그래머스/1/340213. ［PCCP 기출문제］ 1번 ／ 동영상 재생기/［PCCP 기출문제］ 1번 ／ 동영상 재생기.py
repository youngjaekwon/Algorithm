def in_op(osm, oss, oem, oes, m, s):
    if osm <= m <= oem:
        if osm == m == oem:
            return oss <= s <= oes
        elif osm == m:
            return oss <= s
        elif oem == m:
            return s <= oes
        return True
    else:
        return False
    
def compare_time(a, b):
    if a[0] > b[0]:
        return True
    elif a[0] < b[0]:
        return False
    else:
        return a[1] > b[1]

def cal_time(m, s, t):
    s += t
    if s < 0:
        m -= 1
        s += 60
    elif s >= 60:
        m += 1
        s -= 60
    if m > -1:
        return max(0, m), max(0, s)
    else:
        return 0, 0

def add_time(vlm, vls, m, s, t):
    nm, ns = cal_time(m, s, t)
    if nm == 0 and ns < 10:
        return 0, 0
    if compare_time((nm, ns), cal_time(vlm, vls, -10)):
        return vlm, vls
    return nm, ns

def to_string(cm, cs):
    sm = str(cm)
    ss = str(cs)
    if cm < 10:
        sm = "0" + sm
    if cs < 10:
        ss = "0" + ss
    return f"{sm}:{ss}"

def solution(video_len, pos, op_start, op_end, commands):
    commands.append("end")
    osm, oss = tuple(map(int, op_start.split(":")))
    oem, oes = tuple(map(int, op_end.split(":")))
    vlm, vls = tuple(map(int, video_len.split(":")))
    cm, cs = tuple(map(int, pos.split(":")))
    for command in commands:
        if in_op(osm, oss, oem, oes, cm, cs):
            cm, cs = oem, oes
        if command == "end":
            break
        elif command == "next":
            cm, cs = add_time(vlm, vls, cm, cs, 10)
        else:
            cm, cs = add_time(vlm, vls, cm, cs, -10)
        print(cm, cs)
    return to_string(cm, cs)