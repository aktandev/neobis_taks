class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        sum_of_crew = self.crew * 1.5
        how_low_ship = self.draft - sum_of_crew

        if how_low_ship > 20:
            return True
        else:
            return False




Titanic = Ship(15, 10)