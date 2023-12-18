"""
docstring
"""
class Quarter:
    """
    docstring
    """
    value = 25
    def in_nickels(self):
        """
        docstring
        """
        return self.value // 5


if __name__ == "__main__":
    # coin = Quarter()
    # another_coin = Quarter()
    # print(id(coin))
    # print(id(another_coin))
    quarter = Quarter()
    print(quarter.in_nickels())
