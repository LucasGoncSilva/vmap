def handle_duration(duration: str, total: int) -> list[int]:
    new_duration = 0

    if 's' in duration:
        new_duration = int(duration[:-1])

    elif 'm' in duration:
        if duration.endswith('m'):
            new_duration = int(duration[:-1]) * 60
        else:
            m, s = duration.split('m')
            new_duration = (int(m) * 60) + int(s)

    elif 'h' in duration:
        if duration.endswith('h'):
            new_duration = int(duration[:-1]) * 3600
        else:
            h, m = duration.split('h')
            new_duration = (int(h) * 3600) + (int(m) * 60)

    return [new_duration + total] * 2


def handle_stages(stages) -> list[dict[str, int | float]]:
    output = []
    total = 0

    for stage in stages:
        new_duration, total = handle_duration(stage['duration'], total)

        output.append(
            {
                'duration': new_duration,
                'users': stage['users'],
                'spawn_rate': stage['spawn_rate'],
            }
        )

    return output
