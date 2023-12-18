"""
docstring
"""
class QuarterV2:
    """
    docstring
    """
    def __init__(self):
        self.value = 25
    def to_pennies(self):
        """
        docstring
        """
        return self.value


if __name__ == "__main__":
    # coin = Quarter()
    # another_coin = Quarter()
    # print(id(coin))
    # print(id(another_coin))
    quarter = QuarterV2()
    print(quarter.value)
