class DataTree(object):
    """ A simple class to organize data in a branching order
        Every object in data_tree is an item.

        Attributes:
            data_array (list): the list of data to structure as a tree
            structure (kwargs): the structure type of the tree as a string.
                the default is set to 'flattened' or 'f'.
            tree (dict): the organized data as a tree in a dictionary.
                the keys represent the branches and the values are the data
                inside every branch in the data tree.

        Methods:
            flip_matrix:
            tree_statistics:
            flatten:
            graft:
            shift_list:
            unflatten:
            branch:
            construct_path:
            entwine:
            weave:
            partition:
    """

    def __init__(self, data_array, structure='flattened'):
        self._data_array = data_array
        self._structure = structure
        self.tree = {}

        while self._data_array is not None:
            if self._structure == 'f' or self._structure == 'flattened':
                self.path_index = 0
                self.tree[self.path_index] = data_array
            elif self._structure == 'g' or self._structure == 'grafted':
                for index, item in enumerate(data_array):
                    self.path_index = index
                    self.tree[self.path_index] = item
            else:
                self.path_index = 0
                self.tree[self.path_index] = data_array
            break

    def __str__(self):
        return 'class -> DataTree(data_array = ' + str([i for i in self._data_array]) \
               + ', ' + 'structure = ' + '"' + str(self._structure) + '"' + ') ' + '\n' \
               + 'branch = ' + str(self.tree) + '\n' + 'statistics = ' + str(self.tree_statistics())

    def flip_matrix(self):
        pass

    def tree_statistics(self) -> dict:
        """ Get statistics regarding a data tree

            returns (dict): a dictionary containing a list of `paths` representing
            each branch, list of `length` of each branch, and the number of the
            existing branches in the data tree.
        """
        length = []
        paths = []
        statistics = {}
        for index, keys in enumerate(self.tree):
            paths.append(index)
            statistics['paths'] = paths

            if self._structure == 'f' or self._structure == 'flattened':
                length.append(len(self.tree[index]))
                statistics['length'] = length
                statistics['items'] = length[0]

            elif self._structure == 'g' or self._structure == 'grafted':
                length.append(len(list([self.tree[index]])))
                statistics['length'] = length
                statistics['items'] = sum([i for i in length])

            count = index + 1
            statistics['count'] = count

        return statistics

    def flatten(self):
        """ Returning a dictionary that contains all the items in the array list
            as the value and `0` as the only key in the dictionary
        """
        return DataTree(self._data_array, structure='f')

    def graft(self):
        """ Returning a dictionary that contains each of the items in
            the array list as a value in a corresponding key in the dictionary
        """
        return DataTree(self._data_array, structure='g')

    def shift_list(self, offset=1, wrap=False, structure='flattened'):

        if wrap is False:
            if offset <= len(self._data_array):
                return self._data_array[offset:]
            else:
                return list()
        else:
            shifted_array = []
            for i in range(len(self._data_array)):
                shifted_array.insert((i - offset), self._data_array[i])
            if structure == 'f' or structure == 'flattened':
                return DataTree(shifted_array)
            elif structure == 'g' or structure == 'grafted':
                return DataTree(shifted_array, structure='g')
            else:
                print("Please specify a valid `structure` choose from "
                      "('flattened', or 'grafted')")
                return None

    def unflatten(self, guide):
        pass

    def branch(self, path_address=None) -> dict:
        """
        Select a branch from the data tree with the specified path
        :param path_address: The value to select the branch from
        :return: A dictionary representing the branch
        """
        try:
            return {path_address: self.tree[path_address]}
        except KeyError:

            print("The path does not exist in the tree, try a value "
                  "between {0} and {1}".format(0, len(self.tree) - 1))

    def construct_path(self):
        pass

    def entwine(self, *branch: dict) -> dict:
        """
        Entwine the specified branches and create a list of data
        branches

        :param branch: The dictionaries representing data branches to
            merge into the list
        :return: A dictionary of dictionaries representing the branching
            tree structure.
        """
        ent_list = [self.tree, *branch]
        ent_dict = dict()
        for index, item in enumerate(ent_list):
            ent_dict[index] = item
        return ent_dict

    def partition(self):
        pass


def weave(*data_array, pattern: list):
    data_list = [*data_array]
    woven_list = [data_list[i] for i in pattern]
    return woven_list


def main():
    data = [str(i * i) for i in range(5)]
    data_2 = ['Hi', "Javid", 1, 2, 3]

    second_tree = DataTree(data, structure='f')
    # print(second_tree.tree)
    # print(type(second_tree.tree))
    # print(second_tree.shift_list(offset=4, wrap=True, structure='f'))
    # print(id(second_tree.shift_list(1)))
    # print(id(second_tree.tree))

    third_tree = DataTree(data_2, structure='g')
    # print(third_tree.tree)
    # print(second_tree.branch(path_address=1))
    # print(second_tree.flatten())
    g = second_tree.graft()
    print(g.tree_statistics())
    # ent = second_tree.entwine(second_tree.tree, third_tree.tree, {1: "1"})
    print(second_tree.__str__())
    # for key in ent:
    #     print(ent[key])
    # woven_data = weave(second_tree.tree, third_tree.tree, pattern=[1, 0])
    # print(woven_data)

    numb = [i * 2 for i in range(1, len(data) + 1)]


if __name__ == '__main__':
    main()
