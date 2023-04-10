class Musician:
    count = 0
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        Musician.count += 1

    def play_solo(self):
        if self.instrument == "guitar":
            return "face melting guitar solo"
        elif self.instrument == "bass":
            return "bom bom buh bom"
        elif self.instrument == "drums":
            return "rattle boom crash"

    def get_instrument(self):
        return self.instrument

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
        return f'Musician("{self.name}", "{self.instrument}")'
class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, 'guitar')

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, 'drums')

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, 'bass')

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

class Vocalist(Musician):
    def __init__(self, name):
        super().__init__(name, 'vocals')

    def __repr__(self):
        return f"Vocalist instance. Name = {self.name}"

class Band:
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members or []
        Band.instances.append(self)
    def add_member(self, member):
        if isinstance(member, Musician):
            self.members.append(member)

    def play_solos(self):
        solos = []
        for member in self.members:
            solo = member.play_solo()
            solos.append(solo)
        return solos
    @classmethod
    def to_list(cls):
        return cls.instances

    def __str__(self):
        return f"Band {self.name} with {len(self.members)} members."

    def __repr__(self):
        return f"Band(name='{self.name}')"



if __name__ == '__main__':
    thought = Vocalist('BlackThought')
    mark = Bassist('Mark')
    quest = Drummer('QuestLove')
    kirk = Guitarist('Kirk')

    the_roots = Band('The Roots')
    the_roots.add_member(thought)
    the_roots.add_member(mark)
    the_roots.add_member(quest)
    the_roots.add_member(kirk)

    print(the_roots)

    the_roots.play_solos()