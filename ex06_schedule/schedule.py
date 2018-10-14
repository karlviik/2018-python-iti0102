"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    with open(input_filename) as file:
        string_from_file = create_schedule_string(file.read())
    with open(output_filename, "w") as file:
        file.write(string_from_file)
    return None


def diver(length):
    """Return line of minuses with given length."""
    return "-" * length


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    regex = "(?<=[\\s(\\\\n)])(\\d{1,2})[^0-9](\\d{1,2})\\s+([a-zA-Z]+)(?![a-zA-Z])"

    timedic = {}
    for match in re.finditer(regex, input_string):
        hour = match.group(1)
        if len(hour) == 1:
            hour = "0" + hour
        minutes = match.group(2)
        if len(minutes) == 1:
            minutes = "0" + minutes
        if int(hour) > 23 or int(minutes) > 59:
            continue
        activity = match.group(3).lower()
        time = hour + ":" + minutes
        try:
            timedic[time].append(activity)
        except KeyError:
            timedic[time] = [activity]
    if len(timedic) == 0:
        lines = ["| No items found |"]
        maxtimelen = 5
        maxactslen = 6
    else:
        linecontents = []
        maxtimelen = 4
        maxactslen = 5
        for time, acts in sorted(timedic.items()):
            hour = int(time[0:2])
            if hour >= 12:
                ampm = " PM"
            else:
                ampm = " AM"
            hour = hour % 12
            if hour == 0:
                hour = 12
            timecontent = str(hour) + time[2:] + ampm
            if len(timecontent) > maxtimelen:
                maxtimelen = len(timecontent)
            tempacts = []
            actscontent = ""
            for act in acts:
                if act not in tempacts:
                    tempacts.append(act)
                    actscontent += act + ", "
            actscontent = actscontent[:-2]
            if len(actscontent) > maxactslen:
                maxactslen = len(actscontent)
            linecontents.append([timecontent, actscontent])

        lines = []
        for time, acts in linecontents:
            line = "| " + " " * (maxtimelen - len(time)) + time + " | " + acts + " " * (maxactslen - len(acts)) + " |"
            lines.append(line)
    linelen = maxtimelen + maxactslen + 7
    output = diver(linelen) + "\n| " + " " * (maxtimelen - 4) + "time | items" + " " * (maxactslen - 5) + " |\n" + diver(linelen) + "\n"
    for line in lines:
        output += line + "\n"
    output += diver(linelen)
    return output


if __name__ == '__main__':
    #print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst 11:00 Lorem"))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
