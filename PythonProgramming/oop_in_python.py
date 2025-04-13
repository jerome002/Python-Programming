# Base class
class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self._battery_level = battery_level  # Protected attribute (encapsulation)

    def display_info(self):
        print(f"{self.brand} {self.model} - Battery: {self._battery_level}%")

    def charge(self):
        self._battery_level = 100
        print(f"{self.model} is now fully charged.")

# Subclass demonstrating inheritance and polymorphism
class SmartphoneWithStylus(Smartphone):
    def __init__(self, brand, model, battery_level, stylus_type):
        super().__init__(brand, model, battery_level)
        self.stylus_type = stylus_type

    def display_info(self):
        # Overriding to add stylus info
        print(f"{self.brand} {self.model} (Stylus: {self.stylus_type}) - Battery: {self._battery_level}%")

    def write_note(self):
        print(f"{self.model} is writing a note with the {self.stylus_type} stylus.")

# Example usage
phone1 = Smartphone("Apple", "iPhone 14", 75)
phone2 = SmartphoneWithStylus("Samsung", "Galaxy Note", 60, "S Pen")

phone1.display_info()
phone1.charge()

print()

phone2.display_info()
phone2.write_note()

