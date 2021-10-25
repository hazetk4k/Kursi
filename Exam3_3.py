class Tomato:
    states = {
        1: "not ready",
        2: "almost ready",
        3: "pretty ready",
        4: "ready"
    }

    def __init__(self, _index):
        self.i = 0
        self._state = self.states[1]
        self._index = _index

    def grow(self):
        self.i += 1
        self._state = self.states[self.i]

    def is_ripe(self):
        if self._state == "ready":
            return "is ripe"
        else:
            return "is not ripe"


class TomatoBush:

    def __init__(self, number):
        self.list_tomato = []
        for i in range(number):
            self.list_tomato.append(Tomato(i))

    def grow_all(self):
        for i in self.list_tomato:
            i.grow()

    def ripe_all(self):
        for i in self.list_tomato:
            if i.is_ripe() == 'is ripe':
                continue
            else:
                return False
        return True

    def give_away_all(self):
        self.list_tomato.clear()


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.ripe_all():
            self._plant.give_away_all()
        else:
            print('пока не все созрели')

    @staticmethod
    def knowledge_base():
        print('А? Что? Как?')


tomatos = TomatoBush(10)
sOdovod = Gardener(name="сОдовод", plant=tomatos)
sOdovod.work()
sOdovod.work()
sOdovod.work()
print(tomatos.ripe_all())
sOdovod.harvest()
sOdovod.work()
sOdovod.harvest()
print(tomatos.list_tomato)
