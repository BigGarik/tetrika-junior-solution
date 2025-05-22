import unittest
import csv
import os
from unittest.mock import patch, MagicMock
from solution import main


class TestTask2(unittest.TestCase):

    @patch('solution.requests.get')
    def test_main_success(self, mock_get):
        # Мокаем ответ API
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "query": {
                "categorymembers": [
                    {"title": "Арктический волк"},
                    {"title": "Белый медведь"},
                    {"title": "Волк"}
                ]
            }
        }
        mock_get.return_value = mock_response

        # Запускаем основную функцию
        main()

        # Проверяем, что файл создан
        self.assertTrue(os.path.exists("beasts.csv"))

        # Проверяем содержимое
        with open("beasts.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)

        expected = [["А", "1"], ["Б", "1"], ["В", "1"]]
        self.assertEqual(rows, expected)

        # Удаляем тестовый файл
        if os.path.exists("beasts.csv"):
            os.remove("beasts.csv")

    @patch('solution.requests.get')
    def test_main_with_errors(self, mock_get):
        # Мокаем ошибку
        mock_get.side_effect = Exception("Error")

        # Функция не должна падать
        try:
            main()
        except Exception:
            self.fail("main() raised Exception unexpectedly!")


if __name__ == "__main__":
    unittest.main()