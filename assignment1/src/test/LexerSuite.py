import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    # Test IDENTIFIER 
    
    def test_simple_string1(self):
        """test simple string"""
        self.assertTrue(TestLexer.test("a1","a1,<EOF>",101))
    def test_complex_string2(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("1a","1,z,<EOF>",102))
    def test_complex_string3(self):
        """test complex string"""
        self.assertTrue(TestLexer.test('_12A_1_',"_12A_1_,<EOF>",103))
    def test_complex_string4(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("ab11_2","ab11_2,<EOF>",104))
    def test_complex_string5(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("_A123","_A123,<EOF>",105))
    def test_complex_string6(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("_a22_11A","_a22_11A,<EOF>",106))
    def test_complex_string7(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("aaAAA","aaAAA,<EOF>",107))
    def test_complex_string8(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("AAAbb111","AAAbb111,<EOF>",108))      
        
    # TEST NUMBER LITERALS
     
    def test_complex_string9(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("123","123,<EOF>",109))
    def test_complex_string10(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("0","0,<EOF>",110))
    def test_complex_string11(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("0.0","0.0,<EOF>",111))
    def test_complex_string12(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("10.1234","10.1234,<EOF>",112))
    def test_complex_string13(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("10e22","10e22,<EOF>",113))
    def test_complex_string14(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("0.33e11","0.33e11,<EOF>",114))
    def test_complex_string15(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("0.233e-1","0.233e-1,<EOF>",115))
    def test_complex_string16(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("0.3134e+1","0.3134e+1,<EOF>",116))
    def test_complex_string17(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("134e+1","134e+1,<EOF>",117))
    def test_complex_string18(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("0e+1","0e+1,<EOF>",118))
    def test_complex_string19(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("11.","11.,<EOF>",119))
    def test_complex_string20(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("11.e222","11.e222,<EOF>",120))
        
    # TEST STRING 
    
    def test_complex_string21(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("truesdsd","truesdsd,<EOF>",121))
    def test_complex_string22(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("false","false,<EOF>",122))
    def test_complex_string23(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "11.e222" ""","11.e222,<EOF>",123))
    def test_complex_string24(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "11????2****.e222" ""","11????2****.e222,<EOF>",124))
    def test_complex_string25(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "~!@#$%^&*()_+" ""","~!@#$%^&*()_+,<EOF>",125))
    def test_complex_string26(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "\\b \\t \\f \\r" ""","\\b  \\t \\f \\r,<EOF>",126))
    def test_complex_string27(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "he ask me: \'"arre uoi dm\'"  \\r \\n " ""","he ask me: \"arre uoi dm\",<EOF>",127))
    def test_complex_string28(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "he ask  me: \\g arre uoi dm " ""","Illegal Escape In String: he ask  me: \g,<EOF>",128))
    def test_complex_string29(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "123<-w \\n\\n\\n " ""","123<-w \\n\\n\\n ,<EOF>",129))
    def test_complex_string30(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "aaaww '" 122 '" 2  2" " ""","aaaww \" 122 \" 2  2,Unclosed String: ,<EOF>",130))
    def test_complex_string31(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "dd\\' eeee \\r \\r " "Hello \\\ \\" ""","dd\\' eeee \\r \\r ,Illegal Escape In String: Hello \\\ \",<EOF>",131))
        
        
        
    def test_complex_string32(self):
        """test complex string"""
        self.assertTrue(TestLexer.test('"abc\'de"',"11.e222,<EOF>",132))       
    def test_complex_string33(self):
        """test complex string"""
        self.assertTrue(TestLexer.test('"\'"\\b\n"',"11.e222,<EOF>",133))        
    def test_complex_string34(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(" a<-111 \n \n ","a,<-,111,\n,\n,<EOF>",134))
    def test_complex_string35(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "dd\' eeee \\ \\ " ""","11.e222,<EOF>",135))
    def test_complex_string36(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "dd\' eeee \\ \\ " ""","11.e222,<EOF>",136))
    def test_complex_string37(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "dd\' eeee \\ \\ " ""","11.e222,<EOF>",137))
    def test_complex_string38(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "dd\' eeee \\ \\ " ""","11.e222,<EOF>",138))
    def test_complex_string39(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "dd\' eeee \\ \\ " ""","11.e222,<EOF>",139))
    def test_complex_string40(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "dd\' eeee \\ \\ " ""","11.e222,<EOF>",140))
    def test_complex_string41(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "dd\' eeee \\ \\ " ""","11.e222,<EOF>",141))
    

    
    
# import unittest
# from TestUtils import TestLexer



# class LexerSuite(unittest.TestCase):

#     # Comment testing
#     def test_CPP_Comment_alone(self):
#         """test CPP_Comment when not inline"""
#         self.assertTrue(TestLexer.test("1123a123", "<EOF>",  101))

#     def test_C_Comment_alone(self):
#         """test C_Comment"""
#         self.assertTrue(TestLexer.test("/* ayyo */ dds */","dds,*,/,<EOF>",  102))
    
#     def test_CPP_Comment_inline(self):
#         """test CPP_Comment inline """
#         self.assertTrue(TestLexer.test("Hello World //day la cmt", "Hello,World,<EOF>", 103))

#     def test_CPP_Comment_inline2(self):
#         """test CPP_Comment inline with \r or \n """
#         self.assertTrue(TestLexer.test("Hello World //day la cmt\r\n Hello2", "Hello,World,Hello2,<EOF>", 104))
    
#     def test_C_Comment_multiLine(self):
#         """test C_Comment block with multiple line """
#         self.assertTrue(TestLexer.test("/* ayyo \r\n ayyo 2 \r\n */\r\n abcd", "abcd,<EOF>", 105))
    
#     # Identifier testing
#     def test_normal_identifier(self):
#         """test normal id"""
#         self.assertTrue(TestLexer.test("abcd AaBc \r\n_123 _12a32H", "abcd,AaBc,_123,_12a32H,<EOF>", 106))
    
#     # def test_wrong_identifier(self):
#     #     """test id with number as a starting letter"""
#     #     self.assertTrue(TestLexer.test("3a2", "Error Token 3",107))
    
#     def test_keyword(self):
#         """test keyword"""
#         self.assertTrue(TestLexer.test("auto false integer void array break float return out boolean for string continue do function true of else if while inherit", "auto,false,integer,void,array,break,float,return,out,boolean,for,string,continue,do,function,true,of,else,if,while,inherit,<EOF>", 107))
    
#     # Operator testing
#         # calcul_operator
#     def test_calcul_operator1(self):
#         """test + - * / with space"""
#         self.assertTrue(TestLexer.test("+ - * / %", "+,-,*,/,%,<EOF>", 108))
    
#     def test_calcul_operator2(self):
#         """test + - * / without space"""
#         self.assertTrue(TestLexer.test("+-*/%", "+,-,*,/,%,<EOF>", 109))
    
#     def test_calcul_operator3(self):
#         """test + - * / with \\n and no space"""
#         self.assertTrue(TestLexer.test("+*\r\n -/", "+,*,-,/,<EOF>", 110))
    
#     def test_calcul_operator4(self):
#         """test / in div with // in comment"""
#         self.assertTrue(TestLexer.test("a2 / v2 //cmt", "a2,/,v2,<EOF>", 111))

#         # logic_operator
#     def test_logic_operator1(self):
#         """test ! op"""
#         self.assertTrue(TestLexer.test("! this do!worry", "!,this,do,!,worry,<EOF>", 112))

#     def test_logic_operator2(self):
#         """test combination AND OR EQUAL and NEQ"""
#         self.assertTrue(TestLexer.test("a && b is != c ||== d ", "a,&&,b,is,!=,c,||,==,d,<EOF>", 113))
    
#     def test_logic_operator3(self):
#         """test combination AND and NEQ and not"""
#         self.assertTrue(TestLexer.test("!===", "!=,==,<EOF>",114))
    
#     def test_logic_operator4(self):
#         """test combination AND and NEQ and not"""
#         self.assertTrue(TestLexer.test("!==", "!=,=,<EOF>",115))
    
#     def test_logic_operator5(self):
#         """test combination AND and NEQ and not"""
#         self.assertTrue(TestLexer.test("!==", "!=,=,<EOF>",116))
    
#         # comparison operators
#     def test_comparison_operator1(self):
#         """test > >= < <= with space"""
#         self.assertTrue(TestLexer.test("> >= < <=", ">,>=,<,<=,<EOF>",117))

#     def test_comparison_operator2(self):
#         """test > >= < <= without space"""
#         self.assertTrue(TestLexer.test(">>=<<=", ">,>=,<,<=,<EOF>",118))

#     # Separator testing
#     def test_separator_operator1(self):
#         """test bracket"""
#         self.assertTrue(TestLexer.test("(abddsad)\r\n {dasdada}\r\n[jgfdmb]", "(,abddsad,),{,dasdada,},[,jgfdmb,],<EOF>",119))
    
#     def test_separator_operator2(self):
#         """test separator"""
#         self.assertTrue(TestLexer.test("end_with_dot .\r\n End_with_comma,\r\n End_with_SM; \r\n a:b\r\nc=d", "end_with_dot,.,End_with_comma,,,End_with_SM,;,a,:,b,c,=,d,<EOF>",120))
    
#     # Literal testing
#         # int literal
#     def test_intLIT1(self):
#         """test int literal """
#         self.assertTrue(TestLexer.test("12367", "12367,<EOF>",121))
    
#     def test_intLIT2(self):
#         """test many int literals """
#         self.assertTrue(TestLexer.test("123 67", "123,67,<EOF>",122))

#     def test_intLIT3(self):
#         """test int literal with _ """
#         self.assertTrue(TestLexer.test("1_23_67", "12367,<EOF>",123))
    
#     def test_intLIT4(self):
#         """test int literal with _ """
#         self.assertTrue(TestLexer.test("1__67", "1,__67,<EOF>",124))
    
#         # float literal
#     def test_floatLIT1(self):
#         """test float literal """
#         self.assertTrue(TestLexer.test("123.67", "123.67,<EOF>",125))

#     def test_floatLIT2(self):
#         """test float literal with _ """
#         self.assertTrue(TestLexer.test("1_23.67", "123.67,<EOF>",126))

#     def test_floatLIT3(self):
#         """test float literal with scientific notation e positive """
#         self.assertTrue(TestLexer.test("123e67", "123e67,<EOF>",127))

#     def test_floatLIT4(self):
#         """test float literal with scientific notation e negative """
#         self.assertTrue(TestLexer.test("123e-67", "123e-67,<EOF>",128))

#     def test_floatLIT5(self):
#         """test float literal with scientific notation E positive"""
#         self.assertTrue(TestLexer.test("145E67", "145E67,<EOF>",129))

#     def test_floatLIT6(self):
#         """test float literal with scientific notation E negative"""
#         self.assertTrue(TestLexer.test("145E-67", "145E-67,<EOF>",130))

#     def test_floatLIT7(self):
#         """test float literal with decimal part and exponent part"""
#         self.assertTrue(TestLexer.test("14.3435E-67 31231.5575e34", "14.3435E-67,31231.5575e34,<EOF>",131))

#     def test_floatLIT8(self):
#         """test many float literals"""
#         self.assertTrue(TestLexer.test("145E-67 342_434.34e34", "145E-67,342434.34e34,<EOF>",132))
    
#     def test_floatLIT9(self):
#         """test float literal with missing INT_PART"""
#         self.assertTrue(TestLexer.test(".23e12 .32E-12 .e56", ".23e12,.32E-12,.e56,<EOF>", 133))
    
#     # def test_intLIT4(self):
#     #     """test int literal with"""
#     #     self.assertTrue(TestLexer.test("1236_", "Error Token _",125))

#     def test_floatLIT_intLIT_1(self):
#         """test float literal and int literal"""
#         self.assertTrue(TestLexer.test("12.34 12", "12.34,12,<EOF>", 134))

#     def test_floatLIT_intLIT_2(self):
#         """test float literal and int literal with _"""
#         self.assertTrue(TestLexer.test("1_2.34 677889", "12.34,677889,<EOF>", 135))

#     def test_floatLIT_intLIT_3(self):
#         """test float literal and int literal with _"""
#         self.assertTrue(TestLexer.test("12.34 67_7889", "12.34,677889,<EOF>", 136))

    
#     def test_floatLIT_intLIT_4(self):
#         """test float literal and int literal with _"""
#         self.assertTrue(TestLexer.test("1_2.34 67_7889", "12.34,677889,<EOF>", 137))

#     def test_floatLIT_intLIT_5(self):
#         """test combination of float and int """
#         self.assertTrue(TestLexer.test("5463 45345_6546_43534 8765.5455 12e45 7645675.563453E23 12_321.53e-12 434_33e-56", "5463,45345654643534,8765.5455,12e45,7645675.563453E23,12321.53e-12,43433e-56,<EOF>", 138))
    
#         #String literal
#     def test_stringLIT_1(self):
#         """test normal string literal """
#         self.assertTrue(TestLexer.test("\"1 string.\"", "1 string.,<EOF>",139))    
    
#     def test_stringLIT_2(self):
#         """test normal string literal with some escape sequences \" """
#         self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John\\"" """, "He asked me: \\\"Where is John\\\",<EOF>",140))    
    
#     def test_stringLIT_3(self):
#         """test normal string literal """
#         self.assertTrue(TestLexer.test(""" "He asked me: \\r\\n \\"Where is John\\" \\b\\f\\t " """, "He asked me: \\r\\n \\\"Where is John\\\" \\b\\f\\t ,<EOF>",141))    
    
#     def test_stringLIT_4(self):
#         """test normal string literal """
#         self.assertTrue(TestLexer.test(""" "He asked me: \\r\\n \\"Where is John\\" \\c\\f\\t " """, "Illegal Escape In String: He asked me: \\r\\n \\\"Where is John\\\" \\c",142))    
    
#     def test_stringLIT_5(self):
#         """test normal string literal """
#         self.assertTrue(TestLexer.test(""" "test case of unclose string !""", "Unclosed String: test case of unclose string !",143))    
    
#     def test_stringLIT_6(self):
#         """test normal string literal """
#         self.assertTrue(TestLexer.test(""" "alo !\n""", "Unclosed String: alo !",144))    
    
#     def test_stringLIT_7(self):
#         """test normal string literal """
#         self.assertTrue(TestLexer.test(""" "Hi! My name is: \\a" """, "Illegal Escape In String: Hi! My name is: \\a",145))    

#     def test_stringLIT_8(self):
#         """test normal string literal """
#         self.assertTrue(TestLexer.test(""" "Hello, this is \y Mi" """, "Illegal Escape In String: Hello, this is \y",146))    

#     def test_stringLIT_9(self):
#         """test normal string literal """
#         self.assertTrue(TestLexer.test(""" "Oh \\b \\r My" """, "Oh \\b \\r My,<EOF>",147))    

#     def test_stringLIT_10(self):
#         """test normal string literal """
#         self.assertTrue(TestLexer.test(""" "String: \\r \\n normal string !" """, "String: \\r \\n normal string !,<EOF>",148))    

#     def test_stringLIT_11(self):
#         """test normal string literal """
#         self.assertTrue(TestLexer.test(""" "illegal and unclose \\e """, "Illegal Escape In String: illegal and unclose \\e",149))    

#     def test_stringLIT_12(self):
#         """test normal string literal """
#         self.assertTrue(TestLexer.test(""" "Unclose with !\n""", "Unclosed String: Unclose with !",150))    

#     # program testing
#     def test_simple_program_1(self):
#         """ test simple program"""
#         self.assertTrue(TestLexer.test(""" a1: integer; """, "a1,:,integer,;,<EOF>",151))    

#     def test_simple_program_2(self):
#         """ test simple program"""
#         self.assertTrue(TestLexer.test(""" a1: integer = 12; """, "a1,:,integer,=,12,;,<EOF>",152))  

#     def test_simple_program_3(self):
#         """ test simple program"""
#         self.assertTrue(TestLexer.test(""" a_1: float; """, "a_1,:,float,;,<EOF>",153))  

#     def test_simple_program_4(self):
#         """ test simple program"""
#         self.assertTrue(TestLexer.test(""" a_1: float = 12.3; """, "a_1,:,float,=,12.3,;,<EOF>",154))  

#     def test_simple_program_5(self):
#         """ test simple program"""
#         self.assertTrue(TestLexer.test(""" a1: bool; """, "a1,:,bool,;,<EOF>",155))  

#     def test_simple_program_6(self):
#         """ test simple program"""
#         self.assertTrue(TestLexer.test(""" a1: bool = true; """, "a1,:,bool,=,true,;,<EOF>",156))  

#     def test_simple_program_7(self):
#         """ test simple program"""
#         self.assertTrue(TestLexer.test(""" a1: string; """, "a1,:,string,;,<EOF>",157))  

#     def test_simple_program_8(self):
#         """ test simple program"""
#         self.assertTrue(TestLexer.test(""" a1: string = "hello"; """, "a1,:,string,=,hello,;,<EOF>",158))  

#     def test_simple_program_9(self):
#         """ test simple program"""
#         self.assertTrue(TestLexer.test(""" a1, b2: integer = 12,23 ; """, "a1,,,b2,:,integer,=,12,,,23,;,<EOF>",159))  

#     def test_simple_program_10(self):
#         """ test simple program"""
#         self.assertTrue(TestLexer.test(""" a1, b2: boolean = true,false ; """, "a1,,,b2,:,boolean,=,true,,,false,;,<EOF>",160)) 

#     def test_simple_program_11(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(""" a2: integer; """, "a2,:,integer,;,<EOF>",161))    

#     def test_simple_program_12(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(""" a2: integer = 12; """, "a2,:,integer,=,12,;,<EOF>",162))  

#     def test_simple_program_13(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(""" a_2: float; """, "a_2,:,float,;,<EOF>",163))  

#     def test_simple_program_14(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(""" a_2: float = 12.3; """, "a_2,:,float,=,12.3,;,<EOF>",164))  

#     def test_simple_program_15(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(""" a3: bool; """, "a3,:,bool,;,<EOF>",165))  

#     def test_simple_program_16(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(""" a4: bool = false; """, "a4,:,bool,=,false,;,<EOF>",166))  

#     def test_simple_program_17(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(""" c2: string; """, "c2,:,string,;,<EOF>",167))  

#     def test_simple_program_18(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(""" a1: string = "hi"; """, "a1,:,string,=,hi,;,<EOF>",168))  

#     def test_simple_program_19(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(""" a1, b2, c3: integer = 12,23,26 ; """, "a1,,,b2,,,c3,:,integer,=,12,,,23,,,26,;,<EOF>",169))  

#     def test_simple_program_20(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(""" a1, b2: boolean = false,false ; """, "a1,,,b2,:,boolean,=,false,,,false,;,<EOF>",170))

#     # Standard program testing
#     def test_standard_program_1(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: string = "Age: ";
#                 printString(a::age(person));""", 
#             "a,:,string,=,Age: ,;,printString,(,a,::,age,(,person,),),;,<EOF>",171))
       
#     def test_standard_program_2(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: integer = 12;
#                 printInt( a + 12);""", 
#             "a,:,integer,=,12,;,printInt,(,a,+,12,),;,<EOF>",172))

#     def test_standard_program_3(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ b: string = "Age: ";
#                 printString(a::age(person));""", 
#             "b,:,string,=,Age: ,;,printString,(,a,::,age,(,person,),),;,<EOF>",173))

#     def test_standard_program_4(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: bool = true;
#                 print(a);""", 
#             "a,:,bool,=,true,;,print,(,a,),;,<EOF>",174))

#     def test_standard_program_5(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ printString(age(person));""", 
#             "printString,(,age,(,person,),),;,<EOF>",175))

#     def test_standard_program_6(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a = add(1,2);""", 
#             "a,=,add,(,1,,,2,),;,<EOF>",176))

#     def test_standard_program_7(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a = add(1,2);
#                 print(\"a:\",a);""", 
#             "a,=,add,(,1,,,2,),;,print,(,a:,,,a,),;,<EOF>",177))

#     def test_standard_program_8(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: bool = b > 2;
#                 print(a);""", 
#             "a,:,bool,=,b,>,2,;,print,(,a,),;,<EOF>",178))

#     def test_standard_program_9(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: integer = add(1,2);
#                 printString(a);""", 
#             "a,:,integer,=,add,(,1,,,2,),;,printString,(,a,),;,<EOF>",179))

#     def test_standard_program_10(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: float = 12.3;
#                 print(a);""", 
#             "a,:,float,=,12.3,;,print,(,a,),;,<EOF>",180))    
    
#     def test_standard_program_11(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: string = "Name: ";
#                 printString(a::name(person));""", 
#             "a,:,string,=,Name: ,;,printString,(,a,::,name,(,person,),),;,<EOF>",181))
       
#     def test_standard_program_12(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: integer = 22;
#                 printInt( a + 22);""", 
#             "a,:,integer,=,22,;,printInt,(,a,+,22,),;,<EOF>",182))

#     def test_standard_program_13(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ tuoi: string = "Age: ";
#                 printString(bach::age(person));""", 
#             "tuoi,:,string,=,Age: ,;,printString,(,bach,::,age,(,person,),),;,<EOF>",183))

#     def test_standard_program_14(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a_2: bool = true;
#                 print(a);""", 
#             "a_2,:,bool,=,true,;,print,(,a,),;,<EOF>",184))

#     def test_standard_program_15(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ printString(name(person));""", 
#             "printString,(,name,(,person,),),;,<EOF>",185))

#     def test_standard_program_16(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a = sub(1,2);""", 
#             "a,=,sub,(,1,,,2,),;,<EOF>",186))

#     def test_standard_program_17(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a = sub(2,3);
#                 print(\"a:\",a);""", 
#             "a,=,sub,(,2,,,3,),;,print,(,a:,,,a,),;,<EOF>",187))

#     def test_standard_program_18(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: bool = b < 3;
#                 print(a);""", 
#             "a,:,bool,=,b,<,3,;,print,(,a,),;,<EOF>",188))

#     def test_standard_program_19(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: integer = sub(1,3);
#                 printString(a);""", 
#             "a,:,integer,=,sub,(,1,,,3,),;,printString,(,a,),;,<EOF>",189))

#     def test_standard_program_20(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: float = 12e3;
#                 print(a);""", 
#             "a,:,float,=,12e3,;,print,(,a,),;,<EOF>",190))
        
#     def test_standard_program_21(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: string = "Name "::"is: ";
#                 printString(a::name(person));""", 
#             "a,:,string,=,Name ,::,is: ,;,printString,(,a,::,name,(,person,),),;,<EOF>",191))
       
#     def test_standard_program_22(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: integer = 32;
#                 printInt( a - 22);""", 
#             "a,:,integer,=,32,;,printInt,(,a,-,22,),;,<EOF>",192))

#     def test_standard_program_23(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ age: string = "Age: ";
#                 printString(age::age(person));""", 
#             "age,:,string,=,Age: ,;,printString,(,age,::,age,(,person,),),;,<EOF>",193))

#     def test_standard_program_24(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a_2: bool = false;
#                 print(a);""", 
#             "a_2,:,bool,=,false,;,print,(,a,),;,<EOF>",194))

#     def test_standard_program_25(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ printString(isStudent(person));""", 
#             "printString,(,isStudent,(,person,),),;,<EOF>",195))

#     def test_standard_program_26(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a = mul(1,2);""", 
#             "a,=,mul,(,1,,,2,),;,<EOF>",196))

#     def test_standard_program_27(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a = mod(2,3);
#                 print(\"a:\",a);""", 
#             "a,=,mod,(,2,,,3,),;,print,(,a:,,,a,),;,<EOF>",197))

#     def test_standard_program_28(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: bool = b <= 3;
#                 print(a);""", 
#             "a,:,bool,=,b,<=,3,;,print,(,a,),;,<EOF>",198))

#     def test_standard_program_29(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: integer = fact(1,3);
#                 print(a);""", 
#             "a,:,integer,=,fact,(,1,,,3,),;,print,(,a,),;,<EOF>",199))

#     def test_standard_program_30(self):
#         """ test standard program"""
#         self.assertTrue(TestLexer.test(
#             """ a: float = 12.e3;
#                 print(a);""", 
#             "a,:,float,=,12.e3,;,print,(,a,),;,<EOF>",200))