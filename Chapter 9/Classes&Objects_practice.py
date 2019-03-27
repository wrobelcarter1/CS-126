                                                            # Carter Wrobel
                                                            # CS ID: 186
                                                            # Section 1
                                                            # 11/15/17
'''
Classes and objects worksheet part 2
'''
'''
class MutantTracker():
    count = 0
    def __init__(self,num):
        self.count = num
        MutantTracker.count += 1

    @classmethod
    def reset_count(cls):
            cls.count = 0

# Problem 13
mt1 = MutantTracker(1)
mt2 = MutantTracker(2)
x = mt1.count
print(x)
# 1

# Problem 14
mt3 = MutantTracker(3)
mt4 = MutantTracker(4)
x = MutantTracker.count
print(x)
# 4

# Problem 15
MutantTracker.reset_count()
x = MutantTracker.count
print(x)
# 0

# Problem 16
mt5 = MutantTracker(5)
x = MutantTracker.count
print(x)
# 1


class Automobile():
    def is_mobile(self):
        return True

class SportsCar(Automobile):
    def __init__(self, top_speed):
        self.top_speed = top_speed
    def is_sports_car(self):
        if self.top_speed > 176:
            return True
        else:
            return "Not quite"

class Porshe(SportsCar):
    pass

# Problem 17
cayman = Porshe(175)
x = cayman.is_sports_car()
print(x)
# "Not quite"

# Problem 18
gt3 = Porshe(195)
x = gt3.is_sports_car()
print(x)
# True

# Problem 19
malibu = Automobile()
x = malibu.is_mobile()
print(x)
# True

# Problem 20
malibu = Automobile()
x = malibu.is_sports_car()
print(x)
# AttributeError: 'Automobile' object has no attribute 'is_sports_car'
'''


class Courses():

    def __init__(self, name, credits, start, end):
        self.name = name
        self.credits = credits
        self.start_time = start
        self.end_time = end


'''
    def overlaps(self, other):
        if self._daysOVerlap(other):
            return self._timesOverlap(other):
        else:
            return False
    def _daysOverlap(self, other):
        is self._days.intersection(other._days):
            return True
        else:
            return False
        
    def _timesOverlap(self, other):
        self_start = self._getMinutes(self._start_time)
        self_end = self._getMinutes(self._end_time)
        other_start = other._getMinutes(other._start_time)
        other_end = other._getMinutes(other._end_time)

        if self_start <=
'''



    def get_name(self):
        return self.name

    def get_credits(self):
        return self.credits

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time
    

        






















