//Name: NGuyễn Phước Nguyên Phúc
//MSSV: 2053342
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: manydeclare EOF;

manydeclare: declare+;
declare: function_dec|variable_dec; //variable_tail ;

//variable_tail: (func_dec) variable_tail | ;



function_dec: FUNCTION IDENTIFIER LRB comma_separate_param RRB  (newline_separate_optional return_stmt|newline_separate_optional block_stmt)?; //newline_separate ;


comma_separate_param: parameter param_tail | ;

param_tail: CM parameter param_tail | ;





//////////////////////////////////////// STATEMENT //////////////////////////////////////


statement: (variable_dec_stmt|assign_stmt|if_stmt|for_stmt|break_stmt|continue_stmt|return_stmt|func_call_stmt|block_stmt); //newline_separate;


//____________________________ VARIABLE DEC STATEMENT ___________________________//


variable_dec_stmt: variable_dec ;


//____________________________ ASSIGN STATEMENT ___________________________//


assign_stmt: lhs ASSIGN expr ;

lhs: scalar_var | array_dec ;


scalar_var: IDENTIFIER;


//______________________________IF STATEMENT _________________________________//


if_stmt: if_part elif_part* else_part? ;


//------------ COMPONENT --------------//

if_part: IF condition_action  ;

elif_part:	ELIF condition_action ;


else_part: ELSE condition_action ;


condition_action: LRB condition_expr RRB newline_separate_optional statement ;


condition_expr: expr ;


//_________________________________ FOR STATEMENT ___________________________________//


for_stmt: FOR number_variable UNTIL condition_expr BY update_expr newline_separate_optional statement ;


//------------- COMPONENT --------------//

number_variable: scalar_var ;

update_expr: expr ;


//________________________________ BREAK STATEMENT __________________________//


break_stmt: BREAK ;


//________________________________ CONTINUE STATEMENT _________________________//


continue_stmt: CONTINUE ;


//_______________________________ RETURN STATEMENT ____________________________//


return_stmt: RETURN expr? ;


//______________________________ FUNCTION CALL STATEMENT ____________________________//


func_call_stmt: function_call ;


comma_separate_argument:  expr expr_tail | ;



//______________________________ BLOCK STATEMENT ____________________________-//


//block_stmt: BEGIN newline_separate list_statement_nullable END newline_separate_optional;

block_stmt: BEGIN  list_statement_nullable END newline_separate_optional;


//------------- COMPONENT ----------------//


list_statement_nullable: statement statement_tail | ;

statement_tail:  statement statement_tail | ;


//////////////////////////////////////////////////////////////////////////////////////////////



//////////////////////////////////// VARIABLES AND FUNCTIONS ///////////////////////////////////


//______________________________ VARIABLES _____________________________//


variable_dec:	(vardec_normal_type|vardec_implicit_type|vardec_array_type )  | parameter;


//------------- component ---------------//


vardec_normal_type:	(NUMBER|STRING|BOOL) single_dec ;

vardec_implicit_type: var_type | dynamic_type ;

var_type:	VAR IDENTIFIER value_init ;

dynamic_type:	DYNAMIC IDENTIFIER value_init? ;

vardec_array_type:	(NUMBER|STRING|BOOL) IDENTIFIER LSB comma_separate_number RSB value_init?  ;

single_dec:	IDENTIFIER value_init? ;

value_init:	ASSIGN expr ;



parameter: vardec_normal_param|vardec_array_param ;


vardec_normal_param: (NUMBER|STRING|BOOL) IDENTIFIER ;

vardec_array_param: (NUMBER|STRING|BOOL) array_dec ;


//_______________________________ FUNCTION ______________________________//




///////////////////////////////////////////////////////////////////////////////



//////////////////////////////////// BUILD IN FUNCTION /////////////////////////////

build_in_func: readNumber |  writeNumber | readBool | writeBool | readString | writeString ;

readNumber	: 'readNumber' ;					//Read an number from keyboard and return it.

writeNumber	: 'writeNumber' LRB expr RRB;    	//Write an number to the screen.

readBool	: 'readBool' LRB RRB ;              //Read an boolean value from keyboard and return it.

writeBool	: 'writeBool' LRB expr RRB;         //Write an boolean value to the screen.

readString	: 'readString' LRB RRB ;           	//Read an string from keyboard and return it.

writeString	: 'writeString' LRB expr RRB; 	    //Write an string to the screen.


///////////////////////////////////////////////////////////////////////////////////


//////////////////////////////////// EXPRESSION ////////////////////////////////


expr    :	expr1 THREE_DOT expr1		
		|	expr1 ;

expr1   :	expr2 (EQUAL|DOUBLE_EQUAL|NOT_EQUAL|SMALLER|SMALLER_EQUAL|LARGER|LARGER_EQUAL) expr2		
		|	expr2 ;

expr2	:	expr2 (AND|OR) expr3		
		|	expr3 ;

expr3	:	expr3 (PLUS|MINUS) expr4		
		|	expr4 ;

expr4	:	expr4 (MUL|DIV) expr5		
		|	expr5 ;

expr5	:	NOT expr5		
		|	expr6 ;

expr6	:	MINUS expr6		
		|	expr7 ;

expr7	:	LRB expr RRB
		|	operand ;


element_expr	:	expr_array_type LSB index_operators RSB ;

index_operators :	expr
				|	expr CM index_operators ;


expr_array_type: IDENTIFIER | function_call ;


//---------- operands --------------//


operand: variables| function_call;


variables: IDENTIFIER | NUMBER_LIT | BOOLEAN_LIT | STRING_LIT | element_expr;


function_call: build_in_func |  IDENTIFIER LRB comma_separate_argument RRB ;  


////////////////////////////////////////////////////////////




//////////////////////////////////  ARRAY  /////////////////////////////////


array_dec: IDENTIFIER LSB comma_separate_number RSB;

array_value: LSB comma_separate_expr RSB;


//------------- component ----------------//


comma_separate_number: NUMBER_LIT digit_tail ;

digit_tail: CM NUMBER_LIT digit_tail | ;


comma_separate_expr: expr expr_tail ;

expr_tail: CM expr expr_tail | ;






//////////////////////////////////// OPERATORS ///////////////////////////////////////


PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT_OP: 'not';
AND_OP: 'and';
OR_OP: 'or';
EQUAL: '=';
ASSIGN: '<-';
NOT_EQUAL: '!=';
SMALLER: '<';
SMALLER_EQUAL: '<=';
LARGER: '>';
LARGER_EQUAL: '>=';
THREE_DOT: '...';
DOUBLE_EQUAL: '==';


//////////////////////////////////// KEY WORDS //////////////////////////////////////

FUNCTION: 'func';
TRUE: 'true';
FALSE: 'false' ;
NUMBER: 'number' ;
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';

FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE:'else';
ELIF: 'elif' ;
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND:'and';
OR: 'or';


//////////////////////////////////// IDENTIFIER //////////////////////////////////


//////////////////////////////////// LITERALS /////////////////////////////////////

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;



NUMBER_LIT: INTEGER_PART EXPONENT_PART | INTEGER_PART DECIMAL_PART EXPONENT_PART? | [0-9]+;


BOOLEAN_LIT: TRUE|FALSE;

STRING_LIT: '"' (Character|Escape_seq|Double_quote_instring)* '"'  {self.text = self.text[1:-1]} ;


//--------- component ------------//


fragment DIGIT: [0-9];
fragment INTEGER_PART: DIGIT+;
fragment DECIMAL_PART: '.'DIGIT*;
fragment EXPONENT_PART: ('e'|'E') ('+'|'-')? DIGIT+;


fragment Character: ~([\b]| [\n] | [\t] | [\f] | [\r] | [\\] | [\'] | ["] )    ;
fragment Escape_seq: '\\' ([bntrf'\\])  ;
fragment Double_quote_instring: '\'"';




//////////////////////////////////// COMMENT ///////////////////////////////////////

//////////////////////////////////// SEPARATORS ///////////////////////////////////////


newline_separate: NEWLINE+ ;

newline_separate_optional: NEWLINE* ;


CM:',' ;
NEWLINE: '\n';


///////// brackets ////////


LRB: '(';
RRB: ')';

LSB: '[';
RSB: ']';


COMMENT: '##' ([.]| '\n')*  -> skip ;


//////////////////////////////////// CATCH ERROR ///////////////////////////////////


fragment Illigal_escape: '\\' ~[bntrf'\\] | '\\' ;

WS : [ \t\b\f]+ -> skip ; // skip spaces, tabs, newlines

ILLEGAL_ESCAPE:
	'"'(Character|Escape_seq|Double_quote_instring)* Illigal_escape
{
    string_to_illegal = str(self.text)
    raise IllegalEscape(string_to_illegal[1:])
};

UNCLOSE_STRING:
	'"' (Character|Escape_seq|Double_quote_instring)*  ([\b\f\r\n\t\\] | EOF) {
	if self.text[-1] in ['\b', '\t', '\f', '\r', '\n' ]:
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};

ERROR_TOKEN:
	. {raise ErrorToken(self.text)
};



//////////////////////////////////////////////////////////////////////////////////