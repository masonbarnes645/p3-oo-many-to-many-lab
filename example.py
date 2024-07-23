class NationalPark:

    def __init__(self, name):
        self.name = name

    def trips(self):
        return [trip for trip in  Trip.all if trip.national_park is self]

    def visitors(self):
        return list({trip.visitor for trip in self.trips()})

    def total_visits(self):
        pass

    def best_visitor(self):
        pass


class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, date):
        if type(date) is not str:
            raise TypeError("Dates must be of type string")
        elif len(date) < 7:
            raise ValueError("Dates must have at least 7 characters")
        self._start_date = date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, date):
        if type(date) is not str:
            raise TypeError("Dates must be of type string")
        elif len(date) < 7:
            raise ValueError("Dates must have at least 7 characters")
        self._end_date = date

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise TypeError("must be an instance of Visitor class")

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise TypeError("must be an instance of NationalPark class")


class Visitor:

    def __init__(self, name):
        self.name = name

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]

    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})

    def total_visits_at_park(self, park):
        pass