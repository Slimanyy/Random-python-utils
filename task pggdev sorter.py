import random  # for the last approach
# FIRSTLY CHECK LAST LINE OD CODE I REALISED LATE AFTER LISTENING TO VOICE INNSTRUCTIONS

tasks = [
    {'name': 'Watch ball', 'priority': 2, 'duration': 3},
    {'name': 'Test for bugs', 'priority': 3, 'duration': 2},
    {'name': 'Jogging', 'priority': 1, 'duration': 4},
    {'name': 'Sly girls', 'priority': 2, 'duration': 1},
    {'name': 'Write code', 'priority': 3, 'duration': 3},
    {'name': 'Job hunt', 'priority': 1, 'duration': 2},
    {'name': 'Shop for groceries', 'priority': 3, 'duration': 4},
    {'name': 'Call eleniyan', 'priority': 2, 'duration': 3},
    {'name': 'Fix a bug', 'priority': 1, 'duration': 1},
    {'name': 'Attend football training', 'priority': 3, 'duration': 2},
    {'name': 'Take a walk', 'priority': 2, 'duration': 3},
    {'name': 'Go for a walk', 'priority': 1, 'duration': 4},
    {'name': 'Read manga', 'priority': 3, 'duration': 2},
    {'name': 'Watch anime report', 'priority': 2, 'duration': 3},
    {'name': 'Attend a meeting', 'priority': 1, 'duration': 1},
    {'name': 'Clean the house', 'priority': 3, 'duration': 4},
    {'name': 'Take a break', 'priority': 2, 'duration': 3},
]

# priority : high =3 , medium=2 and low =1


def Slim_Scheduler(tasks):
    sorted_tasks = sorted(
        tasks, key=lambda task: task['priority'], reverse=True)
    schedule = [[] for _ in range(24)]

    for task in sorted_tasks:
        # feel like there should be a maximum hour spent on a task, so i made it 6hours
        duration = min(task['duration'], 6)

        # the earliest time a task can be scheduled
        start_hour = None
        # 12 to 5 is for sleeping, so in 24 hour format it'll be 0 to 5 in range 24
        for hour in range(5, 24 - duration + 1):
            if all(not schedule[hour + i] for i in range(duration)):
                start_hour = hour
                break

        # assign tasks in order of priority
        if start_hour is not None:
            for hour in range(start_hour, start_hour + duration):
                schedule[hour].append(task['name'])

    return schedule


def print_schedule(schedule):
    for hour, tasks in enumerate(schedule):
        print(f"Hour {hour:02d}: {', '.join(tasks)}")


schedule = Slim_Scheduler(tasks)
print_schedule(schedule)

# a diff approach
print("for second function")

# this second function just added a little bit of maths to the previous function
# i added difficulty funtion too  compares the difficulty level of the current task with the previous task scheduled in each hour of the time slot. the the difficulty level of the current task must not be higher than or equal to the previous task
# all codes are explained in the previous function
# the schedule will depend on the priorities and available time slots. If tasks have longer duration or limited time slots, it may affect the scheduling and potentially result in some tasks not being scheduled.
# the maths is self explantory sha
# diifficulty is from hard to easy hard =3 easy =1 medium = 2


def Slimany_alt_schedule(tasks):
    sorted_tasks = sorted(tasks, key=lambda task: (
        task['difficulty'], task['priority']), reverse=True)
    schedule = [[] for _ in range(24)]

    for task in sorted_tasks:
        duration = task['duration']

        best_start_hour = None
        best_priority_sum = 0
        best_availability = float('inf')

        for hour in range(5, 24 - duration + 2):
            priority_sum = sum(task['priority']
                               for slot in schedule[hour:hour+duration])
            availability = sum(
                1 for slot in schedule[hour:hour+duration] if not slot)

            if availability == duration and (availability < best_availability or (availability == best_availability and priority_sum > best_priority_sum)):
                is_valid_schedule = True
                for h in range(hour, hour + duration):
                    if len(schedule[h]) > 0:
                        prev_task_difficulty = tasks.index(
                            task) if tasks.index(task) > 0 else 0
                        prev_task_difficulty -= 1
                        if tasks.index(schedule[h][0]) >= prev_task_difficulty:
                            is_valid_schedule = False
                            break
                if is_valid_schedule:
                    best_start_hour = hour
                    best_priority_sum = priority_sum
                    best_availability = availability

        if best_start_hour is not None:
            for hour in range(best_start_hour, best_start_hour + duration):
                schedule[hour].append(task['name'])

    return schedule


def print_schedule(schedule):
    for hour, tasks in enumerate(schedule):
        print(f"Hour {hour:02d}: {', '.join(tasks)}")


tasks = [
    {'name': 'Watch ball', 'priority': 2, 'duration': 3, 'difficulty': 1},
    {'name': 'Test for bugs', 'priority': 3, 'duration': 2, 'difficulty': 2},
    {'name': 'Jogging', 'priority': 1, 'duration': 4, 'difficulty': 3},
    {'name': 'Sly girls', 'priority': 2, 'duration': 1, 'difficulty': 1},
    {'name': 'Write code', 'priority': 3, 'duration': 3, 'difficulty': 2},
    {'name': 'Job hunt', 'priority': 1, 'duration': 2, 'difficulty': 3},
    {'name': 'Shop for groceries', 'priority': 3, 'duration': 4, 'difficulty': 1},
    {'name': 'Call eleniyan', 'priority': 2, 'duration': 3, 'difficulty': 2},
    {'name': 'Fix a bug', 'priority': 1, 'duration': 1, 'difficulty': 1},
    {'name': 'Attend football training',
        'priority': 3, 'duration': 2, 'difficulty': 2},
    {'name': 'Take a walk', 'priority': 2, 'duration': 3, 'difficulty': 3},
    {'name': 'Go for a walk', 'priority': 1, 'duration': 4, 'difficulty': 1},
    {'name': 'Read manga', 'priority': 3, 'duration': 2, 'difficulty': 2},
    {'name': 'Watch anime report', 'priority': 2, 'duration': 3, 'difficulty': 3},
    {'name': 'Attend a meeting', 'priority': 1, 'duration': 1, 'difficulty': 1},
    {'name': 'Clean the house', 'priority': 3, 'duration': 4, 'difficulty': 2},
    {'name': 'Take a break', 'priority': 2, 'duration': 3, 'difficulty': 3},
]

schedule = Slimany_alt_schedule(tasks)
print_schedule(schedule)


# this 3rd function is just based on randomised placing irrespective of the priority
print("3rd approach")


def random_schedule(tasks):
    random.shuffle(tasks)  # Shuffle the tasks randomly
    schedule = [[] for _ in range(24)]

    for task in tasks:
        duration = task['duration']

        best_start_hour = None
        best_availability = float('inf')

        for hour in range(5, 24 - duration + 2):
            availability = sum(
                1 for slot in schedule[hour:hour+duration] if not slot)

            if availability == duration and availability < best_availability:
                best_start_hour = hour
                best_availability = availability

        if best_start_hour is not None:
            for hour in range(best_start_hour, best_start_hour + duration):
                schedule[hour].append(task['name'])

    return schedule


def print_schedule(schedule):
    for hour, tasks in enumerate(schedule):
        print(f"Hour {hour:02d}: {', '.join(tasks)}")


tasks = [
    {'name': 'Watch ball', 'priority': 2, 'duration': 3},
    {'name': 'Test for bugs', 'priority': 3, 'duration': 2},
    {'name': 'Jogging', 'priority': 1, 'duration': 4},
    {'name': 'Sly girls', 'priority': 2, 'duration': 1},
    {'name': 'Write code', 'priority': 3, 'duration': 3},
    {'name': 'Job hunt', 'priority': 1, 'duration': 2},
    {'name': 'Shop for groceries', 'priority': 3, 'duration': 4},
    {'name': 'Call eleniyan', 'priority': 2, 'duration': 3},
    {'name': 'Fix a bug', 'priority': 1, 'duration': 1},
    {'name': 'Attend football training', 'priority': 3, 'duration': 2},
    {'name': 'Take a walk', 'priority': 2, 'duration': 3},
    {'name': 'Go for a walk', 'priority': 1, 'duration': 4},
    {'name': 'Read manga', 'priority': 3, 'duration': 2},
    {'name': 'Watch anime report', 'priority': 2, 'duration': 3},
    {'name': 'Attend a meeting', 'priority': 1, 'duration': 1},
    {'name': 'Clean the house', 'priority': 3, 'duration': 4},
    {'name': 'Take a break', 'priority': 2, 'duration': 3},
]

schedule = random_schedule(tasks)
print_schedule(schedule)


# I JUST ADDED THIS BCOS OF THE DURATION STUFF
cumulative_duration = sum(task['duration'] for task in tasks)
# YOU KNOW SAY PERSON GO SLEEP FOR LIKE 5/6 HOURS
while cumulative_duration > 18:
    task_to_remove = random.choice(tasks)
    tasks.remove(task_to_remove)
    cumulative_duration -= task_to_remove['duration']
# YOU FIT RUN THIS WHILE LOOP TO CHOSE THE TASK  FIRST AND RUN THE CODE BASED ON THOSE TASKS
print(tasks)
