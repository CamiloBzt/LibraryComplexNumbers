import unittest
import complexNumbers as cpl


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(cpl.addComplex([3, -1], [1, 4]), [4, 3])
        self.assertEqual(cpl.addComplex([5, 2], [4, 7]), [9, 9])

    def test_sub(self):
        self.assertEqual(cpl.subtComplex([7, 2], [5, -9]), [2, 11])

    def test_conj(self):
        self.assertEqual(cpl.conjuComplex([-5, 3]), [-5, -3])

    def test_mult(self):
        self.assertEqual(cpl.multComplex([-3, -5], [7, -9]), [-66, -8])

    def test_div(self):
        self.assertEqual(cpl.divComplex([-4, 5], [8, -2]), [round(-42/68, 2), round(32/68, 2)])

    def test_mod(self):
        self.assertEqual(cpl.modComplex([-1, 2]), 2.24)

    def test_phase(self):
        self.assertEqual(cpl.phaseComplex([-1, 2]), 2.03)

    def test_polarC(self):
        self.assertEqual(cpl.polarCarteComplex([5, 45]), [3.53, 3.53])

    def test_carteP(self):
        self.assertEqual(cpl.cartePolarComplex([-3, 3]), [4.24, 2.36])


if __name__ == '__main__':
    unittest.main()
