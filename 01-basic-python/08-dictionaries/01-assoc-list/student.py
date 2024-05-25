class AssocList:
    def __init__(self):
        self.__items = []

    def __setitem__(self, key, value):
        index = self.__find_key_index(key)
        if index == -1:
            self.__items.append([key, value])
        else:
            self.__items[index][1] = value

    def __getitem__(self, key):
        index = self.__find_key_index(key)
        if index == -1:
            return KeyError()
        else:
            return self.__items[index][1]
        
    def __contains__(self, key):
        return self.__find_key_index(key) != -1
    
    def __len__(self):
        return len(self.__items)
    
    def __find_key_index(self, key):
        for i, (k, _) in enumerate(self.__items):
            if k == key:
                return i
        
        return -1
    
    @property
    def keys(self):
        return [k for k, _ in self.__items]
    
    @property
    def values(self):
        return [v for _, v in self.__items]
    

# Create an instance of AssocList
cities_by_country = AssocList()

# Add cities to the associative list
cities_by_country['USA'] = 'New York'
cities_by_country['USA'] = 'Los Angeles'
cities_by_country['USA'] = 'Chicago'
cities_by_country['UK'] = 'London'
cities_by_country['UK'] = 'Manchester'
cities_by_country['France'] = 'Paris'
cities_by_country['Germany'] = 'Berlin'
cities_by_country['Germany'] = 'Munich'

# Access cities by country
print("Cities in USA:", cities_by_country['USA'])
print("Cities in UK:", cities_by_country['UK'])
print("Cities in France:", cities_by_country['France'])

# Check if certain countries are present
print("Is USA in the list?", 'USA' in cities_by_country)
print("Is Japan in the list?", 'Japan' in cities_by_country)

# Get all countries and cities
print("Countries:", cities_by_country.keys)
print("Cities:", cities_by_country.values)

# Get the total number of countries
print("Total number of countries:", len(cities_by_country))