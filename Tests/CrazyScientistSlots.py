import datetime
import unittest


class TestSlots(unittest.TestCase):
    """ Тестирование функционала сущности 'РЕГИСТРАЦИЯ' """

    @classmethod
    def setUpClass(cls):
        cls.todays_date = datetime.datetime.today().strftime("%Y-%m-%d %H-%M-%S")

    def setUp(self):
        pass

    def test_001_1_slot(self):
