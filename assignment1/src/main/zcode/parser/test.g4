grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
  language=Python3;
}

program: declare_list EOF;

declare_list: declare declare_list | list_NL declare_list |;

declare: function_declare ;
// declare: IDENTIFIER;

// !--------------PARSER RULE----------------

function_declare: FUNC IDENTIFIER LPAREN params_list RPAREN 
list_NL? body?;

body: stmt_block | stmt_return;

params_list: param param_tail | list_NL params_list| ;

param_tail: COMMA list_NL? param param_tail | list_NL param_tail |;

param: variable_declare ;

  

//* Statement

statement: stmt_declare list_NL
| stmt_assign list_NL
| stmt_if
| stmt_for 
| stmt_break list_NL
| stmt_continue list_NL
| stmt_return list_NL
| stmt_call list_NL
| stmt_block
;

  

stmt_declare: variable_declare;

variable_declare: normal_declare | array_declare;

  

normal_declare: typ IDENTIFIER value_initialization?
| VAR IDENTIFIER value_initialization
| DYNAMIC IDENTIFIER value_initialization?
;

array_declare: typ IDENTIFIER LBRACK sizes RBRACK value_initialization?;

sizes: NUMBER_LITERAL sizes_tail;

sizes_tail: COMMA NUMBER_LITERAL sizes_tail |;

typ: NUMBER | BOOL | STRING ;

value_initialization:ASSIGN expression ;


stmt_assign: lhs ASSIGN expression;
lhs: IDENTIFIER | expression_index;
  

stmt_if: IF expression list_NL? statement stmt_if_tail;

stmt_if_tail: ELSE list_NL? statement 
| ELSEIF expression list_NL? statement stmt_if_tail 
|;

  

stmt_for: FOR number_variable UNTIL expression BY expression list_NL? statement;

number_variable: IDENTIFIER;

  

stmt_break: BREAK;

  

stmt_continue: CONTINUE;

stmt_return: RETURN expression;

  

stmt_call: IDENTIFIER LPAREN arguments_list RPAREN;

arguments_list: expression arguments_tail |;

arguments_tail: COMMA expression arguments_tail |;

stmt_block: BEGIN list_NL 
statements_list 
END list_NL;

  

statements_list: statement statements_list |;

  

//* Expression

relational_op: EQUAL_ | EQUAL__ | NOTEQUAL | LESS | GREATER | LESSEQUAL | GREATEREQUAL;

subexpression:LPAREN expression RPAREN ;

expression: expression_relat DOTS expression_relat | expression_relat;

expression_relat: expression_logic relational_op expression_logic |expression_logic ;

expression_logic: expression_logic (AND|OR) expression_bina1|expression_bina1;

expression_bina1: expression_bina1 (PLUS|MINUS) expression_bina2|expression_bina2;

expression_bina2: expression_bina2 (MUL|DIV|MOD) expression_unary | expression_unary;

expression_unary: NOT expression_unary
| MINUS expression_unary
| expression_index
;

expression_index: expression_index LBRACK indexoperator RBRACK
|operand
;

indexoperator: expression indexoperator_tail;  
indexoperator_tail: COMMA expression indexoperator_tail |;

operand: constant | functioncall | IDENTIFIER | subexpression ;

constant: NUMBER_LITERAL | STRING_LITERAL | BOOL_LITERAL | araay_literal;

expression_list: expression expression_tail |;
expression_tail: COMMA expression expression_tail |;

functioncall: IDENTIFIER LPAREN arguments_list RPAREN;
  

// !--------------LEXER RULE----------------
// * --------Keyword--------
fragment TRUE: 'true';
fragment FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';

IF: 'if';
ELSE: 'else';
ELSEIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';


// * --------Literal--------

araay_literal
: LBRACK expression_list  RBRACK;

// literal_list: constant literal_tail;
// literal_tail: COMMA constant literal_tail |; 
  

STRING_LITERAL
  : (DQ STR_CHAR* DQ) {self.text = self.text[1:-1]}
  ;

fragment ESC
  : '\\' ( 'b' | 'f' | 'n' | 'r' | 't' | '\'' | '\\' ) | SQDQ
  ;
fragment STR_CHAR: ESC| ~['"\r\n\\];
  

BOOL_LITERAL
  : TRUE
  | FALSE
  ;

NUMBER_LITERAL
  :IntegerLiteral DecimalLiteral? ExponentPart?;

fragment IntegerLiteral
  : [0-9]+;

  

fragment DecimalLiteral
  : '.' [0-9]*;

  

fragment ExponentPart

  : [eE] [+-]? [0-9]+;

  
IDENTIFIER
  : Letter (Letter | Digit)*
  ;

fragment Letter
  : [a-zA-Z_]
;
  

fragment Digit
  : [0-9]
  ;

// * --------Comment--------
COMMENT_CPP : '##' ~[\r\n]* -> skip ;

// *--------Operator--------
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL_: '=';
ASSIGN: '<-';
EQUAL__: '==';
NOTEQUAL: '!=';
LESS: '<';
GREATER: '>';
LESSEQUAL: '<=';
GREATEREQUAL: '>=';
DOTS: '...';
SM: ';';
DQ: '"';
SQDQ: '\'"';

//*--------Seprator--------
LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
COMMA: ',';

NL : ('\n' | '\r' '\n'?) {self.text = '\n'} ;
list_NL : NL list_NL | NL;

WS : [ \t\b\f]+ -> skip ;

UNCLOSE_STRING: DQ STR_CHAR* ( [\b\t\n\f\r\\] | EOF ) {raise UncloseString(self.text[1:])};

fragment ESCAPE_ILLEGAL: '\\' ~[btnfr'\\] | ~'\\' ;
ILLEGAL_ESCAPE: DQ STR_CHAR* ESCAPE_ILLEGAL{raise IllegalEscape(self.text[1:])};

ERROR_CHAR: . {raise ErrorToken(self.text)};