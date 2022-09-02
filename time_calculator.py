def add_time(start, duration, day=None):
    next_d = "(next day)"

    list_start_time = start.split()
    list_start = list_start_time[0].split(":")
    list_duration = duration.split(":")
    h = int(list_start[0]) + int(list_duration[0])
    ap = list_start_time[1]

    m = int(list_start[1]) + int(list_duration[1])
    if m > 60:
        if m % 60 != 0:
            h = h + (m // 60)
            m = m % 60
    if 12 < h < 24:
        h = h - 12

        if ap == "AM":
            ap = "PM"
        else:
            ap = "AM"
            re = str(h) + " : " + f'{m:02}' + " " + ap + " " + next_d
            if day:
                re = re + ", " + day
            return re

    if h == 12:
        if ap == "AM":
            ap = "PM"
        else:
            ap = "AM"
    re = str(h) + " : " + f'{m:02}' + " " + ap

    if day:
        re = re + ", " + day
        return re

    return re


if __name__ == '__main__':
    print(add_time("11:43 PM", "24:20", "tueSday"))

# Returns: 12:03 AM, Thursday (2 days later)
