import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.Usein = Runner('Усэйн', 10)
        self.Andrew = Runner('Андрей', 9)
        self.Nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_result.values():
            print({place: str(runner) for place, runner in result.items()})

    def test_Usein_Nik(self):
        tournament = Tournament(90, self.Usein, self.Nik)
        result = tournament.start()
        TournamentTest.all_result['test_Usain_Nik'] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

    def test_Andrew_Nik(self):
        tournament = Tournament(90, self.Andrew, self.Nik)
        result = tournament.start()
        TournamentTest.all_result['test_Anrew_Nik'] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

    def test_Usein_Andrew_Nik(self):
        tournament = Tournament(90, self.Usein, self.Andrew, self.Nik)
        result = tournament.start()
        TournamentTest.all_result['test_Usain_Anrew_Nik'] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

if __name__ == "__main__":
    unittest.main()








