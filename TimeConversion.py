def time_format(time_str):
    n = len(time_str)
    time = time_str[0:2]
    remaining = time_str[2:n-2]
    format_24 = ''
    time = int(time)
    for i in range(n):
        if time_str[i] == 'P':
            format_24 += f"{time}{remaining}"
        elif time_str[i] == 'A':
            if time == 12:
                format_24 += f"00{remaining}"
            else:
                time += 12
                format_24 += f"{time}{remaining}"
    return format_24
time_str = "07:06:00 AM"
print(time_format(time_str))



            