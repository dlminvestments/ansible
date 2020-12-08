from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


def testtest(data):
    return data == 'from_user2'


class TestModule(object):
    @staticmethod
    def tests():
        return {
            'testtest2': testtest
        }
