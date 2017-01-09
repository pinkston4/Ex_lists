planet_list = ["Mercury", "Mars"]
planet_list.append('Jupiter')
planet_list.append('Saturn')
planet_list.extend(['Neptune', 'Uranus'])
planet_list.insert(1, 'venus')
planet_list.insert(2, 'earth')
planet_list.append('pluto')
print(planet_list)

sl = slice(4,8)
rocky_planets = planet_list[sl]
print(rocky_planets)

del planet_list[8]
print(planet_list)