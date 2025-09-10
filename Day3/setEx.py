

def clean_list(lst):
    """Normalize case and remove duplicates"""
    return set(email.strip().lower() for email in lst)


day1 = ["Alice@Gmail.com", "bob@yahoo.com", "Charlie@outlook.com", "alice@gmail.com"]
day2 = ["BOB@yahoo.com", "david@gmail.com", "alice@gmail.com", "Eve@Yahoo.com"]
day3 = ["charlie@outlook.com", "eve@yahoo.com", "frank@gmail.com", "alice@gmail.com"]
day1_clean = clean_list(day1)
day2_clean = clean_list(day2)
day3_clean = clean_list(day3)
all_unique = day1_clean | day2_clean | day3_clean
all_three = day1_clean & day2_clean & day3_clean
exactly_one = (day1_clean ^ day2_clean ^ day3_clean) - all_three


day1_day2 = day1_clean & day2_clean
day2_day3 = day2_clean & day3_clean
day1_day3 = day1_clean & day3_clean

print("\n===== Workshop Attendance Report =====")
print(f"Total unique attendees: {len(all_unique)}")
print(sorted(all_unique))

print(f"\nAttendees who attended ALL 3 days ({len(all_three)}):")
print(sorted(all_three))

print(f"\nAttendees who attended EXACTLY 1 day ({len(exactly_one)}):")
print(sorted(exactly_one))

print("\nPairwise overlaps:")
print(f"Day1 & Day2: {len(day1_day2)} -> {sorted(day1_day2)}")
print(f"Day2 & Day3: {len(day2_day3)} -> {sorted(day2_day3)}")
print(f"Day1 & Day3: {len(day1_day3)} -> {sorted(day1_day3)}")
