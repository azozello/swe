from collections import deque


def find_available_time(p1_meeting, p2_meeting, p1_hours, p2_hours, time_needed) -> [[float]]:
    time_slots = []

    common_hours = [max(p1_hours[0], p2_hours[0]), min(p1_hours[1], p2_hours[1])]

    deq_1 = get_available_time_queue(common_hours, p1_meeting, time_needed)
    deq_2 = get_available_time_queue(common_hours, p2_meeting, time_needed)

    first_temp_time = deq_1.pop()
    second_temp_time = deq_2.pop()

    while len(deq_1) > 0 or len(deq_2) > 0:
        intersection = get_time_intersection(first_temp_time, second_temp_time)

        if len(intersection) > 0 and intersection[1] - intersection[0] >= time_needed:
            time_slots.append(intersection)

        if first_temp_time[1] < second_temp_time[1]:
            if len(deq_1) > 0:
                first_temp_time = deq_1.pop()
            elif len(deq_2) > 0:
                second_temp_time = deq_2.pop()

        elif second_temp_time[1] < first_temp_time[1]:
            if len(deq_2) > 0:
                second_temp_time = deq_2.pop()
            elif len(deq_1) > 0:
                first_temp_time = deq_1.pop()

    intersection = get_time_intersection(first_temp_time, second_temp_time)
    if len(intersection) > 0 and intersection[1] - intersection[0] >= time_needed:
        time_slots.append(intersection)

    return time_slots


def get_time_intersection(first_time, second_time):
    common_hours = [max(first_time[0], second_time[0]), min(first_time[1], second_time[1])]

    return common_hours if common_hours[0] < common_hours[1] else []


def get_available_time_queue(hours: [float], meetings: [[float]], desired_time: float) -> deque:
    time_slots = []

    last_end_time = hours[0]

    for m in meetings:
        temp_start, temp_end = m

        if temp_start > last_end_time and temp_start - last_end_time > desired_time:
            time_slots.append([last_end_time, temp_start])

        last_end_time = temp_end

    return deque(reversed(time_slots))


if __name__ == '__main__':
    first_person_meetings = [[9.30, 10.30], [12.00, 13.0], [16.0, 18.0]]
    first_person_working_hours = [9.0, 20.0]

    second_person_meetings = [[10.0, 11.30], [12.30, 14.30], [14.30, 15.0], [16.0, 17.0]]
    second_person_working_hours = [10.0, 18.30]

    desired_meeting_time = 0.30

    print(find_available_time(first_person_meetings, second_person_meetings,
                              first_person_working_hours, second_person_working_hours,
                              desired_meeting_time))
