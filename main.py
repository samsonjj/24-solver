from typing import Union, List, Tuple
from itertools import combinations
import sys

add = ("+", lambda x, y: x + y)
sub = ("-", lambda x, y: x - y)
mul = ("*", lambda x, y: x * y)
div = ("/", lambda x, y: x / y if y != 0 else 10000)

operators = [add, sub, mul, div]


def get_val(x: Union['Operation', int]):
    return x.value if isinstance(x, Operation) else x


class Operation:
    def __init__(
        self,
        left: Union['Operation', int],
        operator: Tuple[any, str],
        right: Union['Operation', int]
    ):
        self.operator = operator
        self.left = left
        self.right = right
        self.value = self.compute()

    def compute(self):
        return self.operator[1](get_val(self.left), get_val(self.right))

    def __str__(self):
        return '(' + str(self.left) + self.operator[0] + str(self.right) + ')'


def solve(nums: List[Union[Operation, int]]):
    if len(nums) == 1:
        if nums[0].value == 24:
            print(nums[0])
        else:
            return
    for (i, j) in combinations(range(len(nums)), 2):
        for operator in operators:
            operation = Operation(nums[i], operator, nums[j])
            if operation.value - int(operation.value) != 0:
                continue
            new_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
            new_nums.append(operation)
            solve(new_nums)


if __name__ == "__main__":
    nums = [int(x) for x in sys.argv[1:]]
    print(nums)
    solve(nums)