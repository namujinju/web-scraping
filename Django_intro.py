class Car():

    def __init__(self, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$777")

    def __str__(self):
        return f"Car with {self.wheels} wheels"


class Convertible(Car):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return f"Car with no roof"


porche = Car(price="$100")
mini = Convertible(color="tomato")

print(porche.color)
print(mini.take_off())
