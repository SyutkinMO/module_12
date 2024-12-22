# ----------------------Методы Юнит-тестирования----------------------

import unittest

"""Класс для тестирования"""


class Runner:
    """Изменения в классе Runner:
            Появился атрибут speed для определения скорости бегуна.
            Метод __eq__ для сравнивания имён бегунов.
            Переопределены методы run и walk, теперь изменение дистанции зависит от скорости."""

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
    """Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать
    и список участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции."""

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
                    break  # скорее всего ошибка здесь

        return finishers


class TournamentTest(unittest.TestCase):
    """TournamentTest, наследованный от TestCase и его методы"""

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        """setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться
            результаты всех тестов."""
        cls.all_results = {}

    def setUp(self):
        """setUp - метод, где создаются 3 объекта: Бегун по имени Усэйн, со скоростью 10, Бегун по имени Андрей,
        со скоростью 9. Бегун по имени Ник, со скоростью 3."""
        self.Runner_1 = Runner('Усэйн', speed=10)
        self.Runner_2 = Runner('Андрей', speed=9)
        self.Runner_3 = Runner('Ник', speed=3)

    def tearDown(self):
        """метод, где выводятся all_results по очереди в столбец."""
        sorted_result = {}  # промежуточный словарик для сортированных данных результатов забегов
        for place, finisher in sorted(self.all_results.items()):
            sorted_result[place] = finisher.name
        print(sorted_result)

        """Далее методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90"""

    @unittest.skipIf(is_frozen, 'Тесты заморожены')
    def test_usain_nik(self):
        tornament = Tournament(90, self.Runner_1, self.Runner_3)
        results = tornament.start()  # У объекта класса Tournament запускается метод start, который возвращает
        # словарь в переменную all_results.
        self.all_results.clear()  # на всякий случай очищаем словарь, чтобы не было дублирований
        self.all_results.update(results)  # Метод update() используется для изменения значения имеющегося ключа.
        # Если же ключа нет, то он вместе со значением добавляется в словарь
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")  # находим ключ с максимальным значением -
        # это и есть последнее место и значение этого ключа всегда равно "Ник")

    @unittest.skipIf(is_frozen, 'Тесты заморожены')
    def test_andrey_nik(self):
        tornament = Tournament(90, self.Runner_2, self.Runner_3)
        results = tornament.start()
        self.all_results.clear()
        self.all_results.update(results)
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты заморожены')
    def test_usain_andrey_nik(self):
        tornament = Tournament(90, self.Runner_1, self.Runner_2, self.Runner_3)
        results = tornament.start()
        self.all_results.clear()
        self.all_results.update(results)
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")


if __name__ == "__main__":
    unittest.main()
