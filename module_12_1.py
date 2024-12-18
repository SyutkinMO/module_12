# ----------------------"Простые Юнит-Тесты"----------------------


import unittest


class Runner:
    """Код для тестирования"""

    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    """класс RunnerTest, наследуемый от TestCase из модуля unittest. """

    def test_walk(self):
        """test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk
            у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50."""
        Runner_1 = Runner('Den')
        for i in range(10):
            Runner_1.walk()
        self.assertEqual(Runner_1.distance, 50)

    def test_run(self):
        """test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run
            у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100."""
        Runner_2 = Runner('Ivan')
        for i in range(10):
            Runner_2.run()
        self.assertEqual(Runner_2.distance, 100)

    def test_challenge(self):
        """test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
            Далее 10 раз у объектов вызываются методы run и walk соответственно.
            Т.к. дистанции должны быть разными, используйте метод assertNotEqual,
            чтобы убедится в неравенстве результатов."""
        Runner_ = Runner('Fedor')
        Walker_ = Runner('Kirill')
        for i in range(10):
            Runner_.run()
            Walker_.walk()
        self.assertNotEqual(Runner_.distance, Walker_.distance)


if __name__ == "__main__":
    unittest.main()
