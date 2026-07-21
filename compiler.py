import numexpr
import math
import statistics
import numpy

class Compiler:
    var = {}
    func = {}
    available_vars = {
        "pi": math.pi,
        "euler_number": math.e,
        "tau": math.tau,
        "infinity": math.inf
    }
    available_functions = {
        "math": numexpr.evaluate,
        "greatest_common_divisor": math.gcd,
        "square_root": math.sqrt,
        "sine": math.sin,
        "cosine": math.cos,
        "factorial": math.factorial,
        "tangent": math.tan,
        "logarithm": math.log,
        "natural_log": math.log,
        "log_base_2": math.log2,
        "log_base_10": math.log10,
        "exponential": math.exp,
        "power": math.pow,
        "ceiling": math.ceil,
        "floor": math.floor,
        "truncation": math.trunc,
        "rounding": round,
        "integer_square_root": math.isqrt,
        "binomial_coefficient": math.comb,
        "permutations": math.perm,
        "degreeXradian": math.radians,
        "radianXdegree": math.degrees,
        "least_common_multiple": math.lcm,
        "hypotenuse": math.hypot,
        "arctangent": math.atan2,
        "average": statistics.mean,
        "middle": statistics.median,
        "mode": statistics.mode,
        "sample_standard_deviation": statistics.stdev,
        "population_standard_deviation": statistics.pstdev,
        "sample_variance": statistics.variance,
        "population_variance": statistics.pvariance,
        "pearson_correlation_coefficient": statistics.correlation,
        "Linear regression": statistics.linear_regression,
        "matrix_multiplication": numpy.dot,
        "matrix_determinant": numpy.linalg.det,
        "matrix_inverse": numpy.linalg.inv,
        "Eigenvalues_and_eigenvectors": numpy.linalg.eig,
        "singular_value_decomposition": numpy.linalg.svd,
        "qr_decomposition": numpy.linalg.qr,
        "cholesky_decomposition": numpy.linalg.cholesky,
        "fast_fourier_transform": numpy.fft.fft
    }
    
    def __init__(self, file):
        self.file = file
        self.list_content = open(file, "r").readlines()
        self.content = []
        for content in self.list_content:
            self.content.append(content.replace("\n", ""))
        self.list_content = self.content
        del self.content

    def read_var(self):
        for content in self.list_content:
            if content.startswith("var"):
                value = str(content.split("=")[1])
                list_value = [val for val in value]
                list_value.pop(0)
                value = ""
                for val in list_value:
                    value += val
                value = self.string(value)
                key = content.replace("var", "").replace(" ", "").replace(value, "").split("=")[0]
                if value.isdigit():
                    value = self.convert_to_number(value)
                try:
                    if value.capitalize() == "True":
                        value = True
                    elif value.capitalize() == "False":
                        value = False
                    elif value.capitalize() == "Null":
                        value = None
                except:
                    value = value
                self.var[key] = value

    def read_var_value_as_function(self):
        for content in self.list_content:
            if content.startswith("var"):
                value = str(content.split("=")[1])
                list_value = [val for val in value]
                list_value.pop(0)
                value = ""
                for val in list_value:
                    value += val
                value = self.string(value)
                key = content.replace("var", "").replace(" ", "").replace(value, "").split("=")[0]
                func_entry = value.split("(")[1].replace(")", "").replace(" ", "").split(",")
                for func in self.available_functions:
                    if func == value.split("(")[0].replace("(", ""):
                        if len(func_entry) <= 3:
                            if len(func_entry) == 1:
                                if func_entry[0].isdigit():
                                    func_entry[0] = self.convert_to_number(func_entry[0])
                                self.var[key] = str(self.available_functions[func](func_entry[0]))
                            elif len(func_entry) == 2:
                                if func_entry[0].isdigit():
                                    func_entry[0] = self.convert_to_number(func_entry[0])
                                if func_entry[1].isdigit():
                                    func_entry[1] = self.convert_to_number(func_entry[1])
                                self.var[key] = str(self.available_functions[func](func_entry[0], func_entry[1]))
                            elif len(func_entry) == 3:
                                if func_entry[0].isdigit():
                                    func_entry[0] = self.convert_to_number(func_entry[0])
                                if func_entry[1].isdigit():
                                    func_entry[1] = self.convert_to_number(func_entry[1])
                                if func_entry[2].isdigit():
                                    func_entry[2] = self.convert_to_number(func_entry[2])
                                self.var[key] = str(self.available_functions[func](func_entry[0], func_entry[1], func_entry[2]))

    def read_defined_func(self):
        printit = True
        for content in self.list_content:
            if content.startswith("callfunc"):
                content = content.replace(" ", "").split("callfunc")
                func = content[1].split("(")[0]
                func_entry = content[1].split("(")[1].replace(")", "")
                func_entry = self.string(func_entry)
                for funcs in self.available_functions:
                    if funcs == func:
                        if "," in func_entry:
                            func_entry = func_entry.split(",")
                            if len(func_entry) <= 3:
                                if len(func_entry) == 1:
                                    if func_entry[0].isdigit():
                                        func_entry[0] = self.convert_to_number(func_entry[0])
                                    print(self.available_functions[funcs](func_entry[0]))
                                    printit = False
                                elif len(func_entry) == 2:
                                    if func_entry[0].isdigit():
                                        func_entry[0] = self.convert_to_number(func_entry[0])
                                    if func_entry[1].isdigit():
                                        func_entry[1] = self.convert_to_number(func_entry[1])
                                    print(self.available_functions[funcs](func_entry[0], func_entry[1]))
                                    printit = False
                                elif len(func_entry) == 3:
                                    if func_entry[0].isdigit():
                                        func_entry[0] = self.convert_to_number(func_entry[0])
                                    if func_entry[1].isdigit():
                                        func_entry[1] = self.convert_to_number(func_entry[1])
                                    if func_entry[2].isdigit():
                                        func_entry[2] = self.convert_to_number(func_entry[2])
                                    print(self.available_functions[funcs](func_entry[0], func_entry[1], func_entry[2]))
                                    printit = False
                        if printit:
                            print(self.available_functions[funcs](self.convert_to_number(func_entry)))

    def print_value(self):
        self.value_to_print = []
        self.printed = []
        for content in self.list_content:
            if content.startswith("print("):
                entry_value = content.replace(")", "").split("print(")
                entry_value = self.string(entry_value)
                for key in self.available_vars:
                    try:
                        if self.var[entry_value]:
                            for data in self.var:
                                if data == self.var[entry_value]:
                                    continue
                            self.value_to_print.append(self.var[entry_value])
                        if key == entry_value:
                            self.value_to_print.append(self.available_vars[key])
                    except:
                        self.value_to_print.append(entry_value)
        for m in self.value_to_print:
            if m not in self.printed:
                print(m)
                self.printed.append(m)

    def create_function(self):
        i = 0
        while i < len(self.list_content):
            content = self.list_content[i]
            if content.startswith("func"):
                func_name = content.replace("func", "").replace(" ", "").split("(")[0]
                func_content = []
                
                i += 1
                
                while i < len(self.list_content):
                    line = self.list_content[i]
                    if line.strip() == "%":
                        i += 1
                        break
                    else:
                        func_content.append(line)
                        i += 1
            
                con = "\n".join(func_content)
                con = con.split("\n")
                self.func[func_name] = "\n".join(func_content)
            else:
                i += 1

    def read_user_created_function(self):
        for content in self.list_content:
            print(content.split("(")[0])

    def convert_to_number(self, value):
        try:
            if "." in value:
                return float(value)
            else:
                return int(value)
        except:
            if str(value).capitalize() == "True":
                return True
            elif str(value).capitalize() == "False":
                return False
            elif str(value).capitalize() == "Null":
                return None
            else:
                return value

    def string(self, value):
        m = ""
        for val in value:
            if val.startswith("'") and val.endswith("'"):
                val = val.replace("'", "")
            elif val.startswith('"') and val.endswith('"'):
                val = val.replace('"', "")
            m += val
        return m

    def compile(self):
        self.read_var()
        self.read_defined_func()
        self.read_var_value_as_function()
        self.create_function()
        self.read_user_created_function()
        self.print_value()
        print(self.func)

compiler = Compiler("test.math")
compiler.compile()