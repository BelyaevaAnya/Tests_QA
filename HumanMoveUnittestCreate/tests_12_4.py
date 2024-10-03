# Логирование
from rt_with_exceptions import Runner
import logging
import unittest
import traceback

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log'
                    , format='%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s', encoding='UTF-8')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            beg1 = Runner("Вася", speed=-3)
            logging.info("test_walk выполнен успешно")
        except Exception:
            logging.warning("Неверная скорость для Runner")
            logging.warning(traceback.format_exc())

    def test_run(self):
        try:
            beg2 = Runner(2)
            logging.info("test_run выполнен успешно")
        except Exception:
            logging.warning("Неверный тип данных для объекта Runner")
            logging.warning(traceback.format_exc())


if __name__ == '__main__':
    unittest.main()
