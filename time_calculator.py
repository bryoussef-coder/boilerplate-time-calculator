def add_time(start, duration, day=None):
    next_d = "(next day)"
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

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
    # h > 24
    if h >= 24:
        nd = h // 24
        h = h % 24

        if 12 < h < 24:
            h = h - 12

            if ap == "AM":
                ap = "PM"
            else:
                ap = "AM"
                re = str(h) + " : " + f'{m:02}' + " " + ap + " (" + str(nd + 1) + " days later)"
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
            for i in range(7):
                if day == days[i]:
                    day = days[i + nd - 1]
                    break

            re = re + ", " + day + " (" + str(nd + 1) + " days later)"
            return re
        else:
            re = re + " (" + str(nd) + "days later)"
            return re
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
    print(add_time("6:30 PM", "205:12"))

# Returns: 7:42 AM (9 days later)
