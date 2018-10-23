import unittest
from city.city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    '''测试city_functions.py'''

    def test_city_country(self):
        '''能正确处理像北京 中国这样的么?'''
        city_and_country = city_country('北京', '中国')
        self.assertEqual(city_and_country, '北京 中国 人口:unknown')

if __name__ == '__main__':
    unittest.main()
