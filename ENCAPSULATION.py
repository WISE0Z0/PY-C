class car:
    def __init__(self,make,model,year):
        self.__make = make #private attribute
        self.__model = model
        self.__year = year
        self._is_started = False
    def start_engine(self):
        self._is_started = True
        print("engine started")
    def stop_engine(self):
        self._is_started = False
        print("engine stopped")
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    def is_engine_started(self):
        return self._is_started
my_car = car("toyota","fortuner",2020)
print("make:",my_car.get_make())
print("model:",my_car.get_model())
print("year:",my_car.get_year())

# print("make:",my_car.__make)

my_car.start_engine()
print("engine started?" ,my_car.is_engine_started())

my_car.stop_engine()
print("engine started?" ,my_car.is_engine_started())