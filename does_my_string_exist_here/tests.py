from django.test import TestCase

from views import get_result


class GetResultTests(TestCase):

    def test_method_finds_index_occurences(self):

        textToSearch = 'Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!'
        peter = 'Peter'
        peter_lowercase = 'peter'
        pick = 'pick'
        pi = 'pi'
        z = 'z'
        peterz = 'Peterz'

        self.assertEqual(get_result(textToSearch, peter), (1, 20, 75))
        self.assertEqual(get_result(textToSearch, peter_lowercase), (1, 20, 75))
        self.assertEqual(get_result(textToSearch, pick), (30, 58))
        self.assertEqual(get_result(textToSearch, pi), (30, 37, 43, 51, 58))
        self.assertEqual(get_result(textToSearch, z), ())
        self.assertEqual(get_result(textToSearch, peterz), ())
