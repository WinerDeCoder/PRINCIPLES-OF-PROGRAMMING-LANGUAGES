import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """number a
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, None)])"""
        self.assertTrue(TestAST.test(input,expect,300))
        
    def test_simple_program1(self):
        input = """number a <- 1
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(1.0))])"""
        self.assertTrue(TestAST.test(input,expect,301))
        
    def test_simple_program2(self):
        input ="""func main() return 1
"""
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input,expect,302))
        
    def test_simple_program3(self):
        input = """number a <- "1111"
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, StringLit(1111))])"""
        self.assertTrue(TestAST.test(input,expect,303))
        
    def test_simple_program4(self):
        input = """number a <- 1 + 1
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input,expect,304))
        
    def test_simple_program5(self):
        input = """number a <- 1 + 1 -3
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, BinaryOp(-, BinaryOp(+, NumLit(1.0), NumLit(1.0)), NumLit(3.0)))])"""
        self.assertTrue(TestAST.test(input,expect,305))
        
    def test_simple_program6(self):
        input = """number a <- 1 + 1 -3 ==2
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, BinaryOp(==, BinaryOp(-, BinaryOp(+, NumLit(1.0), NumLit(1.0)), NumLit(3.0)), NumLit(2.0)))])"""
        self.assertTrue(TestAST.test(input,expect,306))
        
    def test_simple_program7(self):
        input = """number a <- 1 + true
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), BooleanLit(True)))])"""
        self.assertTrue(TestAST.test(input,expect,307))
        
    def test_simple_program8(self):
        input = """number a <- 1 + "1111"
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, BinaryOp(+, NumLit(1.0), StringLit(1111)))])"""
        self.assertTrue(TestAST.test(input,expect,308))
        
    def test_simple_program9(self):
        input = """number a <- 1 - 1 /2 *2
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, BinaryOp(-, NumLit(1.0), BinaryOp(*, BinaryOp(/, NumLit(1.0), NumLit(2.0)), NumLit(2.0))))])"""
        self.assertTrue(TestAST.test(input,expect,309))
        
    def test_simple_program10(self):
        input = 	"""func main() begin
number a
if (5 < 2) a <- 1
elif (not true) a <- 2
elif ("h" == "6") a <- 3
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"""
        self.assertTrue(TestAST.test(input,expect,310))
        
    def test_simple_program11(self):
        input = """number a <- b - c +exp
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, BinaryOp(+, BinaryOp(-, Id(b), Id(c)), Id(exp)))])"""
        self.assertTrue(TestAST.test(input,expect,311))
        
    def test_simple_program12(self):
        input = """number a <- all()
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, CallExpr(Id(all), []))])"""
        self.assertTrue(TestAST.test(input,expect,312))
        
    def test_simple_program13(self):
        input = """number a <- callfunc(1,2)
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, CallExpr(Id(callfunc), [NumLit(1.0), NumLit(2.0)]))])"""
        self.assertTrue(TestAST.test(input,expect,313))
        
    def test_simple_program14(self):
        input = """number a <- callfunc(1,"2") -20
        """
        expect = """Program([VarDecl(Id(a), NumberType, None, BinaryOp(-, CallExpr(Id(callfunc), [NumLit(1.0), StringLit(2)]), NumLit(20.0)))])"""
        self.assertTrue(TestAST.test(input,expect,314))
        
    def test_simple_program15(self):
        input = """bool a <- 1 ... -foo(123,"111") - -(foo() +1)
        """
        expect = """Program([VarDecl(Id(a), BoolType, None, BinaryOp(..., NumLit(1.0), BinaryOp(-, UnaryOp(-, CallExpr(Id(foo), [NumLit(123.0), StringLit(111)])), UnaryOp(-, BinaryOp(+, CallExpr(Id(foo), []), NumLit(1.0))))))])"""
        self.assertTrue(TestAST.test(input,expect,315))
        
    def test_simple_program16(self):
        input = """string acv_1 <- "11\\n"
        """
        expect = """Program([VarDecl(Id(acv_1), StringType, None, StringLit(11\\n))])"""
        self.assertTrue(TestAST.test(input,expect,316))
        
    def test_simple_program17(self):
        input = """string acv_1[1] <- [1]
        """
        expect = """Program([VarDecl(Id(acv_1), ArrayType([NumLit(1.0)], StringType), None, ArrayLit(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input,expect,317))
        
    def test_simple_program18(self):
        input = """string ac[1,2] <- [[1,2],[2]]
        """
        expect = """Program([VarDecl(Id(ac), ArrayType([NumLit(1.0), NumLit(2.0)], StringType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(2.0))))])"""
        self.assertTrue(TestAST.test(input,expect,318))
        
    def test_simple_program19(self):
        input = """string acv_1A[2,4] <- 1111
        """
        expect = """Program([VarDecl(Id(acv_1A), ArrayType([NumLit(2.0), NumLit(4.0)], StringType), None, NumLit(1111.0))])"""
        self.assertTrue(TestAST.test(input,expect,319))
        
    def test_simple_program20(self):
        input = """number acv_1 <- ["111"]
        """
        expect = """Program([VarDecl(Id(acv_1), NumberType, None, ArrayLit(StringLit(111)))])"""
        self.assertTrue(TestAST.test(input,expect,320))
        
    def test_simple_program21(self):
        input = """number acv_1 <- ["111",true]
        """
        expect = """Program([VarDecl(Id(acv_1), NumberType, None, ArrayLit(StringLit(111), BooleanLit(True)))])"""
        self.assertTrue(TestAST.test(input,expect,321))
        
    def test_simple_program22(self):
        input = """number acv_1[2] <- ["111",true]
        string _111_ <- "aaa"
        bool trollvn <- 1+1=1
        """
        expect = """Program([VarDecl(Id(acv_1), ArrayType([2.0], NumberType), None, ArrayLit(StringLit(111), BooleanLit(True))), VarDecl(Id(_111_), StringType, None, StringLit(aaa)), VarDecl(Id(trollvn), BoolType, None, BinaryOp(=, BinaryOp(+, NumLit(1.0), NumLit(1.0)), NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input,expect,322))
        
    def test_simple_program23(self):
        input = """func main()
        """
        expect = """Program([FuncDecl(Id(main), [], None)])"""
        self.assertTrue(TestAST.test(input,expect,323))
        
    def test_simple_program24(self):
        input = """func main(number a)
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], None)])"""
        self.assertTrue(TestAST.test(input,expect,324))
        
    def test_simple_program25(self):
        input = """func main(number a, string b, bool c)
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), StringType, None, None), VarDecl(Id(c), BoolType, None, None)], None)])"""
        self.assertTrue(TestAST.test(input,expect,325))
        
    def test_simple_program26(self):
        input = """func main(number a, string h[1,3,4])
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(h), ArrayType([NumLit(1.0), NumLit(3.0), NumLit(4.0)], StringType), None, None)], None)])"""
        self.assertTrue(TestAST.test(input,expect,326))
        
    def test_simple_program27(self):
        input = """func main(number a) return 1
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input,expect,327))
        
    def test_simple_program28(self):
        input = """func main(number a) return 1 + 2 -3 /4 ==true
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(==, BinaryOp(-, BinaryOp(+, NumLit(1.0), NumLit(2.0)), BinaryOp(/, NumLit(3.0), NumLit(4.0))), BooleanLit(True))))])"""
        self.assertTrue(TestAST.test(input,expect,328))
        
    def test_simple_program29(self):
        input = """func main(number a) return "hhh" ... "12"
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(..., StringLit(hhh), StringLit(12))))])"""
        self.assertTrue(TestAST.test(input,expect,329))
        
    def test_simple_program30(self):
        input = """func main(number a) return [1,2,3]
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))))])"""
        self.assertTrue(TestAST.test(input,expect,330))
        
    def test_simple_program31(self):
        input = """func main(number a) begin
        return 1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([Return(NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input,expect,331))
        
    def test_simple_program32(self):
        input = """func main(number a) begin
        return 1
        return 2
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([Return(NumLit(1.0)), Return(NumLit(2.0))]))])"""
        self.assertTrue(TestAST.test(input,expect,332))
        
    def test_simple_program33(self):
        input = """func main(number a)
        begin
        var x <-1
        return 1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([VarDecl(Id(x), None, var, NumLit(1.0)), Return(NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input,expect,333))
        
    def test_simple_program34(self):
        input = """func main(number a)
        begin
        var x <-1
        dynamic y <- "111"
        return 1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([VarDecl(Id(x), None, var, NumLit(1.0)), VarDecl(Id(y), None, dynamic, StringLit(111)), Return(NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input,expect,334))
        
    def test_simple_program35(self):
        input = """func main(number a)
        begin
        return 1
        var x <-1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([Return(NumLit(1.0)), VarDecl(Id(x), None, var, NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input,expect,335))

    def test_simple_program36(self):
        input = """func main(number a)
        begin
        return foo(4)
        var x <- alo(123)
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([Return(CallExpr(Id(foo), [NumLit(4.0)])), VarDecl(Id(x), None, var, CallExpr(Id(alo), [NumLit(123.0)]))]))])"""
        self.assertTrue(TestAST.test(input,expect,336))
        
    def test_simple_program37(self):
        input = """func main(number a, number b)
        begin
        return 1
        var x <-1
        break
        end
        number x <- "string"
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(NumLit(1.0)), VarDecl(Id(x), None, var, NumLit(1.0)), Break])), VarDecl(Id(x), NumberType, None, StringLit(string))])"""
        self.assertTrue(TestAST.test(input,expect,337))
        
    def test_simple_program38(self):
        input = """func main(number a, number b)
        begin
        return 1
        var x <-1
        break
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(NumLit(1.0)), VarDecl(Id(x), None, var, NumLit(1.0)), Break]))])"""
        self.assertTrue(TestAST.test(input,expect,338))

    def test_simple_program39(self):
        input = """func main(number a)
        begin
        return 1
        var x <-1
        continue
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([Return(NumLit(1.0)), VarDecl(Id(x), None, var, NumLit(1.0)), Continue]))])"""
        self.assertTrue(TestAST.test(input,expect,339))
        
    def test_simple_program40(self):
        input = """func main(number a)
        begin
        number x <- 1 + 2 -1 --1 + foo(20)
        return 1
        var x <-1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([VarDecl(Id(x), NumberType, None, BinaryOp(+, BinaryOp(-, BinaryOp(-, BinaryOp(+, NumLit(1.0), NumLit(2.0)), NumLit(1.0)), UnaryOp(-, NumLit(1.0))), CallExpr(Id(foo), [NumLit(20.0)]))), Return(NumLit(1.0)), VarDecl(Id(x), None, var, NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input,expect,340))
        
    def test_simple_program41(self):
        input = """func main(number a)
        begin
        return 1
        end
        
        func _vippro_() 
        begin
            x <- da_money_team()
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([Return(NumLit(1.0))])), FuncDecl(Id(_vippro_), [], Block([AssignStmt(Id(x), CallExpr(Id(da_money_team), []))]))])"""
        self.assertTrue(TestAST.test(input,expect,341))
        
    def test_simple_program42(self):
        input = """func main(number a)
        begin
        return 1
        end
        
        func _vippro_() 
        begin
            x <- da_money_team()
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([Return(NumLit(1.0))])), FuncDecl(Id(_vippro_), [], Block([AssignStmt(Id(x), CallExpr(Id(da_money_team), []))]))])"""
        self.assertTrue(TestAST.test(input,expect,342))
        
    def test_simple_program43(self):
        input = """func main() return 
        
        func _vippro_(string _12a2) 
        begin
            x <- da_money_team()
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Return()), FuncDecl(Id(_vippro_), [VarDecl(Id(_12a2), StringType, None, None)], Block([AssignStmt(Id(x), CallExpr(Id(da_money_team), []))]))])"""
        self.assertTrue(TestAST.test(input,expect,343))
        
    def test_simple_program44(self):
        input = """func main() return 12
        
        func _vippro_(string _12a2, number a[111]) 
        begin
            x <- da_money_team()
            a[1] <- [1]
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(12.0))), FuncDecl(Id(_vippro_), [VarDecl(Id(_12a2), StringType, None, None), VarDecl(Id(a), ArrayType([NumLit(111.0)], NumberType), None, None)], Block([AssignStmt(Id(x), CallExpr(Id(da_money_team), [])), AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), ArrayLit(NumLit(1.0)))]))])"""
        self.assertTrue(TestAST.test(input,expect,344))
        
    def test_simple_program45(self):
        input = """func main()
        
        func _vippro_(string _12a2) 
        begin
            x <- da_money_team(andree_right_hand)
            foo()
            
        end
        """
        expect = """Program([FuncDecl(Id(main), [], None), FuncDecl(Id(_vippro_), [VarDecl(Id(_12a2), StringType, None, None)], Block([AssignStmt(Id(x), CallExpr(Id(da_money_team), [Id(andree_right_hand)])), CallStmt(Id(foo), [])]))])"""
        self.assertTrue(TestAST.test(input,expect,345))
        
    def test_simple_program46(self):
        input = """func main()
        
        func _vippro_(string _12a2) 
        begin
            x <- da_money_team(andree_right_hand)
            foo()
            number a[10] <- foo()[1,1]
            
        end
        """
        expect = """Program([FuncDecl(Id(main), [], None), FuncDecl(Id(_vippro_), [VarDecl(Id(_12a2), StringType, None, None)], Block([AssignStmt(Id(x), CallExpr(Id(da_money_team), [Id(andree_right_hand)])), CallStmt(Id(foo), []), VarDecl(Id(a), ArrayType([NumLit(10.0)], NumberType), None, ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(1.0)]))]))])"""
        self.assertTrue(TestAST.test(input,expect,346))
        
    def test_simple_program47(self):
        input = """func _vippro_(string _12a2) 
        begin
            x <- da_money_team(andree_right_hand[1])
            foo()
            number a[10] <- foo()[1,1] + 1 
            
        end
        """
        expect = """Program([FuncDecl(Id(_vippro_), [VarDecl(Id(_12a2), StringType, None, None)], Block([AssignStmt(Id(x), CallExpr(Id(da_money_team), [ArrayCell(Id(andree_right_hand), [NumLit(1.0)])])), CallStmt(Id(foo), []), VarDecl(Id(a), ArrayType([NumLit(10.0)], NumberType), None, BinaryOp(+, ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0), NumLit(1.0)]), NumLit(1.0)))]))])"""
        self.assertTrue(TestAST.test(input,expect,347))
        
    def test_simple_program48(self):
        input = """func main(number a)
        begin
        number x <- andree_right_hand[1] + binz(foo())
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), NumberType, None, None)], Block([VarDecl(Id(x), NumberType, None, BinaryOp(+, ArrayCell(Id(andree_right_hand), [NumLit(1.0)]), CallExpr(Id(binz), [CallExpr(Id(foo), [])])))]))])"""
        self.assertTrue(TestAST.test(input,expect,348))
        
    def test_simple_program49(self):
        input = """func main(bool a)
        begin
            a[1] <- i
            return a+1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), Id(i)), Return(BinaryOp(+, Id(a), NumLit(1.0)))]))])"""
        self.assertTrue(TestAST.test(input,expect,349))
        
    def test_simple_program50(self):
        input = """func main(bool a)
        begin
            a[4] <- i
            return a+1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(a), [NumLit(4.0)]), Id(i)), Return(BinaryOp(+, Id(a), NumLit(1.0)))]))])"""
        self.assertTrue(TestAST.test(input,expect,350))
        
    def test_simple_program51(self):
        input = """func main(bool a)
        begin
            a[1,3] <- [1,2,[1,1]]
            return a+1 +2
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(a), [NumLit(1.0), NumLit(3.0)]), ArrayLit(NumLit(1.0), NumLit(2.0), ArrayLit(NumLit(1.0), NumLit(1.0)))), Return(BinaryOp(+, BinaryOp(+, Id(a), NumLit(1.0)), NumLit(2.0)))]))])"""
        self.assertTrue(TestAST.test(input,expect,351))
        
    def test_simple_program52(self):
        input = """func main(bool a)
        begin
            a[1] <- foo([1111])
            return _acs_1 + true
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), CallExpr(Id(foo), [ArrayLit(NumLit(1111.0))])), Return(BinaryOp(+, Id(_acs_1), BooleanLit(True)))]))])"""
        self.assertTrue(TestAST.test(input,expect,352))
        
    def test_simple_program53(self):
        input = """func main(bool a)
        begin
            a[1] <- [111,"dddxx"]
            return a+1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), ArrayLit(NumLit(111.0), StringLit(dddxx))), Return(BinaryOp(+, Id(a), NumLit(1.0)))]))])"""
        self.assertTrue(TestAST.test(input,expect,353))
        
    def test_simple_program54(self):
        input = """func main(bool a)
        begin
            a[1] <- ["123",fo(11)]
            return a+1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), ArrayLit(StringLit(123), CallExpr(Id(fo), [NumLit(11.0)]))), Return(BinaryOp(+, Id(a), NumLit(1.0)))]))])"""
        self.assertTrue(TestAST.test(input,expect,354))
        
    def test_simple_program55(self):
        input = """func main(bool a)
        begin
            a[1] <- avcd[1,2]
            return true
            return false
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), ArrayCell(Id(avcd), [NumLit(1.0), NumLit(2.0)])), Return(BooleanLit(True)), Return(BooleanLit(True))]))])"""
        self.assertTrue(TestAST.test(input,expect,355))
        
    def test_simple_program56(self):
        input = """func main(bool a)
        begin
            a[1] <- foo()[1]
            return a+1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), ArrayCell(CallExpr(Id(foo), []), [NumLit(1.0)])), Return(BinaryOp(+, Id(a), NumLit(1.0)))]))])"""
        self.assertTrue(TestAST.test(input,expect,356))
        
    def test_simple_program57(self):
        input = """func main(bool a)
        begin
            a[1] <- vipro(ss)[22,2]
            return a+1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), ArrayCell(CallExpr(Id(vipro), [Id(ss)]), [NumLit(22.0), NumLit(2.0)])), Return(BinaryOp(+, Id(a), NumLit(1.0)))]))])"""
        self.assertTrue(TestAST.test(input,expect,357))
        
    def test_simple_program58(self):
        input = """func main(bool a,number b)
        begin
            a[1] <- foo_xa(1+3)[3+2]
            return a+ false
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), ArrayCell(CallExpr(Id(foo_xa), [BinaryOp(+, NumLit(1.0), NumLit(3.0))]), [BinaryOp(+, NumLit(3.0), NumLit(2.0))])), Return(BinaryOp(+, Id(a), BooleanLit(True)))]))])"""
        self.assertTrue(TestAST.test(input,expect,358))
        
    def test_simple_program59(self):
        input = """func main(bool a, number x, string b)
        begin
            if (a > 2) a <- a+ 1
            else return b+1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None), VarDecl(Id(x), NumberType, None, None), VarDecl(Id(b), StringType, None, None)], Block([If((BinaryOp(>, Id(a), NumLit(2.0)), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), [], Return(BinaryOp(+, Id(b), NumLit(1.0))))]))])"""
        self.assertTrue(TestAST.test(input,expect,359))
        
    def test_simple_program60(self):
        input = """func main(bool a)
        begin
            if (a >= 2+1) a <- a[1]
            else return true
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([If((BinaryOp(>=, Id(a), BinaryOp(+, NumLit(2.0), NumLit(1.0))), AssignStmt(Id(a), ArrayCell(Id(a), [NumLit(1.0)]))), [], Return(BooleanLit(True)))]))])"""
        self.assertTrue(TestAST.test(input,expect,360))
        
    def test_simple_program61(self):
        input = """func main(bool a)
        begin
            if (a+6 > 2/1)
            a <- a+ 1
            else return b+1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([If((BinaryOp(>, BinaryOp(+, Id(a), NumLit(6.0)), BinaryOp(/, NumLit(2.0), NumLit(1.0))), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), [], Return(BinaryOp(+, Id(b), NumLit(1.0))))]))])"""
        self.assertTrue(TestAST.test(input,expect,361))
        
    def test_simple_program62(self):
        input = """func main(bool a)
        begin
            if (a+6 > 2/1)
            a <- a+ 1
            elif ( 4 != 2 )
             return b+1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([If((BinaryOp(>, BinaryOp(+, Id(a), NumLit(6.0)), BinaryOp(/, NumLit(2.0), NumLit(1.0))), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), [(BinaryOp(!=, NumLit(4.0), NumLit(2.0)), Return(BinaryOp(+, Id(b), NumLit(1.0))))], None)]))])"""
        self.assertTrue(TestAST.test(input,expect,362))
        
    def test_simple_program63(self):
        input = """func main(bool a)
        begin
            if (a+6 > 2/1)
            a <- a+ 1
            elif ( 4 != 2 )
            return b+1
            else readString()
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([If((BinaryOp(>, BinaryOp(+, Id(a), NumLit(6.0)), BinaryOp(/, NumLit(2.0), NumLit(1.0))), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), [(BinaryOp(!=, NumLit(4.0), NumLit(2.0)), Return(BinaryOp(+, Id(b), NumLit(1.0))))], CallStmt(Id(readString), []))]))])"""
        self.assertTrue(TestAST.test(input,expect,363))
        
    def test_simple_program64(self):
        input = """
        func main(bool a)
        begin
            if (a[1]+6 > 2/1%2-1+1)
            a <- a+ 1
            elif ( 4 != 2 )
            return b+1
            elif (1==1) readString()
            elif ( 2 <= a+true) writeNumber(a)
            elif ( a[foo(10)] > _12do() ) readNumber()
            elif ( not false ) readBool()
            elif ( not true ) writeBool(true)
            elif ( c ==ccc ) writeString("ss\\t\\r\\f kkokok")
            else return 1
            return 0
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([If((BinaryOp(>, BinaryOp(+, ArrayCell(Id(a), [NumLit(1.0)]), NumLit(6.0)), BinaryOp(+, BinaryOp(-, BinaryOp(%, BinaryOp(/, NumLit(2.0), NumLit(1.0)), NumLit(2.0)), NumLit(1.0)), NumLit(1.0))), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), [(BinaryOp(!=, NumLit(4.0), NumLit(2.0)), Return(BinaryOp(+, Id(b), NumLit(1.0)))), (BinaryOp(==, NumLit(1.0), NumLit(1.0)), CallStmt(Id(readString), [])), (BinaryOp(<=, NumLit(2.0), BinaryOp(+, Id(a), BooleanLit(True))), CallStmt(Id(writeNumber), [Id(a)])), (BinaryOp(>, ArrayCell(Id(a), [CallExpr(Id(foo), [NumLit(10.0)])]), CallExpr(Id(_12do), [])), CallStmt(Id(readNumber), [])), (UnaryOp(not, BooleanLit(True)), CallStmt(Id(readBool), [])), (UnaryOp(not, BooleanLit(True)), CallStmt(Id(writeBool), [BooleanLit(True)])), (BinaryOp(==, Id(c), Id(ccc)), CallStmt(Id(writeString), [StringLit(ss\\t\\r\\f kkokok)]))], Return(NumLit(1.0))), Return(NumLit(0.0))]))])"""
        self.assertTrue(TestAST.test(input,expect,364))
        
    def test_simple_program65(self):
        input = """func main(bool a)
        begin
            if (a+6 > 2/1)
            a <- a+ 1
            elif ( 4 != 2 )

            return b+1
            else begin
                    c <-1
                    alo()
                end

        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([If((BinaryOp(>, BinaryOp(+, Id(a), NumLit(6.0)), BinaryOp(/, NumLit(2.0), NumLit(1.0))), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), [(BinaryOp(!=, NumLit(4.0), NumLit(2.0)), Return(BinaryOp(+, Id(b), NumLit(1.0))))], Block([AssignStmt(Id(c), NumLit(1.0)), CallStmt(Id(alo), [])]))]))])"""
        self.assertTrue(TestAST.test(input,expect,365))
        
    def test_simple_program66(self):
        input = """func main(bool a)
        begin

            for i until i <2 by -1
                writeNumber(i)
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([For(Id(i), BinaryOp(<, Id(i), NumLit(2.0)), UnaryOp(-, NumLit(1.0)), CallStmt(Id(writeNumber), [Id(i)]))]))])"""
        self.assertTrue(TestAST.test(input,expect,366))
        
    def test_simple_program67(self):
        input = """func main(bool a)
        begin
            if (a+6 > 2/1)
            a <- a+ 1
            elif ( 4 != 2 )
             return b+1
            else a <- a+1

            for i until i +2=1 by foo()[1+12,a] +1
                writeNumber(i)
            break
            continue
            return true
            foo()
            var a <- foo(1,2,3,"aaa")
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([If((BinaryOp(>, BinaryOp(+, Id(a), NumLit(6.0)), BinaryOp(/, NumLit(2.0), NumLit(1.0))), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), [(BinaryOp(!=, NumLit(4.0), NumLit(2.0)), Return(BinaryOp(+, Id(b), NumLit(1.0))))], AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), For(Id(i), BinaryOp(=, BinaryOp(+, Id(i), NumLit(2.0)), NumLit(1.0)), BinaryOp(+, ArrayCell(CallExpr(Id(foo), []), [BinaryOp(+, NumLit(1.0), NumLit(12.0)), Id(a)]), NumLit(1.0)), CallStmt(Id(writeNumber), [Id(i)])), Break, Continue, Return(BooleanLit(True)), CallStmt(Id(foo), []), VarDecl(Id(a), None, var, CallExpr(Id(foo), [NumLit(1.0), NumLit(2.0), NumLit(3.0), StringLit(aaa)]))]))])"""
        self.assertTrue(TestAST.test(input,expect,367))
    def test_simple_program68(self):
        input = """func main(bool a)
        begin
            if (a+6 > 2/1)
            a <- a+ 1
            elif ( 4 != 2 )
             return b+1
            else a <- a+1

            for i until i +2=1 by foo()[1+12,a] +1
                writeNumber(i)
            break
            continue
            return true
            foo()
            var a <- foo(1,2,3,"aaa")
            if ( c >1 ) begin
            for i until i > 2 by 1
            begin
                string a
                string b <- "333"
            end
            end
        end

        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([If((BinaryOp(>, BinaryOp(+, Id(a), NumLit(6.0)), BinaryOp(/, NumLit(2.0), NumLit(1.0))), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), [(BinaryOp(!=, NumLit(4.0), NumLit(2.0)), Return(BinaryOp(+, Id(b), NumLit(1.0))))], AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), For(Id(i), BinaryOp(=, BinaryOp(+, Id(i), NumLit(2.0)), NumLit(1.0)), BinaryOp(+, ArrayCell(CallExpr(Id(foo), []), [BinaryOp(+, NumLit(1.0), NumLit(12.0)), Id(a)]), NumLit(1.0)), CallStmt(Id(writeNumber), [Id(i)])), Break, Continue, Return(BooleanLit(True)), CallStmt(Id(foo), []), VarDecl(Id(a), None, var, CallExpr(Id(foo), [NumLit(1.0), NumLit(2.0), NumLit(3.0), StringLit(aaa)])), If((BinaryOp(>, Id(c), NumLit(1.0)), Block([For(Id(i), BinaryOp(>, Id(i), NumLit(2.0)), NumLit(1.0), Block([VarDecl(Id(a), StringType, None, None), VarDecl(Id(b), StringType, None, StringLit(333))]))])), [], None)]))])"""
        self.assertTrue(TestAST.test(input,expect,368))
    def test_simple_program69(self):
        input = """func main(bool a)
        begin
            if (a+6 > 2/1)
            a <- a+ 1
            elif ( 4 != 2 )
             return b+1
            else a <- a+1

            for i until i +2=1 by foo()[1+12,a] +1
                writeNumber(i)
            break
            continue
            return true
            foo()
            var a <- foo(1,2,3,"aaa")
            dynamic b
            var a <- a[1]
            number c <- 3
            if ( c >1 ) begin
            for i until i > 2 by 1
            begin
                string a
                string b <- "333"
            end
            end
            siu <- siu
            return 1+1+siu
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([If((BinaryOp(>, BinaryOp(+, Id(a), NumLit(6.0)), BinaryOp(/, NumLit(2.0), NumLit(1.0))), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), [(BinaryOp(!=, NumLit(4.0), NumLit(2.0)), Return(BinaryOp(+, Id(b), NumLit(1.0))))], AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), For(Id(i), BinaryOp(=, BinaryOp(+, Id(i), NumLit(2.0)), NumLit(1.0)), BinaryOp(+, ArrayCell(CallExpr(Id(foo), []), [BinaryOp(+, NumLit(1.0), NumLit(12.0)), Id(a)]), NumLit(1.0)), CallStmt(Id(writeNumber), [Id(i)])), Break, Continue, Return(BooleanLit(True)), CallStmt(Id(foo), []), VarDecl(Id(a), None, var, CallExpr(Id(foo), [NumLit(1.0), NumLit(2.0), NumLit(3.0), StringLit(aaa)])), VarDecl(Id(b), None, dynamic, None), VarDecl(Id(a), None, var, ArrayCell(Id(a), [NumLit(1.0)])), VarDecl(Id(c), NumberType, None, NumLit(3.0)), If((BinaryOp(>, Id(c), NumLit(1.0)), Block([For(Id(i), BinaryOp(>, Id(i), NumLit(2.0)), NumLit(1.0), Block([VarDecl(Id(a), StringType, None, None), VarDecl(Id(b), StringType, None, StringLit(333))]))])), [], None), AssignStmt(Id(siu), Id(siu)), Return(BinaryOp(+, BinaryOp(+, NumLit(1.0), NumLit(1.0)), Id(siu)))]))])"""
        self.assertTrue(TestAST.test(input,expect,369))
        
    def test_simple_program70(self):
        input = """func main(bool a)
        begin
            if (a+6 > 2/1)
            a <- a+ 1
            elif ( 4 != 2 )
             return b+1
        end
        func heartsteel( number no_hu_1000_so ) begin
            wow<-1
            string ezreal_30
            var ksante <- 2
            break
            return wow
        end

        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([If((BinaryOp(>, BinaryOp(+, Id(a), NumLit(6.0)), BinaryOp(/, NumLit(2.0), NumLit(1.0))), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), [(BinaryOp(!=, NumLit(4.0), NumLit(2.0)), Return(BinaryOp(+, Id(b), NumLit(1.0))))], None)])), FuncDecl(Id(heartsteel), [VarDecl(Id(no_hu_1000_so), NumberType, None, None)], Block([AssignStmt(Id(wow), NumLit(1.0)), VarDecl(Id(ezreal_30), StringType, None, None), VarDecl(Id(ksante), None, var, NumLit(2.0)), Break, Return(Id(wow))]))])"""
        self.assertTrue(TestAST.test(input,expect,370))
        
    def test_simple_program71(self):
        input = """var a <- 3
        dynamic b <- "111"
        string c <-a
        number h
        func main(bool a)
        begin
            if (a+6 > 2/1)
            a <- a+ 1
            elif ( 4 != 2 )
            return b+1
        end
        """
        expect = """Program([VarDecl(Id(a), None, var, NumLit(3.0)), VarDecl(Id(b), None, dynamic, StringLit(111)), VarDecl(Id(c), StringType, None, Id(a)), VarDecl(Id(h), NumberType, None, None), FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([If((BinaryOp(>, BinaryOp(+, Id(a), NumLit(6.0)), BinaryOp(/, NumLit(2.0), NumLit(1.0))), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), [(BinaryOp(!=, NumLit(4.0), NumLit(2.0)), Return(BinaryOp(+, Id(b), NumLit(1.0))))], None)]))])"""
        self.assertTrue(TestAST.test(input,expect,371))
        
    def test_simple_program72(self):
        input = """func main(bool a) return a+1
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0))))])"""
        self.assertTrue(TestAST.test(input,expect,372))
        
    def test_simple_program73(self):
        input = """var a <-foo(a)
var b <- a[1.2e1,1.32,1.,a[foo(3)[23]],"111"]
## sssssssss
number arr[1,2] <- [[1,2],[2,3]]

        """
        expect = """Program([VarDecl(Id(a), None, var, CallExpr(Id(foo), [Id(a)])), VarDecl(Id(b), None, var, ArrayCell(Id(a), [NumLit(12.0), NumLit(1.32), NumLit(1.0), ArrayCell(Id(a), [ArrayCell(CallExpr(Id(foo), [NumLit(3.0)]), [NumLit(23.0)])]), StringLit(111)])), VarDecl(Id(arr), ArrayType([NumLit(1.0), NumLit(2.0)], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(2.0), NumLit(3.0))))])"""
        self.assertTrue(TestAST.test(input,expect,373))
        
    def test_simple_program74(self):
        input = """func main() ##ssss\\n fffdedededededed

begin
##\\ \\n eeeeeeeeeeee
aaaaaaaaaaaaaa <-a
end

        """
        expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(aaaaaaaaaaaaaa), Id(a))]))])"""
        self.assertTrue(TestAST.test(input,expect,374))
        
    def test_simple_program75(self):
        input = """func main()
func foo()
func alo(number x) return 1
var a <- main()
dynamic a <-main
number a[111] <- [1,23,foo(10)]
func ri(string h) begin
number r
number s
r <- 2.0
number a[5]
number b[5]
s <- r * r * 3.14
a[0] <- s
end

        """
        expect = """Program([FuncDecl(Id(main), [], None), FuncDecl(Id(foo), [], None), FuncDecl(Id(alo), [VarDecl(Id(x), NumberType, None, None)], Return(NumLit(1.0))), VarDecl(Id(a), None, var, CallExpr(Id(main), [])), VarDecl(Id(a), None, dynamic, Id(main)), VarDecl(Id(a), ArrayType([NumLit(111.0)], NumberType), None, ArrayLit(NumLit(1.0), NumLit(23.0), CallExpr(Id(foo), [NumLit(10.0)]))), FuncDecl(Id(ri), [VarDecl(Id(h), StringType, None, None)], Block([VarDecl(Id(r), NumberType, None, None), VarDecl(Id(s), NumberType, None, None), AssignStmt(Id(r), NumLit(2.0)), VarDecl(Id(a), ArrayType([NumLit(5.0)], NumberType), None, None), VarDecl(Id(b), ArrayType([NumLit(5.0)], NumberType), None, None), AssignStmt(Id(s), BinaryOp(*, BinaryOp(*, Id(r), Id(r)), NumLit(3.14))), AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), Id(s))]))])"""
        self.assertTrue(TestAST.test(input,expect,375))
        
    def test_simple_program76(self):
        input = """var a <-1
func main()
func foo()
func alo(number x) return 1
var a <- main()
dynamic a <-main
number a[111] <- [1,23,foo(10)]
func ri(string h) begin
number r
number s
r <- 2.0
number a[5]
number b[5]
s <- r * r * 3.14
a[0] <- s
end
##ddddddddddddddddddddddddddddddddd
        """
        expect = """Program([VarDecl(Id(a), None, var, NumLit(1.0)), FuncDecl(Id(main), [], None), FuncDecl(Id(foo), [], None), FuncDecl(Id(alo), [VarDecl(Id(x), NumberType, None, None)], Return(NumLit(1.0))), VarDecl(Id(a), None, var, CallExpr(Id(main), [])), VarDecl(Id(a), None, dynamic, Id(main)), VarDecl(Id(a), ArrayType([NumLit(111.0)], NumberType), None, ArrayLit(NumLit(1.0), NumLit(23.0), CallExpr(Id(foo), [NumLit(10.0)]))), FuncDecl(Id(ri), [VarDecl(Id(h), StringType, None, None)], Block([VarDecl(Id(r), NumberType, None, None), VarDecl(Id(s), NumberType, None, None), AssignStmt(Id(r), NumLit(2.0)), VarDecl(Id(a), ArrayType([NumLit(5.0)], NumberType), None, None), VarDecl(Id(b), ArrayType([NumLit(5.0)], NumberType), None, None), AssignStmt(Id(s), BinaryOp(*, BinaryOp(*, Id(r), Id(r)), NumLit(3.14))), AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), Id(s))]))])"""
        self.assertTrue(TestAST.test(input,expect,376))
        
    def test_simple_program77(self):
        input = """func isPrime(number x)
func main()
begin
number x <- readNumber()
if (isPrime(x)) writeString("Yes")
else writeString("No")
end

        """
        expect = """Program([FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], None), FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, CallExpr(Id(readNumber), [])), If((CallExpr(Id(isPrime), [Id(x)]), CallStmt(Id(writeString), [StringLit(Yes)])), [], CallStmt(Id(writeString), [StringLit(No)]))]))])"""
        self.assertTrue(TestAST.test(input,expect,377))
        
    def test_simple_program78(self):
        input = """func areDivisors(number num1, number num2)
return ((num1 % num2 = 0) or (num2 % num1 = 0))
func main()
begin
var num1 <- readNumber()
var num2 <- readNumber()
if (areDivisors(num1, num2)) writeString("Yes")
else writeString("No")
end
        """
        expect = """Program([FuncDecl(Id(areDivisors), [VarDecl(Id(num1), NumberType, None, None), VarDecl(Id(num2), NumberType, None, None)], Return(BinaryOp(or, BinaryOp(=, BinaryOp(%, Id(num1), Id(num2)), NumLit(0.0)), BinaryOp(=, BinaryOp(%, Id(num2), Id(num1)), NumLit(0.0))))), FuncDecl(Id(main), [], Block([VarDecl(Id(num1), None, var, CallExpr(Id(readNumber), [])), VarDecl(Id(num2), None, var, CallExpr(Id(readNumber), [])), If((CallExpr(Id(areDivisors), [Id(num1), Id(num2)]), CallStmt(Id(writeString), [StringLit(Yes)])), [], CallStmt(Id(writeString), [StringLit(No)]))]))])"""
        self.assertTrue(TestAST.test(input,expect,378))
        
    def test_simple_program79(self):
        input = """func areDivisors(number num1, number num2)
return ((num1 % num2 = 0) or (num2 % num1 = 0))
func main()
begin
var num1 <- readNumber()
var num2 <- readNumber()
if (areDivisors(num1, num2)) writeString("Yes")
else writeString("No")
end
        """
        expect = """Program([FuncDecl(Id(areDivisors), [VarDecl(Id(num1), NumberType, None, None), VarDecl(Id(num2), NumberType, None, None)], Return(BinaryOp(or, BinaryOp(=, BinaryOp(%, Id(num1), Id(num2)), NumLit(0.0)), BinaryOp(=, BinaryOp(%, Id(num2), Id(num1)), NumLit(0.0))))), FuncDecl(Id(main), [], Block([VarDecl(Id(num1), None, var, CallExpr(Id(readNumber), [])), VarDecl(Id(num2), None, var, CallExpr(Id(readNumber), [])), If((CallExpr(Id(areDivisors), [Id(num1), Id(num2)]), CallStmt(Id(writeString), [StringLit(Yes)])), [], CallStmt(Id(writeString), [StringLit(No)]))]))])"""
        self.assertTrue(TestAST.test(input,expect,379))
    def test_simple_program80(self):
        input = """func areDivisors(number num1, number num2) ###sssssssdf/r/n\\n\\r\\d\\g\\c
return ((num1 % num2 = 0) or (num2 % num1 = 0))
func main()
begin
var num1 <- readNumber()  ##ddddd
var num2 <- readNumber()  ##ssssss
if (areDivisors(num1, num2)) writeString("Yes")
else writeString("No")
end  ##eeeeeeeeeeeeeeeee

        """
        expect = """Program([FuncDecl(Id(areDivisors), [VarDecl(Id(num1), NumberType, None, None), VarDecl(Id(num2), NumberType, None, None)], Return(BinaryOp(or, BinaryOp(=, BinaryOp(%, Id(num1), Id(num2)), NumLit(0.0)), BinaryOp(=, BinaryOp(%, Id(num2), Id(num1)), NumLit(0.0))))), FuncDecl(Id(main), [], Block([VarDecl(Id(num1), None, var, CallExpr(Id(readNumber), [])), VarDecl(Id(num2), None, var, CallExpr(Id(readNumber), [])), If((CallExpr(Id(areDivisors), [Id(num1), Id(num2)]), CallStmt(Id(writeString), [StringLit(Yes)])), [], CallStmt(Id(writeString), [StringLit(No)]))]))])"""
        self.assertTrue(TestAST.test(input,expect,380))

    def test_simple_program81(self):
        input = """func main(bool x) return (2-2) or 1
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(x), BoolType, None, None)], Return(BinaryOp(or, BinaryOp(-, NumLit(2.0), NumLit(2.0)), NumLit(1.0))))])"""
        self.assertTrue(TestAST.test(input,expect,381))
        
    def test_simple_program82(self):
        input = """func main(string x, string c) return 2+c...d
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(x), StringType, None, None), VarDecl(Id(c), StringType, None, None)], Return(BinaryOp(..., BinaryOp(+, NumLit(2.0), Id(c)), Id(d))))])"""
        self.assertTrue(TestAST.test(input,expect,382))
        
    def test_simple_program83(self):
        input = """func _aa_12Ad(number _32ssd___s )
begin
continue
for i until ((i >1) or (i<22) or (o<21))  by 1
    continue
if ((a >1) or (s <2))
return 1


elif (ss>2) break
else a<-d
end
        """
        expect = """Program([FuncDecl(Id(_aa_12Ad), [VarDecl(Id(_32ssd___s), NumberType, None, None)], Block([Continue, For(Id(i), BinaryOp(or, BinaryOp(or, BinaryOp(>, Id(i), NumLit(1.0)), BinaryOp(<, Id(i), NumLit(22.0))), BinaryOp(<, Id(o), NumLit(21.0))), NumLit(1.0), Continue), If((BinaryOp(or, BinaryOp(>, Id(a), NumLit(1.0)), BinaryOp(<, Id(s), NumLit(2.0))), Return(NumLit(1.0))), [(BinaryOp(>, Id(ss), NumLit(2.0)), Break)], AssignStmt(Id(a), Id(d)))]))])"""
        self.assertTrue(TestAST.test(input,expect,383))
        
    def test_simple_program84(self):
        input = """func _aa_12Ad(number _32ssd___s )
begin
continue
for i until ((i >1) or (i<22) or (o<21))  by 1
    continue
if ((a >1) or (s <2))
return 1

elif (ss>2) break
else a<-d
wow(11111)
doo(111)
end

string her <- "12133\\r \\f \\b ww2~~!!#@$@+__S>D?A?>>   "
func her() return sd[11,2,f(s0)]
        """
        expect = """Program([FuncDecl(Id(_aa_12Ad), [VarDecl(Id(_32ssd___s), NumberType, None, None)], Block([Continue, For(Id(i), BinaryOp(or, BinaryOp(or, BinaryOp(>, Id(i), NumLit(1.0)), BinaryOp(<, Id(i), NumLit(22.0))), BinaryOp(<, Id(o), NumLit(21.0))), NumLit(1.0), Continue), If((BinaryOp(or, BinaryOp(>, Id(a), NumLit(1.0)), BinaryOp(<, Id(s), NumLit(2.0))), Return(NumLit(1.0))), [(BinaryOp(>, Id(ss), NumLit(2.0)), Break)], AssignStmt(Id(a), Id(d))), CallStmt(Id(wow), [NumLit(11111.0)]), CallStmt(Id(doo), [NumLit(111.0)])])), VarDecl(Id(her), StringType, None, StringLit(12133\\r \\f \\b ww2~~!!#@$@+__S>D?A?>>   )), FuncDecl(Id(her), [], Return(ArrayCell(Id(sd), [NumLit(11.0), NumLit(2.0), CallExpr(Id(f), [Id(s0)])])))])"""
        self.assertTrue(TestAST.test(input,expect,384))
        
    def test_simple_program85(self):
        input = """func main(bool a)
        begin
            if (a+6 > 2/1)
            a <- a+ 1
            else return b+1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([If((BinaryOp(>, BinaryOp(+, Id(a), NumLit(6.0)), BinaryOp(/, NumLit(2.0), NumLit(1.0))), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), [], Return(BinaryOp(+, Id(b), NumLit(1.0))))]))])"""
        self.assertTrue(TestAST.test(input,expect,385))
        
    def test_simple_program86(self):
        input = """func main(bool a)

        return a+1

        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0))))])"""
        self.assertTrue(TestAST.test(input,expect,386))
        
    def test_simple_program87(self):
        input = """number pi <- 3.14

func area_circle(number radius)
begin
number area <- radius * radius * pi
return area
end

func main()
begin
number radius <- readNumber()
writeNumber(area_circle(radius))
end
        """
        expect = """Program([VarDecl(Id(pi), NumberType, None, NumLit(3.14)), FuncDecl(Id(area_circle), [VarDecl(Id(radius), NumberType, None, None)], Block([VarDecl(Id(area), NumberType, None, BinaryOp(*, BinaryOp(*, Id(radius), Id(radius)), Id(pi))), Return(Id(area))])), FuncDecl(Id(main), [], Block([VarDecl(Id(radius), NumberType, None, CallExpr(Id(readNumber), [])), CallStmt(Id(writeNumber), [CallExpr(Id(area_circle), [Id(radius)])])]))])"""
        self.assertTrue(TestAST.test(input,expect,387))
        
    def test_simple_program88(self):
        input = """number pi <- 3.14

func area_circle(number radius)
begin
number area <- radius * radius * pi
return area
end

func swapnumber(number a, number b)
begin
number c
number c <- a
a<-b
b<-c
number result[2] <- [a,b]
return result
end


func main()
begin
number radius <- readNumber()
writeNumber(area_circle(radius))
number a <-3
number b <-6
number result[2] <- swapnumber(a,b)
writeNumber(result[0])
writeNumber(result[1])
end

        """
        expect = """Program([VarDecl(Id(pi), NumberType, None, NumLit(3.14)), FuncDecl(Id(area_circle), [VarDecl(Id(radius), NumberType, None, None)], Block([VarDecl(Id(area), NumberType, None, BinaryOp(*, BinaryOp(*, Id(radius), Id(radius)), Id(pi))), Return(Id(area))])), FuncDecl(Id(swapnumber), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([VarDecl(Id(c), NumberType, None, None), VarDecl(Id(c), NumberType, None, Id(a)), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(c)), VarDecl(Id(result), ArrayType([NumLit(2.0)], NumberType), None, ArrayLit(Id(a), Id(b))), Return(Id(result))])), FuncDecl(Id(main), [], Block([VarDecl(Id(radius), NumberType, None, CallExpr(Id(readNumber), [])), CallStmt(Id(writeNumber), [CallExpr(Id(area_circle), [Id(radius)])]), VarDecl(Id(a), NumberType, None, NumLit(3.0)), VarDecl(Id(b), NumberType, None, NumLit(6.0)), VarDecl(Id(result), ArrayType([NumLit(2.0)], NumberType), None, CallExpr(Id(swapnumber), [Id(a), Id(b)])), CallStmt(Id(writeNumber), [ArrayCell(Id(result), [NumLit(0.0)])]), CallStmt(Id(writeNumber), [ArrayCell(Id(result), [NumLit(1.0)])])]))])"""
        self.assertTrue(TestAST.test(input,expect,388))
        
    def test_simple_program89(self):
        input = """func length_array(number a)
begin
number i <-0
number length <- 0
for i until i > 99999 by 1
    begin
    if (a[i] == true)
        length <- length +1
    else break
    end
return length
end

func sum_of_array(number a)
begin
    number length <- length_array(a)
    number i <-0
    number sum <-0
    for i until i >= length by 1
            sum <- sum + a[i]
    return sum
end


func main()
begin
number a[9] <- [1,2,3,4,5,6,7,8,9]
writeNumber(sum_of_array(a))
end

        """
        expect = """Program([FuncDecl(Id(length_array), [VarDecl(Id(a), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), VarDecl(Id(length), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>, Id(i), NumLit(99999.0)), NumLit(1.0), Block([If((BinaryOp(==, ArrayCell(Id(a), [Id(i)]), BooleanLit(True)), AssignStmt(Id(length), BinaryOp(+, Id(length), NumLit(1.0)))), [], Break)])), Return(Id(length))])), FuncDecl(Id(sum_of_array), [VarDecl(Id(a), NumberType, None, None)], Block([VarDecl(Id(length), NumberType, None, CallExpr(Id(length_array), [Id(a)])), VarDecl(Id(i), NumberType, None, NumLit(0.0)), VarDecl(Id(sum), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(length)), NumLit(1.0), AssignStmt(Id(sum), BinaryOp(+, Id(sum), ArrayCell(Id(a), [Id(i)])))), Return(Id(sum))])), FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([NumLit(9.0)], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0), NumLit(6.0), NumLit(7.0), NumLit(8.0), NumLit(9.0))), CallStmt(Id(writeNumber), [CallExpr(Id(sum_of_array), [Id(a)])])]))])"""
        self.assertTrue(TestAST.test(input,expect,389))
        
    def test_simple_program90(self):
        input = """func neural_network_forward(number x, number weight)
begin
    number result[10]
    for i until x[-1] by 1
    begin
        for j until w[i,-1] by 1
            begin
                sum <- x[i] * w[i,j]
                result[i] <- sum
            end
    end
    return result
end
        """
        expect = """Program([FuncDecl(Id(neural_network_forward), [VarDecl(Id(x), NumberType, None, None), VarDecl(Id(weight), NumberType, None, None)], Block([VarDecl(Id(result), ArrayType([NumLit(10.0)], NumberType), None, None), For(Id(i), ArrayCell(Id(x), [UnaryOp(-, NumLit(1.0))]), NumLit(1.0), Block([For(Id(j), ArrayCell(Id(w), [Id(i), UnaryOp(-, NumLit(1.0))]), NumLit(1.0), Block([AssignStmt(Id(sum), BinaryOp(*, ArrayCell(Id(x), [Id(i)]), ArrayCell(Id(w), [Id(i), Id(j)]))), AssignStmt(ArrayCell(Id(result), [Id(i)]), Id(sum))]))])), Return(Id(result))]))])"""
        self.assertTrue(TestAST.test(input,expect,390))
        
    def test_simple_program91(self):
        input = """string a <- "Hello World!"

        """
        expect = """Program([VarDecl(Id(a), StringType, None, StringLit(Hello World!))])"""
        self.assertTrue(TestAST.test(input,expect,391))

    def test_simple_program92(self):
        input = """string a <- "Hello World!"
func main()  return writeString(a)

        """
        expect = """Program([VarDecl(Id(a), StringType, None, StringLit(Hello World!)), FuncDecl(Id(main), [], Return(CallExpr(Id(writeString), [Id(a)])))])"""
        self.assertTrue(TestAST.test(input,expect,392))
        
    def test_simple_program93(self):
        input = """string a <- "Hello World!"
string c <- "My name is Phuc"
string b <- "Nice to meet human"
string z[3] <- [a,b,c]
func main()  return writeString(z)

        """
        expect = """Program([VarDecl(Id(a), StringType, None, StringLit(Hello World!)), VarDecl(Id(c), StringType, None, StringLit(My name is Phuc)), VarDecl(Id(b), StringType, None, StringLit(Nice to meet human)), VarDecl(Id(z), ArrayType([NumLit(3.0)], StringType), None, ArrayLit(Id(a), Id(b), Id(c))), FuncDecl(Id(main), [], Return(CallExpr(Id(writeString), [Id(z)])))])"""
        self.assertTrue(TestAST.test(input,expect,393))
        
    def test_simple_program94(self):
        input = """func main(bool a)
        begin
            if (a+6 > 2/1)
            a <- a+ 1
            elif (1+1 >3) begin
            return "aaa"
            end
            elif (1 ==2) return 1
            else return b+1
        end
        """
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), BoolType, None, None)], Block([If((BinaryOp(>, BinaryOp(+, Id(a), NumLit(6.0)), BinaryOp(/, NumLit(2.0), NumLit(1.0))), AssignStmt(Id(a), BinaryOp(+, Id(a), NumLit(1.0)))), [(BinaryOp(>, BinaryOp(+, NumLit(1.0), NumLit(1.0)), NumLit(3.0)), Block([Return(StringLit(aaa))])), (BinaryOp(==, NumLit(1.0), NumLit(2.0)), Return(NumLit(1.0)))], Return(BinaryOp(+, Id(b), NumLit(1.0))))]))])"""
        self.assertTrue(TestAST.test(input,expect,394))
        
    def test_simple_program95(self):
        input = """string a <- "Hello World!" ## string a
string c <- "My name is Phuc"  ## name
string b <- "Nice to meet human" ## introduce
string z[3] <- [a,b,c]  ## ##bii#
func main() ###main
  return writeString(z)

        """
        expect = """Program([VarDecl(Id(a), StringType, None, StringLit(Hello World!)), VarDecl(Id(c), StringType, None, StringLit(My name is Phuc)), VarDecl(Id(b), StringType, None, StringLit(Nice to meet human)), VarDecl(Id(z), ArrayType([3.0], StringType), None, ArrayLit(Id(a), Id(b), Id(c))), FuncDecl(Id(main), [], Return(CallExpr(Id(writeString), [Id(z)])))])"""
        self.assertTrue(TestAST.test(input,expect,395))

    def test_simple_program96(self):
        input = """string a <- "Hello World!" ## string a
string c <- "My name is Phuc"  ## name
string b <- "Nice to meet human" ## introduce
string z[3] <- [a,b,c]  ## ##bii#
func main() ###main
  return writeString(z)

func main()
begin
    bool a[22,2,3] <- [true,false,not true,true or false, 1 or 2, a+1=12]
    bool b[2] <- a[a[a[a[main(a)]]]]
    string c <- a[1] + b[2]
    return c - main(h) * (1+2) /4 %2
end

        """
        expect = """Program([VarDecl(Id(a), StringType, None, StringLit(Hello World!)), VarDecl(Id(c), StringType, None, StringLit(My name is Phuc)), VarDecl(Id(b), StringType, None, StringLit(Nice to meet human)), VarDecl(Id(z), ArrayType([NumLit(3.0)], StringType), None, ArrayLit(Id(a), Id(b), Id(c))), FuncDecl(Id(main), [], Return(CallExpr(Id(writeString), [Id(z)]))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([NumLit(22.0), NumLit(2.0), NumLit(3.0)], BoolType), None, ArrayLit(BooleanLit(True), BooleanLit(True), UnaryOp(not, BooleanLit(True)), BinaryOp(or, BooleanLit(True), BooleanLit(True)), BinaryOp(or, NumLit(1.0), NumLit(2.0)), BinaryOp(=, BinaryOp(+, Id(a), NumLit(1.0)), NumLit(12.0)))), VarDecl(Id(b), ArrayType([NumLit(2.0)], BoolType), None, ArrayCell(Id(a), [ArrayCell(Id(a), [ArrayCell(Id(a), [ArrayCell(Id(a), [CallExpr(Id(main), [Id(a)])])])])])), VarDecl(Id(c), StringType, None, BinaryOp(+, ArrayCell(Id(a), [NumLit(1.0)]), ArrayCell(Id(b), [NumLit(2.0)]))), Return(BinaryOp(-, Id(c), BinaryOp(%, BinaryOp(/, BinaryOp(*, CallExpr(Id(main), [Id(h)]), BinaryOp(+, NumLit(1.0), NumLit(2.0))), NumLit(4.0)), NumLit(2.0))))]))])"""
        self.assertTrue(TestAST.test(input,expect,396))

    def test_simple_program97(self):
        input = """func mainercanh(bool boollit) return binzetdapoet ## Xuan Dan
        """
        expect = """Program([FuncDecl(Id(mainercanh), [VarDecl(Id(boollit), BoolType, None, None)], Return(Id(binzetdapoet)))])"""
        self.assertTrue(TestAST.test(input,expect,397))
        
    def test_simple_program98(self):
        input = """string c <- "Hen em vao motj ngay mua thu nang dep, \\n toi tang em mot bo hoa tuoi tham, \\n trao em mot nu hon nong nan"
        """
        expect = """Program([VarDecl(Id(c), StringType, None, StringLit(Hen em vao motj ngay mua thu nang dep, \\n toi tang em mot bo hoa tuoi tham, \\n trao em mot nu hon nong nan))])"""
        self.assertTrue(TestAST.test(input,expect,398))
        
    def test_simple_program99(self):
        input = """number poet <- "Xuan Dang den ben em, gio xuan tuyet voi ong mat troi"
        func poetry(string poet)
        begin
            bool Phuc_dep_trai <- true ## false is eliminated
            string Phuc <- " "
            return Phuc * 9999999
        end
        """
        expect = """Program([VarDecl(Id(poet), NumberType, None, StringLit(Xuan Dang den ben em, gio xuan tuyet voi ong mat troi)), FuncDecl(Id(poetry), [VarDecl(Id(poet), StringType, None, None)], Block([VarDecl(Id(Phuc_dep_trai), BoolType, None, BooleanLit(True)), VarDecl(Id(Phuc), StringType, None, StringLit( )), Return(BinaryOp(*, Id(Phuc), NumLit(9999999.0)))]))])"""
        self.assertTrue(TestAST.test(input,expect,399))
        
    def test_simple_program100(self):
        input = """func foo(number a[5], string b)
begin
var i <- 0
for i until i >= 5 by 1
begin
a[i] <- i * i + 5
end
return -1
end
        """
        expect = """Program([VarDecl(Id(c), StringType, None, StringLit(Hen em vao motj ngay mua thu nang dep, \\n toi tang em mot bo hoa tuoi tham, \\n trao em mot nu hon nong nan))])"""
        self.assertTrue(TestAST.test(input,expect,400))
        
    
    def test_simple_program101(self):
        input = """number a[1] <- [[1,2],[2]]
        """
        expect = """Program([VarDecl(Id(c), StringType, None, StringLit(Hen em vao motj ngay mua thu nang dep, \\n toi tang em mot bo hoa tuoi tham, \\n trao em mot nu hon nong nan))])"""
        self.assertTrue(TestAST.test(input,expect,401))
    



   