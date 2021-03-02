from unittest import TestCase
from handlers import pulls


class TestPrime(TestCase):

    def setUp(self):
        """Init"""

    def test_get_pulls(self):
        open_pull = {'num': 92, 'title': 'Homework6: Volha Huryna',
                     'link': 'https://github.com/alenaPy/devops_lab/pull/92'}
        self.assertEqual(pulls.get_pulls('open').count(open_pull), 1)

        closed_pull = {'num': 1, 'title': 'Test PR',
                       'link': 'https://github.com/alenaPy/devops_lab/pull/1'}
        self.assertNotEqual(pulls.get_pulls('closed').count(closed_pull), 0)

        need_work_pull = {'num': 67, 'title': 'Homevork3: Vitali Lukashevich',
                          'link': 'https://github.com/alenaPy/devops_lab/pull/67'}
        self.assertEqual(pulls.get_pulls('needs work').count(need_work_pull), 1)

        accepted_pull = {'num': 93, 'title': 'Homework6: Aliaksandr Mukhitdzinau',
                         'link': 'https://github.com/alenaPy/devops_lab/pull/93'}
        self.assertNotEqual(pulls.get_pulls('accepted').count(accepted_pull), 0)

    def tearDown(self):
        """Finish"""
