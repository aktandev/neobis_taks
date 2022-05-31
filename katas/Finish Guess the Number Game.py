class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if self.lives == 0:
            raise "Omae wa mo shindeiru"
        if n != self.number:
            self.lives -=1
            return False
        else:
            return True





guesser = Guesser(10, 2)
print(guesser.guess(1))
print(guesser.guess(10))
print(guesser.guess(6))
print(guesser.guess(6))