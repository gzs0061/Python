__author__ = 'Ella Seaman'


class musician():
    _name = ""
    _rating = ""
    _song = ""

    def musician(self, name, rating, song):
        self._name = name
        self._rating = rating
        self._song = song

    def display(self):
        print(self.name, self.rating, self.song)

    def matches(self, name):
        return self.name == self._name


def main(name):
    musicians = []
    counter = 0

    musicians.append(musician("John", 10, "Imagine"))
    musicians.append(musician("Paul", 9, "Listen to What the Man Said"))
    musicians.append(musician("George", 8, "Here Comes the Sun"))
    musicians.append(musician("Ringo", 7, "With a Little Help From My Friends"))

    while counter < 4:
        if musicians[counter].matches(name):
            musicians[counter].display()
            counter = counter + 1


main("George")
