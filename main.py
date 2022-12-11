def add_time(start_time, duration, day=""):
    day = day.lower()
    day = day.capitalize()

    dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    dict_day = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7
    }
    # Split the time too hours and minutes
    start_list = start_time.split(":")
    duration_list = duration.split(":")
    result_hour = int(start_list[0]) + int(duration_list[0])
    # Split the minutes and the clock format ("AM" or "PM")
    start_min_list = start_list[1].split()
    result_min = int(start_min_list[0]) + int(duration_list[1])
    count = 1
    while result_hour >= 12:
        result_hour -= 12

        if day == "" or "day" in day:
            if count == 1:
                day = "(next day)"

            else:
                day = "(" + str(count) + " " + "days later)"

            count += 1

        elif day in dict_day:
            day_count = dict_day[day] + 1
            # Checks if day_count is out of the index of the dictionary
            if day_count > len(dict_day):
                day_count = 1

            day = dict[day_count]

        if start_min_list[1] == "AM":
            start_min_list[1] = "PM"

        else:
            start_min_list[1] = "AM"

    result = str(result_hour) + ":" + str(result_min) + " " + start_min_list[1] + " " + day
    return result



