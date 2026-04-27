class NumberSeparator:
    """Transmuting numbers based on their parity"""
    def __init__(self, number_list):
        self.numbers = number_list

    def transmute_even(self):
        """Squares even numbers"""
        return [x ** 2 for x in self.numbers if x % 2 == 0]

    def transmute_odd(self):
        """Cubes odd numbers"""
        return [x ]

