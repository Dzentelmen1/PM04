import unittest

def validate_component_name(name):
    return len(name) > 0 and name[0].isupper()

class TestMaintenance(unittest.TestCase):
    def test_name_valid(self):
        # Проверка, что имя компонента начинается с заглавной буквы
        self.assertTrue(validate_component_name("Database"))
        self.assertFalse(validate_component_name("db"))

if __name__ == '__main__':
    unittest.main()
