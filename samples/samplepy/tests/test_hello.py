import unittest
import json
import os
from mock import patch, MagicMock

from testfixtures import compare, Replacer


def data_path(filename):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)


@unittest.skip
class TestComplexDictCompare(unittest.TestCase):
    maxDiff = None

    def test_dict_compare_1(self):
        json1 = json.loads(open(data_path('twitter-1.json')).read())
        json2 = json.loads(open(data_path('twitter-2.json')).read())

        self.assertEqual(json1, json2)

    def test_dict_compare_2(self):
        json1 = json.loads(open(data_path('twitter-1.json')).read())
        json2 = json.loads(open(data_path('twitter-2.json')).read())

        compare(json1, json2)


@unittest.skip
class TestSimpleDictCompare(unittest.TestCase):

    def test_simple_dict_compare_1(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        dict2 = {'a': 1, 'b': 1, 'c': 3, 'd': 5}

        self.assertEqual(dict1, dict2)

    def test_simple_dict_compare_2(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        dict2 = {'a': 1, 'b': 1, 'c': 3, 'd': 5}

        compare(dict1, dict2)


class RealClassA(object):
    def say(self):
        return self.__class__.__name__


class RealClassB(object):
    def say(self):
        return self.__class__.__name__


@unittest.skip
class TestSimpleMock(unittest.TestCase):

    def test_mock(self):
        # Python 2.7+
        with patch('test_hello.RealClassA') as mock_a, patch('test_hello.RealClassB') as mock_b:
            instance_a = RealClassA()
            instance_b = RealClassB()

            instance_a.say.return_value = 'FakeClassA'
            instance_b.say.return_value = 'FakeClassB'

            self.assertEqual(instance_a.say(), 'FakeClassA')
            self.assertEqual(instance_b.say(), 'FakeClassB')

    def test_testfixture_replacer(self):
        with Replacer() as r:
            r.replace('test_hello.RealClassA', MagicMock())
            r.replace('test_hello.RealClassB', MagicMock())

            instance_a = RealClassA()
            instance_b = RealClassB()

            instance_a.say.return_value = 'FakeClassA'
            instance_b.say.return_value = 'FakeClassB'

            self.assertEqual(instance_a.say(), 'FakeClassA')
            self.assertEqual(instance_b.say(), 'FakeClassB')


@unittest.skip
class TestMockXUnit(unittest.TestCase):
    def setUp(self):
        self.patcher_a = patch('test_hello.RealClassA', spec=True)
        self.patcher_b = patch('test_hello.RealClassB', spec=True)

        self.mock_a = self.patcher_a.start()
        self.mock_b = self.patcher_b.start()

    def tearDown(self):
        self.patcher_a.stop()
        self.patcher_b.stop()

    def test_mock(self):
        instance_a = RealClassA()
        instance_b = RealClassB()

        instance_a.say.return_value = 'FakeClassA'
        instance_b.say.return_value = 'FakeClassB'

        self.assertEqual(instance_a.say(), 'FakeClassA')
        self.assertEqual(instance_b.say(), 'FakeClassB')


class TestReplacerXUnit(unittest.TestCase):
    def setUp(self):
        self.replacer = Replacer()

        self.mock_a = MagicMock()
        self.mock_b = MagicMock()

        self.replacer.replace('test_hello.RealClassA', self.mock_a)
        self.replacer.replace('test_hello.RealClassB', self.mock_b)

    def tearDown(self):
        self.replacer.restore()

    def test_mock(self):
        instance_a = RealClassA()
        instance_b = RealClassB()

        instance_a.say.return_value = 'FakeClassA'
        instance_b.say.return_value = 'FakeClassB'

        self.assertEqual(instance_a.say(), 'FakeClassA')
        self.assertEqual(instance_b.say(), 'FakeClassB')
