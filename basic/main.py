mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

print("First stop:", mission_route[0])

print("Last stop:", mission_route[-1])

print("Total stops:", len(mission_route))

for i in mission_route:
    print(i)

if "Europa" in mission_route:
    print("Europa is on the route.")
