from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):

    def visitProgram(self,ctx:ZCodeParser.ProgramContext):
        return Program(decl = ctx.manydeclare().accept(self))
    
    def visitManydeclare(self, ctx: ZCodeParser.ManydeclareContext):
        return [dec.accept(self) for dec in ctx.declare()]
    
    
    def visitDeclare(self, ctx: ZCodeParser.DeclareContext):
        if ctx.variable_dec():
            return ctx.variable_dec().accept(self)
        elif ctx.function_dec():
            return ctx.function_dec().accept(self)
        
######################### VARIABLES DECLARATIONS ####################
        
    def visitVariable_dec(self, ctx: ZCodeParser.Variable_decContext):
        if ctx.vardec_normal_type() :
            return ctx.vardec_normal_type().accept(self)
        elif ctx.vardec_implicit_type():
            return ctx.vardec_implicit_type().accept(self)
        elif ctx.vardec_array_type():
            return ctx.vardec_array_type().accept(self)
        
    def visitVardec_normal_type(self, ctx: ZCodeParser.Vardec_normal_typeContext):
        typee = ctx.variable_type().accept(self)
        id, init = ctx.single_dec().accept(self)
        return VarDecl(name = id, varType = typee, varInit = init, modifier = None)
    
    def visitVariable_type(self, ctx: ZCodeParser.Variable_typeContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOL():
            return BoolType()

    
    def visitSingle_dec(self, ctx: ZCodeParser.Single_decContext):
        id = Id(name = ctx.IDENTIFIER().getText())
        init = ctx.value_init().accept(self) if ctx.value_init() else None
        return id, init
    
    def visitValue_init(self, ctx: ZCodeParser.Value_initContext):
        return ctx.expr().accept(self)
    
    
    ###### EXPR ######
    
    def visitExpr(self, ctx: ZCodeParser.ExprContext):
        if ctx.getChildCount() == 1:
            return ctx.expr1(0).accept(self)
        else:
            return BinaryOp(op = ctx.getChild(1).getText(), left = ctx.expr1(0).accept(self), right = ctx.expr1(1).accept(self))

    def visitExpr1(self, ctx: ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return ctx.expr2(0).accept(self)
        else:
            return BinaryOp(op = ctx.getChild(1).getText(), left = ctx.expr2(0).accept(self), right = ctx.expr2(1).accept(self))
        
    def visitExpr2(self, ctx: ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return ctx.expr3().accept(self)
        else:
            return BinaryOp(op = ctx.getChild(1).getText(), left = ctx.expr2().accept(self), right = ctx.expr3().accept(self))
        
    def visitExpr3(self, ctx: ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return ctx.expr4().accept(self)
        else:
            return BinaryOp(op = ctx.getChild(1).getText(), left = ctx.expr3().accept(self), right = ctx.expr4().accept(self))
        
    def visitExpr4(self, ctx: ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return ctx.expr5().accept(self)
        else:
            return BinaryOp(op = ctx.getChild(1).getText(), left = ctx.expr4().accept(self), right = ctx.expr5().accept(self))
    
    def visitExpr5(self, ctx: ZCodeParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return ctx.expr6().accept(self)
        else:
            return UnaryOp(op = ctx.getChild(0).getText(), operand = ctx.getChild(1).accept(self))
    
    def visitExpr6(self, ctx: ZCodeParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return ctx.expr7().accept(self)
        else:
            return UnaryOp(op = ctx.getChild(0).getText(), operand = ctx.getChild(1).accept(self))    
    
    def visitExpr7(self, ctx: ZCodeParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return ctx.operand().accept(self)
        else:
            return ctx.expr().accept(self)    


    def visitOperand(self, ctx: ZCodeParser.OperandContext):
        if ctx.variables():
            return ctx.variables().accept(self)
        else:
            return ctx.function_call().accept(self)    
        
    def visitVariables(self, ctx: ZCodeParser.VariablesContext):
        if ctx.element_expr():
            id, list_number =  ctx.element_expr().accept(self)
            return ArrayCell(arr = id, idx = list_number)
        elif ctx.array_value():
            return ctx.array_value().accept(self)
        elif ctx.IDENTIFIER():
            return Id(name = ctx.IDENTIFIER().getText())
        elif ctx.NUMBER_LIT():
            return NumberLiteral(value = self.float_define(ctx.NUMBER_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(value = ctx.STRING_LIT().getText())
        else:
            return BooleanLiteral(value = ctx.BOOLEAN_LIT().getText())
        
    def float_define(self,a:str):
        if a[0] == '.':
            return float('0' + a)
        else:
            return float(a)
        
        
    def visitFunction_call(self, ctx: ZCodeParser.Function_callContext):
        id = Id(name = ctx.IDENTIFIER().getText())
        argument = ctx.comma_separate_argument().accept(self)
        return CallExpr(name = id, args = argument)
        
    def visitComma_separate_argument(self, ctx: ZCodeParser.Comma_separate_argumentContext):
        return [each_expr.accept(self) for each_expr in ctx.expr()] if ctx.expr() else []


    def visitVardec_implicit_type(self, ctx: ZCodeParser.Vardec_implicit_typeContext):
        if ctx.var_type():
            return ctx.var_type().accept(self)
        else:
            return ctx.dynamic_type().accept(self)       
        
    def visitVar_type(self, ctx: ZCodeParser.Var_typeContext):
        init = ctx.value_init().accept(self)
        id = Id(name = ctx.IDENTIFIER().getText())
        return VarDecl(name = id, varType = None, varInit = init, modifier = "var")
    
    def visitDynamic_type(self, ctx: ZCodeParser.Dynamic_typeContext):
        init = ctx.value_init().accept(self) if ctx.value_init() else None
        id = Id(name = ctx.IDENTIFIER().getText())
        return VarDecl(name = id, varType = None, varInit = init, modifier = "dynamic")
    
    
    def visitVardec_array_type(self, ctx: ZCodeParser.Vardec_array_typeContext):
        typee = ctx.variable_type().accept(self)
        id =Id(name = ctx.IDENTIFIER().getText())
        cell = ctx.comma_separate_number_one().accept(self)
        init = ctx.array_assign().accept(self) if ctx.array_assign() else None
        return VarDecl(name = id, varType = ArrayType(size = cell, eleType = typee), varInit = init)
    
    def visitArray_assign(self, ctx: ZCodeParser.Array_assignContext):
        return ctx.getChild(1).accept(self)
    
    
    
    
    def visitComma_separate_number_one(self, ctx: ZCodeParser.Comma_separate_number_oneContext):
        return [self.float_define(number.getText()) for number in ctx.NUMBER_LIT()]
    
    def visitComma_separate_number(self, ctx: ZCodeParser.Comma_separate_numberContext):
        return [NumberLiteral(value = self.float_define(number.getText())) for number in ctx.NUMBER_LIT()]
        
    ##### PARAMETER
    
    def visitParameter(self, ctx: ZCodeParser.ParameterContext):
        if ctx.vardec_normal_param():
            return ctx.vardec_normal_param().accept(self)
        else:
            return ctx.vardec_array_param().accept(self)
        
    def visitVardec_normal_param(self, ctx: ZCodeParser.Vardec_normal_paramContext):
        typee = ctx.variable_type().accept(self)
        id = Id(name = ctx.IDENTIFIER().getText())
        return VarDecl(name = id, varType = typee )
    
    def visitVardec_array_param(self, ctx: ZCodeParser.Vardec_array_paramContext):
        typee = ctx.variable_type().accept(self)
        id,list_number = ctx.array_dec().accept(self)
        #array_type = ArrayType(size = [1,2,3], eleType = typee)
        return VarDecl(name = id, varType = ArrayType(size = list_number, eleType = typee) )
    
    def visitArray_dec(self, ctx: ZCodeParser.Array_decContext):
        id = Id(name = ctx.IDENTIFIER().getText())
        list_number = ctx.comma_separate_number().accept(self)
        return id, list_number
    
    ################ FUNCTION DECCLARATION #####################
    
    def visitFunction_dec(self, ctx: ZCodeParser.Function_decContext):
        id = Id(name = ctx.IDENTIFIER().getText())
        param = ctx.comma_separate_param().accept(self)
        body = ctx.body().accept(self)
        return FuncDecl(name = id, param = param, body = body)
    
    def visitComma_separate_param(self, ctx: ZCodeParser.Comma_separate_paramContext):
        return [each_param.accept(self) for each_param in ctx.parameter()] if ctx.parameter() else []

    def visitBody(self, ctx: ZCodeParser.BodyContext):
        if ctx.return_stmt():
            return ctx.return_stmt().accept(self)
        elif ctx.block_stmt():
            return ctx.block_stmt().accept(self)
        else:
            return None
        
        
    ################## STATEMENT ################
    def visitReturn_stmt(self, ctx: ZCodeParser.Return_stmtContext):
        if ctx.expr():
            return Return(expr = ctx.expr().accept(self))
        else:
            return Return(expr = None)
        
    def visitBlock_stmt(self, ctx: ZCodeParser.Block_stmtContext):
        list_stmt = ctx.list_statement_nullable().accept(self)
        return Block(stmt = list_stmt)
    
    def visitList_statement_nullable(self, ctx: ZCodeParser.List_statement_nullableContext):
        return [stmt.accept(self) for stmt in ctx.statement()] if ctx.statement() else []
    
    
    def visitVariable_dec_stmt(self, ctx: ZCodeParser.Variable_dec_stmtContext):
        return ctx.variable_dec().accept(self)
    
    def visitAssign_stmt(self, ctx: ZCodeParser.Assign_stmtContext):
        lhs = ctx.lhs().accept(self)
        expr = ctx.expr().accept(self)
        return Assign(lhs = lhs, rhs = expr)
    
    def visitLhs(self, ctx: ZCodeParser.LhsContext):
        if ctx.IDENTIFIER():
            return Id(name = ctx.IDENTIFIER().getText())
        else:
            id, list_number =  ctx.element_expr().accept(self)
            return ArrayCell(arr = id, idx = list_number)
    
    def visitIf_stmt(self, ctx: ZCodeParser.If_stmtContext):
        if_expr, then_stmt = ctx.if_part().accept(self)
        elif_part = [elif_stmt.accept(self) for elif_stmt in ctx.elif_part()] if ctx.elif_part() else []
        else_part = ctx.else_part().accept(self) if ctx.else_part() else None
        return If(expr = if_expr, thenStmt = then_stmt, elifStmt = elif_part, elseStmt = else_part)
    
    def visitIf_part(self, ctx: ZCodeParser.If_partContext):
        return ctx.condition_action().accept(self)
    
    def visitCondition_action(self, ctx: ZCodeParser.Condition_actionContext):
        if_expr = ctx.expr().accept(self)
        then_stmt = ctx.statement().accept(self)
        return if_expr, then_stmt
    
    def visitStatement(self, ctx: ZCodeParser.StatementContext):
        return ctx.getChild(0).accept(self)
    
    def visitElif_part(self, ctx: ZCodeParser.Elif_partContext):
        return ctx.condition_action().accept(self)
    
    def visitElse_part(self, ctx: ZCodeParser.Else_partContext):
        return ctx.statement().accept(self)
    
    
    def visitFor_stmt(self, ctx: ZCodeParser.For_stmtContext):
        name = Id(name = ctx.IDENTIFIER().getText())
        cond = ctx.expr(0).accept(self)
        updt = ctx.expr(1).accept(self)
        body = ctx.statement().accept(self)
        return For(name = name, condExpr = cond, updExpr = updt, body = body)
    
    
    def visitBreak_stmt(self, ctx: ZCodeParser.Break_stmtContext):
        return Break()
    
    def visitContinue_stmt(self, ctx: ZCodeParser.Continue_stmtContext):
        return Continue()
    
    def visitFunc_call_stmt(self, ctx: ZCodeParser.Func_call_stmtContext):
        id = Id(name = ctx.IDENTIFIER().getText())
        argument = ctx.comma_separate_argument().accept(self)
        return CallStmt(name = id, args = argument)
    
    def visitArray_value(self, ctx: ZCodeParser.Array_valueContext):
        list_expr = ctx.comma_separate_expr().accept(self)
        return ArrayLiteral(value = list_expr)
    
    def visitComma_separate_expr(self, ctx: ZCodeParser.Comma_separate_exprContext):
        return [expr.accept(self) for expr in ctx.expr()]
    
        
    def visitElement_expr(self, ctx: ZCodeParser.Element_exprContext):
        id = ctx.expr_array_type().accept(self)
        list_expr = ctx.index_operators().accept(self)
        return id, list_expr
    
    def visitExpr_array_type(self, ctx: ZCodeParser.Expr_array_typeContext):
        if ctx.IDENTIFIER():
            return Id(name = ctx.IDENTIFIER().getText())
        else:
            return ctx.function_call().accept(self)
        
    def visitIndex_operators(self, ctx: ZCodeParser.Index_operatorsContext):
        list_exp = [self.visit(ctx.expr())]
        
        return list_exp + self.visit(ctx.index_operators()) if ctx.index_operators() else list_exp
