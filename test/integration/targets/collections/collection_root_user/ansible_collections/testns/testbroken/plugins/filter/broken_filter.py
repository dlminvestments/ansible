from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class FilterModule(object):

    @staticmethod
    def filters():
        return {
            'broken': lambda x: 'broken',
        }


raise Exception('This is a broken filter plugin.')
