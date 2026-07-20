import unittest
import math
from compiler import Compiler

class TestAvailableFunctions(unittest.TestCase):
    
    def setUp(self):
        self.functions = Compiler.available_functions
    
    def test1_math(self):
        result = self.functions["math"]("2 + 3")
        self.assertEqual(result, 5)
        result = self.functions["math"]("10 * 5")
        self.assertEqual(result, 50)
        result = self.functions["math"]("2 ** 3")
        self.assertEqual(result, 8)
    
    def test2_gcd(self):
        self.assertEqual(self.functions["greatest_common_divisor"](12, 18), 6)
        self.assertEqual(self.functions["greatest_common_divisor"](17, 13), 1)
        self.assertEqual(self.functions["greatest_common_divisor"](100, 25), 25)
    
    def test3_square_root(self):
        self.assertEqual(self.functions["square_root"](25), 5)
        self.assertEqual(self.functions["square_root"](81), 9)
        self.assertAlmostEqual(self.functions["square_root"](2), 1.4142135623730951)
    
    def test4_sine(self):
        self.assertEqual(self.functions["sine"](0), 0)
        self.assertEqual(int(self.functions["sine"](math.pi/2)), 1)
        self.assertEqual(int(self.functions["sine"](math.pi)), 0)
    
    def test5_cosine(self):
        self.assertEqual(self.functions["cosine"](0), 1)
        self.assertEqual(self.functions["cosine"](math.pi), -1)
        self.assertEqual(int(self.functions["cosine"](math.pi/2)), 0)
    
    def test6_factorial(self):
        self.assertEqual(self.functions["factorial"](5), 120)
        self.assertEqual(self.functions["factorial"](0), 1)
        self.assertEqual(self.functions["factorial"](1), 1)
    
    def test7_tangent(self):
        self.assertEqual(self.functions["tangent"](0), 0)
        self.assertAlmostEqual(self.functions["tangent"](math.pi/4), 1)
    
    def test8_logarithm(self):
        self.assertEqual(self.functions["logarithm"](math.e), 1)
        self.assertEqual(self.functions["logarithm"](1), 0)
        self.assertAlmostEqual(self.functions["logarithm"](math.e**2), 2)
    
    def test9_log_base_2(self):
        self.assertEqual(self.functions["log_base_2"](8), 3)
        self.assertEqual(self.functions["log_base_2"](2), 1)
        self.assertEqual(self.functions["log_base_2"](1), 0)
    
    def test10_log_base_10(self):
        self.assertEqual(self.functions["log_base_10"](100), 2)
        self.assertEqual(self.functions["log_base_10"](10), 1)
        self.assertEqual(self.functions["log_base_10"](1), 0)
    
    def test11_exponential(self):
        self.assertEqual(self.functions["exponential"](0), 1)
        self.assertAlmostEqual(self.functions["exponential"](1), math.e)
        self.assertAlmostEqual(self.functions["exponential"](2), math.e**2)
    
    def test12_power(self):
        self.assertEqual(self.functions["power"](2, 3), 8)
        self.assertEqual(self.functions["power"](5, 2), 25)
        self.assertEqual(self.functions["power"](10, 0), 1)
    
    def test13_ceiling(self):
        self.assertEqual(self.functions["ceiling"](3.2), 4)
        self.assertEqual(self.functions["ceiling"](3.0), 3)
        self.assertEqual(self.functions["ceiling"](-3.2), -3)
    
    def test14_floor(self):
        self.assertEqual(self.functions["floor"](3.8), 3)
        self.assertEqual(self.functions["floor"](3.0), 3)
        self.assertEqual(self.functions["floor"](-3.8), -4)
    
    def test15_truncation(self):
        self.assertEqual(self.functions["truncation"](3.8), 3)
        self.assertEqual(self.functions["truncation"](3.0), 3)
        self.assertEqual(self.functions["truncation"](-3.8), -3)
    
    def test16_rounding(self):
        self.assertEqual(self.functions["rounding"](3.5), 4)
        self.assertEqual(self.functions["rounding"](3.4), 3)
        self.assertEqual(self.functions["rounding"](3.0), 3)
    
    def test17_integer_square_root(self):
        self.assertEqual(self.functions["integer_square_root"](25), 5)
        self.assertEqual(self.functions["integer_square_root"](26), 5)
        self.assertEqual(self.functions["integer_square_root"](0), 0)
    
    def test18_binomial_coefficient(self):
        self.assertEqual(self.functions["bBinomial_coefficient"](5, 2), 10)
        self.assertEqual(self.functions["bBinomial_coefficient"](5, 0), 1)
        self.assertEqual(self.functions["bBinomial_coefficient"](5, 5), 1)
    
    def test19_permutations(self):
        self.assertEqual(self.functions["permutations"](5, 2), 20)
        self.assertEqual(self.functions["permutations"](5, 0), 1)
        self.assertEqual(self.functions["permutations"](5, 5), 120)
    
    def test20_degree_to_radian(self):
        self.assertEqual(self.functions["degreeXradian"](180), math.pi)
        self.assertEqual(self.functions["degreeXradian"](90), math.pi/2)
        self.assertEqual(self.functions["degreeXradian"](0), 0)
    
    def test21_radian_to_degree(self):
        self.assertEqual(self.functions["radianXdegree"](math.pi), 180)
        self.assertEqual(self.functions["radianXdegree"](math.pi/2), 90)
        self.assertEqual(self.functions["radianXdegree"](0), 0)
    
    def test22_lcm(self):
        self.assertEqual(self.functions["least_common_multiple"](4, 6), 12)
        self.assertEqual(self.functions["least_common_multiple"](5, 7), 35)
        self.assertEqual(self.functions["least_common_multiple"](3, 9), 9)
    
    def test23_hypotenuse(self):
        self.assertEqual(self.functions["hypotenuse"](3, 4), 5)
        self.assertEqual(self.functions["hypotenuse"](5, 12), 13)
        self.assertAlmostEqual(self.functions["hypotenuse"](1, 1), math.sqrt(2))
    
    def test24_arctangent(self):
        self.assertEqual(self.functions["arctangent"](0, 1), 0)
        self.assertAlmostEqual(self.functions["arctangent"](1, 1), math.pi/4)
        self.assertAlmostEqual(self.functions["arctangent"](1, 0), math.pi/2)
    
    def test25_average(self):
        self.assertEqual(self.functions["average"]([1, 2, 3, 4, 5]), 3)
        self.assertEqual(self.functions["average"]([10, 20, 30]), 20)
        self.assertEqual(self.functions["average"]([5]), 5)
    
    def test26_median(self):
        self.assertEqual(self.functions["middle"]([1, 2, 3, 4, 5]), 3)
        self.assertEqual(self.functions["middle"]([1, 2, 3, 4]), 2.5)
        self.assertEqual(self.functions["middle"]([5]), 5)
    
    def test27_mode(self):
        self.assertEqual(self.functions["mode"]([1, 2, 2, 3, 4]), 2)
        self.assertEqual(self.functions["mode"]([1, 1, 1, 2, 2]), 1)
    
    def test28_sample_std_dev(self):
        data = [1, 2, 3, 4, 5]
        result = self.functions["sample_standard_deviation"](data)
        self.assertAlmostEqual(result, 1.5811388300841898)
    
    def test29_population_std_dev(self):
        data = [1, 2, 3, 4, 5]
        result = self.functions["population_standard_deviation"](data)
        self.assertAlmostEqual(result, 1.4142135623730951)
    
    def test30_sample_variance(self):
        data = [1, 2, 3, 4, 5]
        result = self.functions["sample_variance"](data)
        self.assertEqual(result, 2.5)
    
    def test31_population_variance(self):
        data = [1, 2, 3, 4, 5]
        result = self.functions["population_variance"](data)
        self.assertEqual(result, 2.0)
    
    def test32_pearson_correlation(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        result = self.functions["pearson_correlation_coefficient"](x, y)
        self.assertEqual(result, 1.0)
    
    def test33_linear_regression(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        result = self.functions["Linear regression"](x, y)
        self.assertAlmostEqual(result.slope, 2.0)
        self.assertAlmostEqual(result.intercept, 0.0)

if __name__ == '__main__':
    unittest.main()