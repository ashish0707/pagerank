import abc


class Searcher(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def merge_list(self, list1, list2):
        """Retrieve data from the input source and return an object."""
        return

