from datetime import datetime, timedelta

def simulate_trip(route_data, total_distance, current_cycle_used):
    duty_status_log = []
    log_sheets = []
    time = 0  # Start time in hours
    position = 0  # Distance traveled in miles
    driving_time = 0  # Cumulative driving time in current duty day
    on_duty_time = 0  # Total on-duty time in current duty day
    time_since_break = 0  # Time since last break
    speed = 60  # Average speed in mph
    total_duration = route_data['duration'] / 3600  # Total driving time in hours
    
    # Past 7 days: assume even distribution of current_cycle_used
    past_hours = [current_cycle_used / 7] * 7
    daily_hours = []

    def check_70_hour_limit():
        last_8_days = past_hours[-7:] + daily_hours
        return sum(last_8_days) < 70

    current_day = 0
    day_start_time = 0
    daily_grid = []

    while position < total_distance:
        if not daily_hours or time >= day_start_time + 24:
            # Start new day
            if daily_hours:
                day_hours = sum(e['duration'] for e in daily_grid if e['status'] in ['driving', 'on_duty_not_driving'])
                daily_hours.append(day_hours)
                log_sheets.append({
                    "date": (datetime.today() + timedelta(days=current_day-1)).strftime('%Y-%m-%d'),
                    "grid": daily_grid
                })
            current_day += 1
            day_start_time = (current_day - 1) * 24
            daily_grid = [{"start": day_start_time, "end": time, "status": "off_duty"}]
            driving_time = 0
            on_duty_time = 0
            time_since_break = 0

            if not check_70_hour_limit():
                off_time = time
                while not check_70_hour_limit():
                    time += 1
                    if time >= day_start_time + 24:
                        daily_hours.append(0)
                        log_sheets.append({
                            "date": (datetime.today() + timedelta(days=current_day-1)).strftime('%Y-%m-%d'),
                            "grid": daily_grid
                        })
                        current_day += 1
                        day_start_time = (current_day - 1) * 24
                        daily_grid = [{"start": day_start_time, "end": time, "status": "off_duty"}]
                duty_status_log.append({"time": off_time, "status": "off_duty", "duration": time - off_time})
                daily_grid.append({"start": off_time, "end": time, "status": "off_duty"})

        # Start driving
        if on_duty_time == 0:
            duty_status_log.append({"time": time, "status": "on_duty_not_driving"})
            daily_grid.append({"start": time, "end": time + 0.5, "status": "on_duty_not_driving", "duration": 0.5})
            time += 0.5
            on_duty_time += 0.5

        remaining_distance = total_distance - position
        time_to_next_stop = min(1000 - (position % 1000), remaining_distance) / speed if position % 1000 != 0 else remaining_distance / speed
        time_to_break = 8 - time_since_break if time_since_break < 8 else 0
        time_to_end_day = min(14 - on_duty_time, 11 - driving_time)

        next_event_time = min(time_to_next_stop, time_to_break, time_to_end_day, total_duration - (position / speed))


        if next_event_time > 0:
            duty_status_log.append({"time": time, "status": "driving"})
            daily_grid.append({"start": time, "end": time + next_event_time, "status": "driving", "duration": next_event_time})
            position += next_event_time * speed
            driving_time += next_event_time
            on_duty_time += next_event_time
            time_since_break += next_event_time
            time += next_event_time

        if time_since_break >= 8:
            duty_status_log.append({"time": time, "status": "off_duty", "location": route_data['geometry'][int(len(route_data['geometry']) * (position / total_distance))], "duration": 0.5})
            daily_grid.append({"start": time, "end": time + 0.5, "status": "off_duty", "duration": 0.5})
            time += 0.5
            on_duty_time += 0.5
            time_since_break = 0
        elif position % 1000 >= 999 or position >= total_distance:
            event_type = "fueling" if position < total_distance else ("pickup" if position <= route_data['legs'][0]['distance'] / 1609.34 else "dropoff")
            duration = 0.5 if event_type == "fueling" else 1.0
            duty_status_log.append({"time": time, "status": "on_duty_not_driving"})
            daily_grid.append({"start": time, "end": time + duration, "status": "on_duty_not_driving", "duration": duration})
            time += duration
            on_duty_time += duration
        elif driving_time >= 11 or on_duty_time >= 14:
            duty_status_log.append({"time": time, "status": "off_duty", "location": route_data['geometry'][int(len(route_data['geometry']) * (position / total_distance))], "duration": 10})
            daily_grid.append({"start": time, "end": time + 10, "status": "off_duty", "duration": 10})
            time += 10

    # Finalize last day
    if daily_grid:
        day_hours = sum(e['duration'] for e in daily_grid if e['status'] in ['driving', 'on_duty_not_driving'])
        daily_hours.append(day_hours)
        log_sheets.append({
            "date": (datetime.today() + timedelta(days=current_day-1)).strftime('%Y-%m-%d'),
            "grid": daily_grid
        })

    return duty_status_log, log_sheets