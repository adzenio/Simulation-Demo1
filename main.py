
class Planet:
    def __init__ (self, name, size, distance_from_sun) :
        self.name = name
        self.size = size
        self.distance_from_sun = distance_from_sun

    def describe (self) :
        return f"Planet {self.name}: Size = {self.size} km, Distance from Sun = {self.distance_from_sun} million km"

class Galaxy:
    def __init__ (self, name) :
        self.name = name
        self.planets = []

    def add_planet (self, planet) :
        self.planets.append(planet)

    def show_planets (self) :
        return [planet.describe() for planet in self.planets]

class Universe:
    def __init__ (self, id) :
        self.id = id
        self.galaxies = {}

    def add_galaxy (self, galaxy) :
        self.galaxies[galaxy.name] = galaxy

    def list_galaxies (self) :
        return list(self.galaxies.keys())

    def show_galaxy_planets (self, galaxy_name) :
        galaxy = self.galaxies.get(galaxy_name)

        if galaxy:
            return galaxy.show_planets()
        else:
            return f"Galaxy {galaxy_name} not found."

# initialization of Universe
universe = Universe(1) # I hope there's only one universe :P. Otherwise it would be the comedy of god.

# initialization of Galaxies
milky_way = Galaxy("Milky Way") # Best Galaxy Ever
andromeda = Galaxy("Andromeda") # Foster-sibling Galaxy :HEHEHEHE

# initialization of Planets
earth = Planet("Earth", 12742, 149.6)
mars = Planet("Mars", 6779, 227.9)

milky_way.add_planet(earth)
milky_way.add_planet(mars)

universe.add_galaxy(milky_way)
universe.add_galaxy(andromeda)

# Output
print("Current Universe: #" + f"{universe.id}")
print("Galaxies:", universe.list_galaxies())
print("\nPlanets in the Milky Way:")
print("\n". join(universe.show_galaxy_planets("Milky Way")))
