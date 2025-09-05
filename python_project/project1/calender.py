def leapyear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def getDayOfWeek(year, month):
    # Zeller's Congruence algorithm for Gregorian calendar
    q = 1  # Day of month
    m = month
    y = year
    if m < 3:
        m += 12
        y -= 1
    k = y % 100
    j = y // 100
    h = (q + (13 * (m + 1)) // 5 + k + (k // 4) + (j // 4) + 5 * j) % 7
    # 0=Saturday, 1=Sunday, ..., 6=Friday
    # We want 0=Sunday, ..., 6=Saturday
    return (h + 6) % 7

y = int(input("Enter year: "))
months = [
    ("January", 31),
    ("February", 29 if leapyear(y) else 28),
    ("March", 31),
    ("April", 30),
    ("May", 31),
    ("June", 30),
    ("July", 31),
    ("August", 31),
    ("September", 30),
    ("October", 31),
    ("November", 30),
    ("December", 31)
]

for idx, (month, days) in enumerate(months, 1):
    print(f"\n\n\t\t{month} {y}")
    print("Sun\tMon\tTue\tWed\tThu\tFri\tSat")
    start_day = getDayOfWeek(y, idx)
    print("\t" * start_day, end="")

    for day in range(1, days + 1):
        print(f"{day}\t", end="")
        if (start_day + day) % 7 == 0:
            print()
    print()