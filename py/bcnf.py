# Counts the number of steps required to decompose a relation into BCNF.

from relation import *
from functional_dependency import *


# You should implement the static function declared
# in the ImplementMe class and submit this (and only this!) file.
# You are welcome to add supporting classes and methods in this file.
class ImplementMe:

    # Returns the number of recursive steps required for BCNF decomposition
    #
    # The input is a set of relations and a set of functional dependencies.
    # The relations have *already* been decomposed.
    # This function determines how many recursive steps were required for that
    # decomposition or -1 if the relations are not a correct decomposition.
    @staticmethod
    def DecompositionSteps(relations, fds):
        return -1

    @staticmethod
    def check_bcnf(relation, fd, fds):
        # find closure
        closure = set()
        # add LHS to to closure
        for letter in fd.left_hand_side:
            closure.add(letter)
        # ADD rhs to closure
        for r_letter in fd.right_hand_side:
            closure.add(r_letter)
        # check for BCNF
        if relation == closure:
            return 0
        # check if rhs leads to other attributes
        # fix this do it recursively
        else:
            for let in fd.right_hand_side:
                for func_d in fds:
                    if let == func_d.left_hand_side:
                        if func_d.right_hand_side not in closure:
                            closure.add(func_d.right_hand_side)
        # final BCNF check
        if relation == closure:
            return 0
        else:
            return -1
