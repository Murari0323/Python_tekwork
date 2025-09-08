def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    return base_fare + distance_fare

def total_trip_fare(trips):
    total = 0
    for i, d in enumerate(trips, start=1):
        fare = calculate_fare(d)
        total += fare
        print(f"Trip {i}: ${fare}")
    print("Total Fare:", f"${total}")

trips = list(map(int, input("Enter trip distances separated by space: ").split()))
total_trip_fare(trips)
