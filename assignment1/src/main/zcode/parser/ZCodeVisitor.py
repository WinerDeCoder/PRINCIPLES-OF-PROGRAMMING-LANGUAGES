# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#manydeclare.
    def visitManydeclare(self, ctx:ZCodeParser.ManydeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declare.
    def visitDeclare(self, ctx:ZCodeParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_dec.
    def visitFunction_dec(self, ctx:ZCodeParser.Function_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#comma_separate_param.
    def visitComma_separate_param(self, ctx:ZCodeParser.Comma_separate_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_tail.
    def visitParam_tail(self, ctx:ZCodeParser.Param_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variable_dec_stmt.
    def visitVariable_dec_stmt(self, ctx:ZCodeParser.Variable_dec_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assign_stmt.
    def visitAssign_stmt(self, ctx:ZCodeParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#scalar_var.
    def visitScalar_var(self, ctx:ZCodeParser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_part.
    def visitIf_part(self, ctx:ZCodeParser.If_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_part.
    def visitElif_part(self, ctx:ZCodeParser.Elif_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_part.
    def visitElse_part(self, ctx:ZCodeParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#condition_action.
    def visitCondition_action(self, ctx:ZCodeParser.Condition_actionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#condition_expr.
    def visitCondition_expr(self, ctx:ZCodeParser.Condition_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#number_variable.
    def visitNumber_variable(self, ctx:ZCodeParser.Number_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#update_expr.
    def visitUpdate_expr(self, ctx:ZCodeParser.Update_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call_stmt.
    def visitFunc_call_stmt(self, ctx:ZCodeParser.Func_call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#comma_separate_argument.
    def visitComma_separate_argument(self, ctx:ZCodeParser.Comma_separate_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_statement_nullable.
    def visitList_statement_nullable(self, ctx:ZCodeParser.List_statement_nullableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement_tail.
    def visitStatement_tail(self, ctx:ZCodeParser.Statement_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variable_dec.
    def visitVariable_dec(self, ctx:ZCodeParser.Variable_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardec_normal_type.
    def visitVardec_normal_type(self, ctx:ZCodeParser.Vardec_normal_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardec_implicit_type.
    def visitVardec_implicit_type(self, ctx:ZCodeParser.Vardec_implicit_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_type.
    def visitVar_type(self, ctx:ZCodeParser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dynamic_type.
    def visitDynamic_type(self, ctx:ZCodeParser.Dynamic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardec_array_type.
    def visitVardec_array_type(self, ctx:ZCodeParser.Vardec_array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#single_dec.
    def visitSingle_dec(self, ctx:ZCodeParser.Single_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#value_init.
    def visitValue_init(self, ctx:ZCodeParser.Value_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter.
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardec_normal_param.
    def visitVardec_normal_param(self, ctx:ZCodeParser.Vardec_normal_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardec_array_param.
    def visitVardec_array_param(self, ctx:ZCodeParser.Vardec_array_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#build_in_func.
    def visitBuild_in_func(self, ctx:ZCodeParser.Build_in_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#readNumber.
    def visitReadNumber(self, ctx:ZCodeParser.ReadNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#writeNumber.
    def visitWriteNumber(self, ctx:ZCodeParser.WriteNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#readBool.
    def visitReadBool(self, ctx:ZCodeParser.ReadBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#writeBool.
    def visitWriteBool(self, ctx:ZCodeParser.WriteBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#readString.
    def visitReadString(self, ctx:ZCodeParser.ReadStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#writeString.
    def visitWriteString(self, ctx:ZCodeParser.WriteStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#element_expr.
    def visitElement_expr(self, ctx:ZCodeParser.Element_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_operators.
    def visitIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_array_type.
    def visitExpr_array_type(self, ctx:ZCodeParser.Expr_array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variables.
    def visitVariables(self, ctx:ZCodeParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_call.
    def visitFunction_call(self, ctx:ZCodeParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_dec.
    def visitArray_dec(self, ctx:ZCodeParser.Array_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_value.
    def visitArray_value(self, ctx:ZCodeParser.Array_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#comma_separate_number.
    def visitComma_separate_number(self, ctx:ZCodeParser.Comma_separate_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#digit_tail.
    def visitDigit_tail(self, ctx:ZCodeParser.Digit_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#comma_separate_expr.
    def visitComma_separate_expr(self, ctx:ZCodeParser.Comma_separate_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_tail.
    def visitExpr_tail(self, ctx:ZCodeParser.Expr_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_separate.
    def visitNewline_separate(self, ctx:ZCodeParser.Newline_separateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_separate_optional.
    def visitNewline_separate_optional(self, ctx:ZCodeParser.Newline_separate_optionalContext):
        return self.visitChildren(ctx)



del ZCodeParser