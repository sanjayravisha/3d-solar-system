from solar_system import SolarSystem, Sun, Planet

solarsystem = SolarSystem(400)

suns = (
    Sun(solarsystem, position=(40, 40, 40), velocity=(6, 0, 6)),
    Sun(solarsystem, position=(-40, -40, 40), velocity=(-6, 0, -6))
)
planets = (
    Planet(solarsystem, 10, position=(100, 100, 0), velocity=(0, 5.5, 5.5)),
    Planet(solarsystem, 20, position=(0, 0, 0), velocity=(-11, 11, 0))
)

while True:
    solarsystem.calculate_all_body_interactions()
    solarsystem.update_all()
    solarsystem.draw_all()