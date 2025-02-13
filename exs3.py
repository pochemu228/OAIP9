class Pet():
    def init(self, name):
      self.name = name
      self.energy = 100
      self.hunger = 0
      self.happy = 100
      self.dream = 100
      self.die = False

    def feed(self, amount_food):
        if self.die:
            print(f"{self.name} питомец умер, не получится покормить")
            return
        self.hunger -= amount_food
        self.hunger = max(self.hunger, 0)
        print(f"{self.name} покормлен. Уровень голода: {self.hunger}")

    def sleep(self):
        if self.die:
            print(f"{self.name} питомец умер, не получится спать")
            return
        self.dream = 100
        self.energy += 20
        print(f"{self.name} спит. Уровень сна: {self.dream}, Energy: {self.energy}")

    def play(self, time):
        if self.die:
            print(f"{self.name} умер, не получится играть")
            return
        self_happy = min(100, self.happy + time * 10)
        self_hunger = min(100, self.hunger + time * 5)
        self_energy = min(100, self.energy + time * 15)
        self.happy = self_happy
        self.hunger = self_hunger
        self.energy = self_energy

        print(f"{self.name} играл {time} минут. Уровень счастья: {self.happy}, Голод: {self.hunger}, Энергия: {self.energy}")

    def check_statuses(self):
        if self.die:
            print(f"{self.name} умер")
            return
        if self.energy <= 0 or self.hunger >= 100 or self.happy <= 0 or self.dream <= 0:
            self.die = True
            print(f"{self.name} умер")
        else:
            print(f"Статусы питомца {self.name}: Энергия - {self.energy}, Голод - {self.hunger}, Счастье - {self.happy}, Сон - {self.dream}")
