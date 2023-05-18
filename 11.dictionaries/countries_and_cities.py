countries = {}

n = int(input())
for _ in range(n):
    country, *cities = input().split()
    for city in cities:
        countries[city] = country

m = int(input())
for _ in range(m):
    city = input()
    country = countries.get(city, "Not found")
    print(country)
