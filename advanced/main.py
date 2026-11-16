mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

for i in mission_route:
    print(i)


destination = input("Please enter a destination: ")
destination = destination.strip().title()

if destination in mission_route:

    print(f"{destination} is on the route.")

    destination_index = mission_route.index(destination)
    print(destination_index)

    print(f"Stops from start:{destination_index}")
    length = len(mission_route)
    print(f"Stops to end:{length-destination_index-1}")

    if destination_index + 1 < len(mission_route):
        print("Next stop:", mission_route[destination_index+1])

    else:
        print("This is the last stop on the route.")

else:
    print(f"{destination} is not on the route.")