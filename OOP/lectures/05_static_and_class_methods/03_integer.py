class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(int(float_value))

        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        result = Integer.roman_to_int(value)
        return cls(result)

    @staticmethod
    def roman_to_int(s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str) and int(value):
            return cls(int(value))

        return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))

# import unittest
#
#
# class IntegerTests(unittest.TestCase):
#     def test_basic_init(self):
#         integer = Integer(1)
#         self.assertEqual(integer.value, 1)
#
#     def test_from_float_success(self):
#         integer = Integer.from_float(2.5)
#         self.assertEqual(integer.value, 2)
#
#     def test_from_float_wrong_type(self):
#         result = Integer.from_float("2.5")
#         self.assertEqual(result, "value is not a float")
#
#     def test_from_roman(self):
#         integer = Integer.from_roman("XIX")
#         self.assertEqual(integer.value, 19)
#
#     def test_from_string_success(self):
#         integer = Integer.from_string("10")
#         self.assertEqual(integer.value, 10)
#
#     def test_from_string_wrong_type(self):
#         result = Integer.from_string(1.5)
#         self.assertEqual(result, "wrong type")
#
#
# if __name__ == "__main__":
#     unittest.main()