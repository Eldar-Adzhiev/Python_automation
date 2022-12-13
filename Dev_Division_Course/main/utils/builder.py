

class LocationBuilder(dict):

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            return ''

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, item):
        try:
            del self[item]
        except KeyError:
            pass

    def with_country(self, country):
        self.country = country
        return self

    def with_city(self, city):
        self.city = city
        return self

    def with_street(self, street):
        self.street = street
        return self

    def with_building(self, building):
        self.building = building
        return self

    def with_zipcode(self, zipcode):
        self.zipcode = zipcode
        return self

    def build(self):
        return f'{self.zipcode}, {self.street} {self.building}, {self.city} {self.country}'
