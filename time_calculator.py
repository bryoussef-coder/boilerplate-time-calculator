def add_time(start, duration, day=None):
    list_start_time = start.split()
    list_start = list_start_time[0].split(":")
    list_duration = duration.split(":")
    h = int(list_start[0]) + int(list_duration[0])
    ap = list_start_time[1]
    if 12 < h < 24:
        if h == 12:
            h = 12
        else:
            h = h - 12

        if ap == "AM":
            ap = "PM"
        else:
            ap = "AM"

    m = int(list_start[1]) + int(list_duration[1])
    if m > 60:
        if m % 60 != 0:
            h = h + (m // 60)
            m = m % 60

    re = str(h) + " : " + f'{m:02}' + " " + ap
    if day:
        re = re + ", " + day

    return re


if __name__ == '__main__':
    print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday
