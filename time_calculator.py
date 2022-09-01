def add_time(start, duration):
    verif_format_start(start)
    if duration:
        verif_format_duration(duration)


def verif_format_start(start):
    try:
        if start.split()[1] not in ["PM", "AM"]:
            print("format start est invalid")
        else:
            return
            # print("le format start est valid")
    except:
        print("Le format start est invalid")


def verif_format_duration(duration):
    verif = duration.split(":")
    if int(verif[0]) > 12 or int(verif[1]) > 60:
        print("le format duration invalid")


if __name__ == '__main__':
    add_time("3:00 PM", "150:00")

