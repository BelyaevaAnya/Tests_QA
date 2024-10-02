from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        objRunner = Runner('Forest')
        for i in range(10):
            objRunner.walk()
        self.assertEqual(objRunner.distance, 50)

    def test_run(self):
        objRunner = Runner('Forest')
        for i in range(10):
            objRunner.run()
        self.assertEqual(objRunner.distance, 100)

    def test_challange(self):
        objRunner1 = Runner('Forest')
        objRunner2 = Runner('Gabi')
        for i in range(10):
            objRunner1.walk()
            objRunner2.run()
        self.assertNotEqual(objRunner1.distance, objRunner2.distance)

    def test_false_run(self):
        objRunner = Runner('Forest')
        for i in range(10):
            objRunner.run()
        self.assertEqual(objRunner.distance, 2)


if __name__ == '__main__':
    unittest.main()
