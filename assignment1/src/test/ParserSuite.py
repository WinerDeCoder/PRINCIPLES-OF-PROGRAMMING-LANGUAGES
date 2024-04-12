import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """func main()
        begin
            var x <- 5
            var y <- 10
            var z <- 15
            var result <- multiplyTwoNumbers(addThreeNumbers(x, y, z), addThreeNumbers(y, z, x))
            writeNumber(result)
        end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))