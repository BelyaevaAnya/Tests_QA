from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, reason='Тесты в этом кейсе заморожены')
    def test_walk(self):
        objRunner = Runner('Forest')
        for i in range(10):
            objRunner.walk()
        self.assertEqual(objRunner.distance, 50)

    @unittest.skipIf(is_frozen, reason='Тесты в этом кейсе заморожены')
    def test_run(self):
        objRunner = Runner('Forest')
        for i in range(10):
            objRunner.run()
        self.assertEqual(objRunner.distance, 100)

    @unittest.skipIf(is_frozen, reason='Тесты в этом кейсе заморожены')
    def test_challange(self):
        objRunner1 = Runner('Forest')
        objRunner2 = Runner('Gabi')
        for i in range(10):
            objRunner1.walk()
            objRunner2.run()
        self.assertNotEqual(objRunner1.distance, objRunner2.distance)

    @unittest.skipIf(is_frozen, reason='Тесты в этом кейсе заморожены')
    def test_false_run(self):
        objRunner = Runner('Forest')
        for i in range(10):
            objRunner.run()
        self.assertEqual(objRunner.distance, 2)


import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print("Полные результаты всех тестов:")
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")  # Выводим результаты как есть

    @unittest.skipIf(is_frozen, reason='Тесты в этом кейсе заморожены')
    def test_race_usain_and_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)  # Передаем участников в список
        result = tournament.start()
        # Преобразуем результаты в имена бегунов
        self.all_results['Usain vs Nick'] = {rank: self.get_runner_name(name) for rank, name in result.items()}
        # Проверяем, что последний бегун - Ник
        self.assertTrue(self.all_results['Usain vs Nick'][max(result.keys())] == "Ник")

    @unittest.skipIf(is_frozen, reason='Тесты в этом кейсе заморожены')
    def test_race_andrey_and_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)  # Передаем участников в список
        result = tournament.start()
        # Преобразуем результаты в имена бегунов
        self.all_results['Andrey vs Nick'] = {rank: self.get_runner_name(name) for rank, name in result.items()}
        # Проверяем, что последний бегун - Ник
        self.assertTrue(self.all_results['Andrey vs Nick'][max(result.keys())] == "Ник")

    @unittest.skipIf(is_frozen, reason='Тесты в этом кейсе заморожены')
    def test_race_all(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)  # Передаем участников в список
        result = tournament.start()
        # Преобразуем результаты в имена бегунов
        self.all_results['Usain, Andrey, Nick'] = {rank: self.get_runner_name(name) for rank, name in result.items()}
        # Проверяем, что последний бегун - Ник
        self.assertTrue(self.all_results['Usain, Andrey, Nick'][max(result.keys())] == "Ник")

    def get_runner_name(self, runner_object):
        """ Возвращает имя бегуна по объекту. """
        # Здесь мы предположим, что runner_object - это объект Runner
        return runner_object.name if isinstance(runner_object, Runner) else runner_object


if __name__ == '__main__':
    unittest.main()
