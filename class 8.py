class Vehicle:
    def start_engine(self):
        raise NotImplementedError("Subclasses must implement this method")

    def stop_engine(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

Car=Car()
Car.start_engine()
