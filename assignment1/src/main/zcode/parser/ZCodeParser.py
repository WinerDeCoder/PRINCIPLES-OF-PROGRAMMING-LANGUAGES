# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3>")
        buf.write("\u01ed\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\3\2\3\2\3\2\3\3\6\3\u008f\n\3\r\3\16\3\u0090\3")
        buf.write("\4\3\4\5\4\u0095\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\5\5\u00a2\n\5\3\6\3\6\3\6\3\6\5\6\u00a8\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\5\7\u00af\n\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\5\b\u00ba\n\b\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\5\13\u00c4\n\13\3\f\3\f\3\r\3\r\7\r\u00ca\n")
        buf.write("\r\f\r\16\r\u00cd\13\r\3\r\5\r\u00d0\n\r\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\5\30\u00f6\n\30\3\31\3\31\3\32\3\32\3\32\3\32\5\32\u00fe")
        buf.write("\n\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u0109\n\34\3\35\3\35\3\35\3\35\5\35\u010f\n\35\3\36\3")
        buf.write("\36\3\36\5\36\u0114\n\36\3\36\5\36\u0117\n\36\3\37\3\37")
        buf.write("\3\37\3 \3 \5 \u011e\n \3!\3!\3!\3!\3\"\3\"\3\"\5\"\u0127")
        buf.write("\n\"\3#\3#\3#\3#\3#\3#\5#\u012f\n#\3$\3$\5$\u0133\n$\3")
        buf.write("%\3%\3%\3&\3&\5&\u013a\n&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3)\3)\5)\u0148\n)\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3-\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\5\60\u0168\n\60\3\61\3\61\3\61\3\61\3")
        buf.write("\61\5\61\u016f\n\61\3\62\3\62\3\62\3\62\3\62\3\62\7\62")
        buf.write("\u0177\n\62\f\62\16\62\u017a\13\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\7\63\u0182\n\63\f\63\16\63\u0185\13\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\7\64\u018d\n\64\f\64\16\64\u0190")
        buf.write("\13\64\3\65\3\65\3\65\5\65\u0195\n\65\3\66\3\66\3\66\5")
        buf.write("\66\u019a\n\66\3\67\3\67\3\67\3\67\3\67\5\67\u01a1\n\67")
        buf.write("\38\38\38\38\38\39\39\39\39\39\59\u01ad\n9\3:\3:\5:\u01b1")
        buf.write("\n:\3;\3;\5;\u01b5\n;\3<\3<\3<\3<\3<\5<\u01bc\n<\3=\3")
        buf.write("=\3=\3=\3=\3=\5=\u01c4\n=\3>\3>\3>\3>\3>\3?\3?\3?\3?\3")
        buf.write("@\3@\3@\3A\3A\3A\3A\5A\u01d6\nA\3B\3B\3B\3C\3C\3C\3C\3")
        buf.write("C\5C\u01e0\nC\3D\6D\u01e3\nD\rD\16D\u01e4\3E\7E\u01e8")
        buf.write("\nE\fE\16E\u01eb\13E\3E\2\5bdfF\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\2\7")
        buf.write("\3\2\35\37\5\2\21\21\23\27\31\31\3\2./\3\2\t\n\3\2\13")
        buf.write("\f\2\u01de\2\u008a\3\2\2\2\4\u008e\3\2\2\2\6\u0094\3\2")
        buf.write("\2\2\b\u0096\3\2\2\2\n\u00a7\3\2\2\2\f\u00ae\3\2\2\2\16")
        buf.write("\u00b9\3\2\2\2\20\u00bb\3\2\2\2\22\u00bd\3\2\2\2\24\u00c3")
        buf.write("\3\2\2\2\26\u00c5\3\2\2\2\30\u00c7\3\2\2\2\32\u00d1\3")
        buf.write("\2\2\2\34\u00d4\3\2\2\2\36\u00d7\3\2\2\2 \u00da\3\2\2")
        buf.write("\2\"\u00e0\3\2\2\2$\u00e2\3\2\2\2&\u00eb\3\2\2\2(\u00ed")
        buf.write("\3\2\2\2*\u00ef\3\2\2\2,\u00f1\3\2\2\2.\u00f3\3\2\2\2")
        buf.write("\60\u00f7\3\2\2\2\62\u00fd\3\2\2\2\64\u00ff\3\2\2\2\66")
        buf.write("\u0108\3\2\2\28\u010e\3\2\2\2:\u0116\3\2\2\2<\u0118\3")
        buf.write("\2\2\2>\u011d\3\2\2\2@\u011f\3\2\2\2B\u0123\3\2\2\2D\u0128")
        buf.write("\3\2\2\2F\u0130\3\2\2\2H\u0134\3\2\2\2J\u0139\3\2\2\2")
        buf.write("L\u013b\3\2\2\2N\u013e\3\2\2\2P\u0147\3\2\2\2R\u0149\3")
        buf.write("\2\2\2T\u014b\3\2\2\2V\u0150\3\2\2\2X\u0154\3\2\2\2Z\u0159")
        buf.write("\3\2\2\2\\\u015d\3\2\2\2^\u0167\3\2\2\2`\u016e\3\2\2\2")
        buf.write("b\u0170\3\2\2\2d\u017b\3\2\2\2f\u0186\3\2\2\2h\u0194\3")
        buf.write("\2\2\2j\u0199\3\2\2\2l\u01a0\3\2\2\2n\u01a2\3\2\2\2p\u01ac")
        buf.write("\3\2\2\2r\u01b0\3\2\2\2t\u01b4\3\2\2\2v\u01bb\3\2\2\2")
        buf.write("x\u01c3\3\2\2\2z\u01c5\3\2\2\2|\u01ca\3\2\2\2~\u01ce\3")
        buf.write("\2\2\2\u0080\u01d5\3\2\2\2\u0082\u01d7\3\2\2\2\u0084\u01df")
        buf.write("\3\2\2\2\u0086\u01e2\3\2\2\2\u0088\u01e9\3\2\2\2\u008a")
        buf.write("\u008b\5\4\3\2\u008b\u008c\7\2\2\3\u008c\3\3\2\2\2\u008d")
        buf.write("\u008f\5\6\4\2\u008e\u008d\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\5\3\2\2")
        buf.write("\2\u0092\u0095\5\b\5\2\u0093\u0095\5:\36\2\u0094\u0092")
        buf.write("\3\2\2\2\u0094\u0093\3\2\2\2\u0095\7\3\2\2\2\u0096\u0097")
        buf.write("\7\32\2\2\u0097\u0098\7\60\2\2\u0098\u0099\7\66\2\2\u0099")
        buf.write("\u009a\5\n\6\2\u009a\u00a1\7\67\2\2\u009b\u009c\5\u0088")
        buf.write("E\2\u009c\u009d\5.\30\2\u009d\u00a2\3\2\2\2\u009e\u009f")
        buf.write("\5\u0088E\2\u009f\u00a0\5\64\33\2\u00a0\u00a2\3\2\2\2")
        buf.write("\u00a1\u009b\3\2\2\2\u00a1\u009e\3\2\2\2\u00a1\u00a2\3")
        buf.write("\2\2\2\u00a2\t\3\2\2\2\u00a3\u00a4\5J&\2\u00a4\u00a5\5")
        buf.write("\f\7\2\u00a5\u00a8\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7\u00a3")
        buf.write("\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\13\3\2\2\2\u00a9\u00aa")
        buf.write("\7\64\2\2\u00aa\u00ab\5J&\2\u00ab\u00ac\5\f\7\2\u00ac")
        buf.write("\u00af\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae\u00a9\3\2\2\2")
        buf.write("\u00ae\u00ad\3\2\2\2\u00af\r\3\2\2\2\u00b0\u00ba\5\20")
        buf.write("\t\2\u00b1\u00ba\5\22\n\2\u00b2\u00ba\5\30\r\2\u00b3\u00ba")
        buf.write("\5$\23\2\u00b4\u00ba\5*\26\2\u00b5\u00ba\5,\27\2\u00b6")
        buf.write("\u00ba\5.\30\2\u00b7\u00ba\5\60\31\2\u00b8\u00ba\5\64")
        buf.write("\33\2\u00b9\u00b0\3\2\2\2\u00b9\u00b1\3\2\2\2\u00b9\u00b2")
        buf.write("\3\2\2\2\u00b9\u00b3\3\2\2\2\u00b9\u00b4\3\2\2\2\u00b9")
        buf.write("\u00b5\3\2\2\2\u00b9\u00b6\3\2\2\2\u00b9\u00b7\3\2\2\2")
        buf.write("\u00b9\u00b8\3\2\2\2\u00ba\17\3\2\2\2\u00bb\u00bc\5:\36")
        buf.write("\2\u00bc\21\3\2\2\2\u00bd\u00be\5\24\13\2\u00be\u00bf")
        buf.write("\7\22\2\2\u00bf\u00c0\5^\60\2\u00c0\23\3\2\2\2\u00c1\u00c4")
        buf.write("\5\26\f\2\u00c2\u00c4\5z>\2\u00c3\u00c1\3\2\2\2\u00c3")
        buf.write("\u00c2\3\2\2\2\u00c4\25\3\2\2\2\u00c5\u00c6\7\60\2\2\u00c6")
        buf.write("\27\3\2\2\2\u00c7\u00cb\5\32\16\2\u00c8\u00ca\5\34\17")
        buf.write("\2\u00c9\u00c8\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9")
        buf.write("\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd")
        buf.write("\u00cb\3\2\2\2\u00ce\u00d0\5\36\20\2\u00cf\u00ce\3\2\2")
        buf.write("\2\u00cf\u00d0\3\2\2\2\u00d0\31\3\2\2\2\u00d1\u00d2\7")
        buf.write("(\2\2\u00d2\u00d3\5 \21\2\u00d3\33\3\2\2\2\u00d4\u00d5")
        buf.write("\7*\2\2\u00d5\u00d6\5 \21\2\u00d6\35\3\2\2\2\u00d7\u00d8")
        buf.write("\7)\2\2\u00d8\u00d9\5 \21\2\u00d9\37\3\2\2\2\u00da\u00db")
        buf.write("\7\66\2\2\u00db\u00dc\5\"\22\2\u00dc\u00dd\7\67\2\2\u00dd")
        buf.write("\u00de\5\u0088E\2\u00de\u00df\5\16\b\2\u00df!\3\2\2\2")
        buf.write("\u00e0\u00e1\5^\60\2\u00e1#\3\2\2\2\u00e2\u00e3\7#\2\2")
        buf.write("\u00e3\u00e4\5&\24\2\u00e4\u00e5\7$\2\2\u00e5\u00e6\5")
        buf.write("\"\22\2\u00e6\u00e7\7%\2\2\u00e7\u00e8\5(\25\2\u00e8\u00e9")
        buf.write("\5\u0088E\2\u00e9\u00ea\5\16\b\2\u00ea%\3\2\2\2\u00eb")
        buf.write("\u00ec\5\26\f\2\u00ec\'\3\2\2\2\u00ed\u00ee\5^\60\2\u00ee")
        buf.write(")\3\2\2\2\u00ef\u00f0\7&\2\2\u00f0+\3\2\2\2\u00f1\u00f2")
        buf.write("\7\'\2\2\u00f2-\3\2\2\2\u00f3\u00f5\7 \2\2\u00f4\u00f6")
        buf.write("\5^\60\2\u00f5\u00f4\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6")
        buf.write("/\3\2\2\2\u00f7\u00f8\5x=\2\u00f8\61\3\2\2\2\u00f9\u00fa")
        buf.write("\5^\60\2\u00fa\u00fb\5\u0084C\2\u00fb\u00fe\3\2\2\2\u00fc")
        buf.write("\u00fe\3\2\2\2\u00fd\u00f9\3\2\2\2\u00fd\u00fc\3\2\2\2")
        buf.write("\u00fe\63\3\2\2\2\u00ff\u0100\7+\2\2\u0100\u0101\5\66")
        buf.write("\34\2\u0101\u0102\7,\2\2\u0102\u0103\5\u0088E\2\u0103")
        buf.write("\65\3\2\2\2\u0104\u0105\5\16\b\2\u0105\u0106\58\35\2\u0106")
        buf.write("\u0109\3\2\2\2\u0107\u0109\3\2\2\2\u0108\u0104\3\2\2\2")
        buf.write("\u0108\u0107\3\2\2\2\u0109\67\3\2\2\2\u010a\u010b\5\16")
        buf.write("\b\2\u010b\u010c\58\35\2\u010c\u010f\3\2\2\2\u010d\u010f")
        buf.write("\3\2\2\2\u010e\u010a\3\2\2\2\u010e\u010d\3\2\2\2\u010f")
        buf.write("9\3\2\2\2\u0110\u0114\5<\37\2\u0111\u0114\5> \2\u0112")
        buf.write("\u0114\5D#\2\u0113\u0110\3\2\2\2\u0113\u0111\3\2\2\2\u0113")
        buf.write("\u0112\3\2\2\2\u0114\u0117\3\2\2\2\u0115\u0117\5J&\2\u0116")
        buf.write("\u0113\3\2\2\2\u0116\u0115\3\2\2\2\u0117;\3\2\2\2\u0118")
        buf.write("\u0119\t\2\2\2\u0119\u011a\5F$\2\u011a=\3\2\2\2\u011b")
        buf.write("\u011e\5@!\2\u011c\u011e\5B\"\2\u011d\u011b\3\2\2\2\u011d")
        buf.write("\u011c\3\2\2\2\u011e?\3\2\2\2\u011f\u0120\7!\2\2\u0120")
        buf.write("\u0121\7\60\2\2\u0121\u0122\5H%\2\u0122A\3\2\2\2\u0123")
        buf.write("\u0124\7\"\2\2\u0124\u0126\7\60\2\2\u0125\u0127\5H%\2")
        buf.write("\u0126\u0125\3\2\2\2\u0126\u0127\3\2\2\2\u0127C\3\2\2")
        buf.write("\2\u0128\u0129\t\2\2\2\u0129\u012a\7\60\2\2\u012a\u012b")
        buf.write("\78\2\2\u012b\u012c\5~@\2\u012c\u012e\79\2\2\u012d\u012f")
        buf.write("\5H%\2\u012e\u012d\3\2\2\2\u012e\u012f\3\2\2\2\u012fE")
        buf.write("\3\2\2\2\u0130\u0132\7\60\2\2\u0131\u0133\5H%\2\u0132")
        buf.write("\u0131\3\2\2\2\u0132\u0133\3\2\2\2\u0133G\3\2\2\2\u0134")
        buf.write("\u0135\7\22\2\2\u0135\u0136\5^\60\2\u0136I\3\2\2\2\u0137")
        buf.write("\u013a\5L\'\2\u0138\u013a\5N(\2\u0139\u0137\3\2\2\2\u0139")
        buf.write("\u0138\3\2\2\2\u013aK\3\2\2\2\u013b\u013c\t\2\2\2\u013c")
        buf.write("\u013d\7\60\2\2\u013dM\3\2\2\2\u013e\u013f\t\2\2\2\u013f")
        buf.write("\u0140\5z>\2\u0140O\3\2\2\2\u0141\u0148\5R*\2\u0142\u0148")
        buf.write("\5T+\2\u0143\u0148\5V,\2\u0144\u0148\5X-\2\u0145\u0148")
        buf.write("\5Z.\2\u0146\u0148\5\\/\2\u0147\u0141\3\2\2\2\u0147\u0142")
        buf.write("\3\2\2\2\u0147\u0143\3\2\2\2\u0147\u0144\3\2\2\2\u0147")
        buf.write("\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148Q\3\2\2\2\u0149")
        buf.write("\u014a\7\3\2\2\u014aS\3\2\2\2\u014b\u014c\7\4\2\2\u014c")
        buf.write("\u014d\7\66\2\2\u014d\u014e\5^\60\2\u014e\u014f\7\67\2")
        buf.write("\2\u014fU\3\2\2\2\u0150\u0151\7\5\2\2\u0151\u0152\7\66")
        buf.write("\2\2\u0152\u0153\7\67\2\2\u0153W\3\2\2\2\u0154\u0155\7")
        buf.write("\6\2\2\u0155\u0156\7\66\2\2\u0156\u0157\5^\60\2\u0157")
        buf.write("\u0158\7\67\2\2\u0158Y\3\2\2\2\u0159\u015a\7\7\2\2\u015a")
        buf.write("\u015b\7\66\2\2\u015b\u015c\7\67\2\2\u015c[\3\2\2\2\u015d")
        buf.write("\u015e\7\b\2\2\u015e\u015f\7\66\2\2\u015f\u0160\5^\60")
        buf.write("\2\u0160\u0161\7\67\2\2\u0161]\3\2\2\2\u0162\u0163\5`")
        buf.write("\61\2\u0163\u0164\7\30\2\2\u0164\u0165\5`\61\2\u0165\u0168")
        buf.write("\3\2\2\2\u0166\u0168\5`\61\2\u0167\u0162\3\2\2\2\u0167")
        buf.write("\u0166\3\2\2\2\u0168_\3\2\2\2\u0169\u016a\5b\62\2\u016a")
        buf.write("\u016b\t\3\2\2\u016b\u016c\5b\62\2\u016c\u016f\3\2\2\2")
        buf.write("\u016d\u016f\5b\62\2\u016e\u0169\3\2\2\2\u016e\u016d\3")
        buf.write("\2\2\2\u016fa\3\2\2\2\u0170\u0171\b\62\1\2\u0171\u0172")
        buf.write("\5d\63\2\u0172\u0178\3\2\2\2\u0173\u0174\f\4\2\2\u0174")
        buf.write("\u0175\t\4\2\2\u0175\u0177\5d\63\2\u0176\u0173\3\2\2\2")
        buf.write("\u0177\u017a\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3")
        buf.write("\2\2\2\u0179c\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017c")
        buf.write("\b\63\1\2\u017c\u017d\5f\64\2\u017d\u0183\3\2\2\2\u017e")
        buf.write("\u017f\f\4\2\2\u017f\u0180\t\5\2\2\u0180\u0182\5f\64\2")
        buf.write("\u0181\u017e\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181\3")
        buf.write("\2\2\2\u0183\u0184\3\2\2\2\u0184e\3\2\2\2\u0185\u0183")
        buf.write("\3\2\2\2\u0186\u0187\b\64\1\2\u0187\u0188\5h\65\2\u0188")
        buf.write("\u018e\3\2\2\2\u0189\u018a\f\4\2\2\u018a\u018b\t\6\2\2")
        buf.write("\u018b\u018d\5h\65\2\u018c\u0189\3\2\2\2\u018d\u0190\3")
        buf.write("\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018fg")
        buf.write("\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0192\7-\2\2\u0192")
        buf.write("\u0195\5h\65\2\u0193\u0195\5j\66\2\u0194\u0191\3\2\2\2")
        buf.write("\u0194\u0193\3\2\2\2\u0195i\3\2\2\2\u0196\u0197\7\n\2")
        buf.write("\2\u0197\u019a\5j\66\2\u0198\u019a\5l\67\2\u0199\u0196")
        buf.write("\3\2\2\2\u0199\u0198\3\2\2\2\u019ak\3\2\2\2\u019b\u019c")
        buf.write("\7\66\2\2\u019c\u019d\5^\60\2\u019d\u019e\7\67\2\2\u019e")
        buf.write("\u01a1\3\2\2\2\u019f\u01a1\5t;\2\u01a0\u019b\3\2\2\2\u01a0")
        buf.write("\u019f\3\2\2\2\u01a1m\3\2\2\2\u01a2\u01a3\5r:\2\u01a3")
        buf.write("\u01a4\78\2\2\u01a4\u01a5\5p9\2\u01a5\u01a6\79\2\2\u01a6")
        buf.write("o\3\2\2\2\u01a7\u01ad\5^\60\2\u01a8\u01a9\5^\60\2\u01a9")
        buf.write("\u01aa\7\64\2\2\u01aa\u01ab\5p9\2\u01ab\u01ad\3\2\2\2")
        buf.write("\u01ac\u01a7\3\2\2\2\u01ac\u01a8\3\2\2\2\u01adq\3\2\2")
        buf.write("\2\u01ae\u01b1\7\60\2\2\u01af\u01b1\5x=\2\u01b0\u01ae")
        buf.write("\3\2\2\2\u01b0\u01af\3\2\2\2\u01b1s\3\2\2\2\u01b2\u01b5")
        buf.write("\5v<\2\u01b3\u01b5\5x=\2\u01b4\u01b2\3\2\2\2\u01b4\u01b3")
        buf.write("\3\2\2\2\u01b5u\3\2\2\2\u01b6\u01bc\7\60\2\2\u01b7\u01bc")
        buf.write("\7\61\2\2\u01b8\u01bc\7\62\2\2\u01b9\u01bc\7\63\2\2\u01ba")
        buf.write("\u01bc\5n8\2\u01bb\u01b6\3\2\2\2\u01bb\u01b7\3\2\2\2\u01bb")
        buf.write("\u01b8\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01ba\3\2\2\2")
        buf.write("\u01bcw\3\2\2\2\u01bd\u01c4\5P)\2\u01be\u01bf\7\60\2\2")
        buf.write("\u01bf\u01c0\7\66\2\2\u01c0\u01c1\5\62\32\2\u01c1\u01c2")
        buf.write("\7\67\2\2\u01c2\u01c4\3\2\2\2\u01c3\u01bd\3\2\2\2\u01c3")
        buf.write("\u01be\3\2\2\2\u01c4y\3\2\2\2\u01c5\u01c6\7\60\2\2\u01c6")
        buf.write("\u01c7\78\2\2\u01c7\u01c8\5~@\2\u01c8\u01c9\79\2\2\u01c9")
        buf.write("{\3\2\2\2\u01ca\u01cb\78\2\2\u01cb\u01cc\5\u0082B\2\u01cc")
        buf.write("\u01cd\79\2\2\u01cd}\3\2\2\2\u01ce\u01cf\7\61\2\2\u01cf")
        buf.write("\u01d0\5\u0080A\2\u01d0\177\3\2\2\2\u01d1\u01d2\7\64\2")
        buf.write("\2\u01d2\u01d3\7\61\2\2\u01d3\u01d6\5\u0080A\2\u01d4\u01d6")
        buf.write("\3\2\2\2\u01d5\u01d1\3\2\2\2\u01d5\u01d4\3\2\2\2\u01d6")
        buf.write("\u0081\3\2\2\2\u01d7\u01d8\5^\60\2\u01d8\u01d9\5\u0084")
        buf.write("C\2\u01d9\u0083\3\2\2\2\u01da\u01db\7\64\2\2\u01db\u01dc")
        buf.write("\5^\60\2\u01dc\u01dd\5\u0084C\2\u01dd\u01e0\3\2\2\2\u01de")
        buf.write("\u01e0\3\2\2\2\u01df\u01da\3\2\2\2\u01df\u01de\3\2\2\2")
        buf.write("\u01e0\u0085\3\2\2\2\u01e1\u01e3\7\65\2\2\u01e2\u01e1")
        buf.write("\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4")
        buf.write("\u01e5\3\2\2\2\u01e5\u0087\3\2\2\2\u01e6\u01e8\7\65\2")
        buf.write("\2\u01e7\u01e6\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7")
        buf.write("\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u0089\3\2\2\2\u01eb")
        buf.write("\u01e9\3\2\2\2(\u0090\u0094\u00a1\u00a7\u00ae\u00b9\u00c3")
        buf.write("\u00cb\u00cf\u00f5\u00fd\u0108\u010e\u0113\u0116\u011d")
        buf.write("\u0126\u012e\u0132\u0139\u0147\u0167\u016e\u0178\u0183")
        buf.write("\u018e\u0194\u0199\u01a0\u01ac\u01b0\u01b4\u01bb\u01c3")
        buf.write("\u01d5\u01df\u01e4\u01e9")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'readNumber'", "'writeNumber'", "'readBool'", 
                     "'writeBool'", "'readString'", "'writeString'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='", "'<-'", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'...'", "'=='", "'func'", "'true'", 
                     "'false'", "'number'", "'bool'", "'string'", "'return'", 
                     "'var'", "'dynamic'", "'for'", "'until'", "'by'", "'break'", 
                     "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
                     "'end'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "','", "'\n'", 
                     "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "PLUS", "MINUS", 
                      "MUL", "DIV", "MOD", "NOT_OP", "AND_OP", "OR_OP", 
                      "EQUAL", "ASSIGN", "NOT_EQUAL", "SMALLER", "SMALLER_EQUAL", 
                      "LARGER", "LARGER_EQUAL", "THREE_DOT", "DOUBLE_EQUAL", 
                      "FUNCTION", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FOR", "UNTIL", "BY", 
                      "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "IDENTIFIER", "NUMBER_LIT", 
                      "BOOLEAN_LIT", "STRING_LIT", "CM", "NEWLINE", "LRB", 
                      "RRB", "LSB", "RSB", "COMMENT", "WS", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_manydeclare = 1
    RULE_declare = 2
    RULE_function_dec = 3
    RULE_comma_separate_param = 4
    RULE_param_tail = 5
    RULE_statement = 6
    RULE_variable_dec_stmt = 7
    RULE_assign_stmt = 8
    RULE_lhs = 9
    RULE_scalar_var = 10
    RULE_if_stmt = 11
    RULE_if_part = 12
    RULE_elif_part = 13
    RULE_else_part = 14
    RULE_condition_action = 15
    RULE_condition_expr = 16
    RULE_for_stmt = 17
    RULE_number_variable = 18
    RULE_update_expr = 19
    RULE_break_stmt = 20
    RULE_continue_stmt = 21
    RULE_return_stmt = 22
    RULE_func_call_stmt = 23
    RULE_comma_separate_argument = 24
    RULE_block_stmt = 25
    RULE_list_statement_nullable = 26
    RULE_statement_tail = 27
    RULE_variable_dec = 28
    RULE_vardec_normal_type = 29
    RULE_vardec_implicit_type = 30
    RULE_var_type = 31
    RULE_dynamic_type = 32
    RULE_vardec_array_type = 33
    RULE_single_dec = 34
    RULE_value_init = 35
    RULE_parameter = 36
    RULE_vardec_normal_param = 37
    RULE_vardec_array_param = 38
    RULE_build_in_func = 39
    RULE_readNumber = 40
    RULE_writeNumber = 41
    RULE_readBool = 42
    RULE_writeBool = 43
    RULE_readString = 44
    RULE_writeString = 45
    RULE_expr = 46
    RULE_expr1 = 47
    RULE_expr2 = 48
    RULE_expr3 = 49
    RULE_expr4 = 50
    RULE_expr5 = 51
    RULE_expr6 = 52
    RULE_expr7 = 53
    RULE_element_expr = 54
    RULE_index_operators = 55
    RULE_expr_array_type = 56
    RULE_operand = 57
    RULE_variables = 58
    RULE_function_call = 59
    RULE_array_dec = 60
    RULE_array_value = 61
    RULE_comma_separate_number = 62
    RULE_digit_tail = 63
    RULE_comma_separate_expr = 64
    RULE_expr_tail = 65
    RULE_newline_separate = 66
    RULE_newline_separate_optional = 67

    ruleNames =  [ "program", "manydeclare", "declare", "function_dec", 
                   "comma_separate_param", "param_tail", "statement", "variable_dec_stmt", 
                   "assign_stmt", "lhs", "scalar_var", "if_stmt", "if_part", 
                   "elif_part", "else_part", "condition_action", "condition_expr", 
                   "for_stmt", "number_variable", "update_expr", "break_stmt", 
                   "continue_stmt", "return_stmt", "func_call_stmt", "comma_separate_argument", 
                   "block_stmt", "list_statement_nullable", "statement_tail", 
                   "variable_dec", "vardec_normal_type", "vardec_implicit_type", 
                   "var_type", "dynamic_type", "vardec_array_type", "single_dec", 
                   "value_init", "parameter", "vardec_normal_param", "vardec_array_param", 
                   "build_in_func", "readNumber", "writeNumber", "readBool", 
                   "writeBool", "readString", "writeString", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "element_expr", "index_operators", "expr_array_type", 
                   "operand", "variables", "function_call", "array_dec", 
                   "array_value", "comma_separate_number", "digit_tail", 
                   "comma_separate_expr", "expr_tail", "newline_separate", 
                   "newline_separate_optional" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    PLUS=7
    MINUS=8
    MUL=9
    DIV=10
    MOD=11
    NOT_OP=12
    AND_OP=13
    OR_OP=14
    EQUAL=15
    ASSIGN=16
    NOT_EQUAL=17
    SMALLER=18
    SMALLER_EQUAL=19
    LARGER=20
    LARGER_EQUAL=21
    THREE_DOT=22
    DOUBLE_EQUAL=23
    FUNCTION=24
    TRUE=25
    FALSE=26
    NUMBER=27
    BOOL=28
    STRING=29
    RETURN=30
    VAR=31
    DYNAMIC=32
    FOR=33
    UNTIL=34
    BY=35
    BREAK=36
    CONTINUE=37
    IF=38
    ELSE=39
    ELIF=40
    BEGIN=41
    END=42
    NOT=43
    AND=44
    OR=45
    IDENTIFIER=46
    NUMBER_LIT=47
    BOOLEAN_LIT=48
    STRING_LIT=49
    CM=50
    NEWLINE=51
    LRB=52
    RRB=53
    LSB=54
    RSB=55
    COMMENT=56
    WS=57
    ILLEGAL_ESCAPE=58
    UNCLOSE_STRING=59
    ERROR_TOKEN=60

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def manydeclare(self):
            return self.getTypedRuleContext(ZCodeParser.ManydeclareContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.manydeclare()
            self.state = 137
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManydeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.DeclareContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.DeclareContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_manydeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManydeclare" ):
                return visitor.visitManydeclare(self)
            else:
                return visitor.visitChildren(self)




    def manydeclare(self):

        localctx = ZCodeParser.ManydeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_manydeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 139
                self.declare()
                self.state = 142 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.FUNCTION) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_dec(self):
            return self.getTypedRuleContext(ZCodeParser.Function_decContext,0)


        def variable_dec(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_decContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare" ):
                return visitor.visitDeclare(self)
            else:
                return visitor.visitChildren(self)




    def declare(self):

        localctx = ZCodeParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.function_dec()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.variable_dec()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(ZCodeParser.FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def comma_separate_param(self):
            return self.getTypedRuleContext(ZCodeParser.Comma_separate_paramContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def newline_separate_optional(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_separate_optionalContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_dec" ):
                return visitor.visitFunction_dec(self)
            else:
                return visitor.visitChildren(self)




    def function_dec(self):

        localctx = ZCodeParser.Function_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(ZCodeParser.FUNCTION)
            self.state = 149
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 150
            self.match(ZCodeParser.LRB)
            self.state = 151
            self.comma_separate_param()
            self.state = 152
            self.match(ZCodeParser.RRB)
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 153
                self.newline_separate_optional()
                self.state = 154
                self.return_stmt()

            elif la_ == 2:
                self.state = 156
                self.newline_separate_optional()
                self.state = 157
                self.block_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comma_separate_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def param_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Param_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_comma_separate_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma_separate_param" ):
                return visitor.visitComma_separate_param(self)
            else:
                return visitor.visitChildren(self)




    def comma_separate_param(self):

        localctx = ZCodeParser.Comma_separate_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comma_separate_param)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.parameter()
                self.state = 162
                self.param_tail()
                pass
            elif token in [ZCodeParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def param_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Param_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_tail" ):
                return visitor.visitParam_tail(self)
            else:
                return visitor.visitChildren(self)




    def param_tail(self):

        localctx = ZCodeParser.Param_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param_tail)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(ZCodeParser.CM)
                self.state = 168
                self.parameter()
                self.state = 169
                self.param_tail()
                pass
            elif token in [ZCodeParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_dec_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_dec_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def func_call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 174
                self.variable_dec_stmt()
                pass

            elif la_ == 2:
                self.state = 175
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.state = 176
                self.if_stmt()
                pass

            elif la_ == 4:
                self.state = 177
                self.for_stmt()
                pass

            elif la_ == 5:
                self.state = 178
                self.break_stmt()
                pass

            elif la_ == 6:
                self.state = 179
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.state = 180
                self.return_stmt()
                pass

            elif la_ == 8:
                self.state = 181
                self.func_call_stmt()
                pass

            elif la_ == 9:
                self.state = 182
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_dec_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_dec(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_decContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_dec_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_dec_stmt" ):
                return visitor.visitVariable_dec_stmt(self)
            else:
                return visitor.visitChildren(self)




    def variable_dec_stmt(self):

        localctx = ZCodeParser.Variable_dec_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable_dec_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.variable_dec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = ZCodeParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.lhs()
            self.state = 188
            self.match(ZCodeParser.ASSIGN)
            self.state = 189
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(ZCodeParser.Scalar_varContext,0)


        def array_dec(self):
            return self.getTypedRuleContext(ZCodeParser.Array_decContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_lhs)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.array_dec()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_scalar_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_var" ):
                return visitor.visitScalar_var(self)
            else:
                return visitor.visitChildren(self)




    def scalar_var(self):

        localctx = ZCodeParser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_scalar_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_part(self):
            return self.getTypedRuleContext(ZCodeParser.If_partContext,0)


        def elif_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Elif_partContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Elif_partContext,i)


        def else_part(self):
            return self.getTypedRuleContext(ZCodeParser.Else_partContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.if_part()
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 198
                    self.elif_part() 
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 204
                self.else_part()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def condition_action(self):
            return self.getTypedRuleContext(ZCodeParser.Condition_actionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_part" ):
                return visitor.visitIf_part(self)
            else:
                return visitor.visitChildren(self)




    def if_part(self):

        localctx = ZCodeParser.If_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(ZCodeParser.IF)
            self.state = 208
            self.condition_action()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def condition_action(self):
            return self.getTypedRuleContext(ZCodeParser.Condition_actionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_part" ):
                return visitor.visitElif_part(self)
            else:
                return visitor.visitChildren(self)




    def elif_part(self):

        localctx = ZCodeParser.Elif_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_elif_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(ZCodeParser.ELIF)
            self.state = 211
            self.condition_action()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def condition_action(self):
            return self.getTypedRuleContext(ZCodeParser.Condition_actionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = ZCodeParser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_else_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(ZCodeParser.ELSE)
            self.state = 214
            self.condition_action()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_actionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def condition_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Condition_exprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def newline_separate_optional(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_separate_optionalContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_condition_action

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_action" ):
                return visitor.visitCondition_action(self)
            else:
                return visitor.visitChildren(self)




    def condition_action(self):

        localctx = ZCodeParser.Condition_actionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_condition_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(ZCodeParser.LRB)
            self.state = 217
            self.condition_expr()
            self.state = 218
            self.match(ZCodeParser.RRB)
            self.state = 219
            self.newline_separate_optional()
            self.state = 220
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_condition_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_expr" ):
                return visitor.visitCondition_expr(self)
            else:
                return visitor.visitChildren(self)




    def condition_expr(self):

        localctx = ZCodeParser.Condition_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condition_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def number_variable(self):
            return self.getTypedRuleContext(ZCodeParser.Number_variableContext,0)


        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def condition_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Condition_exprContext,0)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def update_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Update_exprContext,0)


        def newline_separate_optional(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_separate_optionalContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(ZCodeParser.FOR)
            self.state = 225
            self.number_variable()
            self.state = 226
            self.match(ZCodeParser.UNTIL)
            self.state = 227
            self.condition_expr()
            self.state = 228
            self.match(ZCodeParser.BY)
            self.state = 229
            self.update_expr()
            self.state = 230
            self.newline_separate_optional()
            self.state = 231
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(ZCodeParser.Scalar_varContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_number_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_variable" ):
                return visitor.visitNumber_variable(self)
            else:
                return visitor.visitChildren(self)




    def number_variable(self):

        localctx = ZCodeParser.Number_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_number_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.scalar_var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_update_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate_expr" ):
                return visitor.visitUpdate_expr(self)
            else:
                return visitor.visitChildren(self)




    def update_expr(self):

        localctx = ZCodeParser.Update_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_update_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ZCodeParser.RETURN)
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 242
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_stmt" ):
                return visitor.visitFunc_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def func_call_stmt(self):

        localctx = ZCodeParser.Func_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_func_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.function_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comma_separate_argumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def expr_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_comma_separate_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma_separate_argument" ):
                return visitor.visitComma_separate_argument(self)
            else:
                return visitor.visitChildren(self)




    def comma_separate_argument(self):

        localctx = ZCodeParser.Comma_separate_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_comma_separate_argument)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.BOOLEAN_LIT, ZCodeParser.STRING_LIT, ZCodeParser.LRB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.expr()
                self.state = 248
                self.expr_tail()
                pass
            elif token in [ZCodeParser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def list_statement_nullable(self):
            return self.getTypedRuleContext(ZCodeParser.List_statement_nullableContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def newline_separate_optional(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_separate_optionalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(ZCodeParser.BEGIN)
            self.state = 254
            self.list_statement_nullable()
            self.state = 255
            self.match(ZCodeParser.END)
            self.state = 256
            self.newline_separate_optional()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statement_nullableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statement_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_statement_nullable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement_nullable" ):
                return visitor.visitList_statement_nullable(self)
            else:
                return visitor.visitChildren(self)




    def list_statement_nullable(self):

        localctx = ZCodeParser.List_statement_nullableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_list_statement_nullable)
        try:
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.statement()
                self.state = 259
                self.statement_tail()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statement_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_tail" ):
                return visitor.visitStatement_tail(self)
            else:
                return visitor.visitChildren(self)




    def statement_tail(self):

        localctx = ZCodeParser.Statement_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_statement_tail)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.statement()
                self.state = 265
                self.statement_tail()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardec_normal_type(self):
            return self.getTypedRuleContext(ZCodeParser.Vardec_normal_typeContext,0)


        def vardec_implicit_type(self):
            return self.getTypedRuleContext(ZCodeParser.Vardec_implicit_typeContext,0)


        def vardec_array_type(self):
            return self.getTypedRuleContext(ZCodeParser.Vardec_array_typeContext,0)


        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_dec" ):
                return visitor.visitVariable_dec(self)
            else:
                return visitor.visitChildren(self)




    def variable_dec(self):

        localctx = ZCodeParser.Variable_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_variable_dec)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 270
                    self.vardec_normal_type()
                    pass

                elif la_ == 2:
                    self.state = 271
                    self.vardec_implicit_type()
                    pass

                elif la_ == 3:
                    self.state = 272
                    self.vardec_array_type()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardec_normal_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_dec(self):
            return self.getTypedRuleContext(ZCodeParser.Single_decContext,0)


        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vardec_normal_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardec_normal_type" ):
                return visitor.visitVardec_normal_type(self)
            else:
                return visitor.visitChildren(self)




    def vardec_normal_type(self):

        localctx = ZCodeParser.Vardec_normal_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_vardec_normal_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 279
            self.single_dec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardec_implicit_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(ZCodeParser.Var_typeContext,0)


        def dynamic_type(self):
            return self.getTypedRuleContext(ZCodeParser.Dynamic_typeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardec_implicit_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardec_implicit_type" ):
                return visitor.visitVardec_implicit_type(self)
            else:
                return visitor.visitChildren(self)




    def vardec_implicit_type(self):

        localctx = ZCodeParser.Vardec_implicit_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_vardec_implicit_type)
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.var_type()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.dynamic_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_type" ):
                return visitor.visitVar_type(self)
            else:
                return visitor.visitChildren(self)




    def var_type(self):

        localctx = ZCodeParser.Var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_var_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(ZCodeParser.VAR)
            self.state = 286
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 287
            self.value_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dynamic_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamic_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamic_type" ):
                return visitor.visitDynamic_type(self)
            else:
                return visitor.visitChildren(self)




    def dynamic_type(self):

        localctx = ZCodeParser.Dynamic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_dynamic_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(ZCodeParser.DYNAMIC)
            self.state = 290
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 291
                self.value_init()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardec_array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def comma_separate_number(self):
            return self.getTypedRuleContext(ZCodeParser.Comma_separate_numberContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardec_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardec_array_type" ):
                return visitor.visitVardec_array_type(self)
            else:
                return visitor.visitChildren(self)




    def vardec_array_type(self):

        localctx = ZCodeParser.Vardec_array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_vardec_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 295
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 296
            self.match(ZCodeParser.LSB)
            self.state = 297
            self.comma_separate_number()
            self.state = 298
            self.match(ZCodeParser.RSB)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 299
                self.value_init()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_single_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_dec" ):
                return visitor.visitSingle_dec(self)
            else:
                return visitor.visitChildren(self)




    def single_dec(self):

        localctx = ZCodeParser.Single_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_single_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 303
                self.value_init()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_value_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_init" ):
                return visitor.visitValue_init(self)
            else:
                return visitor.visitChildren(self)




    def value_init(self):

        localctx = ZCodeParser.Value_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_value_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(ZCodeParser.ASSIGN)
            self.state = 307
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardec_normal_param(self):
            return self.getTypedRuleContext(ZCodeParser.Vardec_normal_paramContext,0)


        def vardec_array_param(self):
            return self.getTypedRuleContext(ZCodeParser.Vardec_array_paramContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_parameter)
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.vardec_normal_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.vardec_array_param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardec_normal_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vardec_normal_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardec_normal_param" ):
                return visitor.visitVardec_normal_param(self)
            else:
                return visitor.visitChildren(self)




    def vardec_normal_param(self):

        localctx = ZCodeParser.Vardec_normal_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_vardec_normal_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 314
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardec_array_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_dec(self):
            return self.getTypedRuleContext(ZCodeParser.Array_decContext,0)


        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vardec_array_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardec_array_param" ):
                return visitor.visitVardec_array_param(self)
            else:
                return visitor.visitChildren(self)




    def vardec_array_param(self):

        localctx = ZCodeParser.Vardec_array_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_vardec_array_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 317
            self.array_dec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Build_in_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def readNumber(self):
            return self.getTypedRuleContext(ZCodeParser.ReadNumberContext,0)


        def writeNumber(self):
            return self.getTypedRuleContext(ZCodeParser.WriteNumberContext,0)


        def readBool(self):
            return self.getTypedRuleContext(ZCodeParser.ReadBoolContext,0)


        def writeBool(self):
            return self.getTypedRuleContext(ZCodeParser.WriteBoolContext,0)


        def readString(self):
            return self.getTypedRuleContext(ZCodeParser.ReadStringContext,0)


        def writeString(self):
            return self.getTypedRuleContext(ZCodeParser.WriteStringContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_build_in_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuild_in_func" ):
                return visitor.visitBuild_in_func(self)
            else:
                return visitor.visitChildren(self)




    def build_in_func(self):

        localctx = ZCodeParser.Build_in_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_build_in_func)
        try:
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.readNumber()
                pass
            elif token in [ZCodeParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.writeNumber()
                pass
            elif token in [ZCodeParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 321
                self.readBool()
                pass
            elif token in [ZCodeParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 322
                self.writeBool()
                pass
            elif token in [ZCodeParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 323
                self.readString()
                pass
            elif token in [ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 324
                self.writeString()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_readNumber

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadNumber" ):
                return visitor.visitReadNumber(self)
            else:
                return visitor.visitChildren(self)




    def readNumber(self):

        localctx = ZCodeParser.ReadNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_readNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(ZCodeParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_writeNumber

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteNumber" ):
                return visitor.visitWriteNumber(self)
            else:
                return visitor.visitChildren(self)




    def writeNumber(self):

        localctx = ZCodeParser.WriteNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_writeNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(ZCodeParser.T__1)
            self.state = 330
            self.match(ZCodeParser.LRB)
            self.state = 331
            self.expr()
            self.state = 332
            self.match(ZCodeParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadBoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_readBool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadBool" ):
                return visitor.visitReadBool(self)
            else:
                return visitor.visitChildren(self)




    def readBool(self):

        localctx = ZCodeParser.ReadBoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_readBool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(ZCodeParser.T__2)
            self.state = 335
            self.match(ZCodeParser.LRB)
            self.state = 336
            self.match(ZCodeParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteBoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_writeBool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteBool" ):
                return visitor.visitWriteBool(self)
            else:
                return visitor.visitChildren(self)




    def writeBool(self):

        localctx = ZCodeParser.WriteBoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_writeBool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(ZCodeParser.T__3)
            self.state = 339
            self.match(ZCodeParser.LRB)
            self.state = 340
            self.expr()
            self.state = 341
            self.match(ZCodeParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_readString

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadString" ):
                return visitor.visitReadString(self)
            else:
                return visitor.visitChildren(self)




    def readString(self):

        localctx = ZCodeParser.ReadStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_readString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(ZCodeParser.T__4)
            self.state = 344
            self.match(ZCodeParser.LRB)
            self.state = 345
            self.match(ZCodeParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_writeString

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteString" ):
                return visitor.visitWriteString(self)
            else:
                return visitor.visitChildren(self)




    def writeString(self):

        localctx = ZCodeParser.WriteStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_writeString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(ZCodeParser.T__5)
            self.state = 348
            self.match(ZCodeParser.LRB)
            self.state = 349
            self.expr()
            self.state = 350
            self.match(ZCodeParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def THREE_DOT(self):
            return self.getToken(ZCodeParser.THREE_DOT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.expr1()
                self.state = 353
                self.match(ZCodeParser.THREE_DOT)
                self.state = 354
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def DOUBLE_EQUAL(self):
            return self.getToken(ZCodeParser.DOUBLE_EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def SMALLER(self):
            return self.getToken(ZCodeParser.SMALLER, 0)

        def SMALLER_EQUAL(self):
            return self.getToken(ZCodeParser.SMALLER_EQUAL, 0)

        def LARGER(self):
            return self.getToken(ZCodeParser.LARGER, 0)

        def LARGER_EQUAL(self):
            return self.getToken(ZCodeParser.LARGER_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.expr2(0)
                self.state = 360
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.SMALLER) | (1 << ZCodeParser.SMALLER_EQUAL) | (1 << ZCodeParser.LARGER) | (1 << ZCodeParser.LARGER_EQUAL) | (1 << ZCodeParser.DOUBLE_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 361
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 369
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 370
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 371
                    self.expr3(0) 
                self.state = 376
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 385
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 380
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 381
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 382
                    self.expr4(0) 
                self.state = 387
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 396
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 391
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 392
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.MUL or _la==ZCodeParser.DIV):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 393
                    self.expr5() 
                self.state = 398
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_expr5)
        try:
            self.state = 402
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(ZCodeParser.NOT)
                self.state = 400
                self.expr5()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.BOOLEAN_LIT, ZCodeParser.STRING_LIT, ZCodeParser.LRB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_expr6)
        try:
            self.state = 407
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.match(ZCodeParser.MINUS)
                self.state = 405
                self.expr6()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.BOOLEAN_LIT, ZCodeParser.STRING_LIT, ZCodeParser.LRB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_expr7)
        try:
            self.state = 414
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LRB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.match(ZCodeParser.LRB)
                self.state = 410
                self.expr()
                self.state = 411
                self.match(ZCodeParser.RRB)
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.BOOLEAN_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_array_type(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_array_typeContext,0)


        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_element_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expr" ):
                return visitor.visitElement_expr(self)
            else:
                return visitor.visitChildren(self)




    def element_expr(self):

        localctx = ZCodeParser.Element_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_element_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.expr_array_type()
            self.state = 417
            self.match(ZCodeParser.LSB)
            self.state = 418
            self.index_operators()
            self.state = 419
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_index_operators)
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.expr()
                self.state = 423
                self.match(ZCodeParser.CM)
                self.state = 424
                self.index_operators()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_array_type" ):
                return visitor.visitExpr_array_type(self)
            else:
                return visitor.visitChildren(self)




    def expr_array_type(self):

        localctx = ZCodeParser.Expr_array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_expr_array_type)
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_operand)
        try:
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.variables()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(ZCodeParser.BOOLEAN_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def element_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Element_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = ZCodeParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_variables)
        try:
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.match(ZCodeParser.NUMBER_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 438
                self.match(ZCodeParser.BOOLEAN_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 439
                self.match(ZCodeParser.STRING_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 440
                self.element_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def build_in_func(self):
            return self.getTypedRuleContext(ZCodeParser.Build_in_funcContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def comma_separate_argument(self):
            return self.getTypedRuleContext(ZCodeParser.Comma_separate_argumentContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = ZCodeParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_function_call)
        try:
            self.state = 449
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.build_in_func()
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 445
                self.match(ZCodeParser.LRB)
                self.state = 446
                self.comma_separate_argument()
                self.state = 447
                self.match(ZCodeParser.RRB)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def comma_separate_number(self):
            return self.getTypedRuleContext(ZCodeParser.Comma_separate_numberContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_dec" ):
                return visitor.visitArray_dec(self)
            else:
                return visitor.visitChildren(self)




    def array_dec(self):

        localctx = ZCodeParser.Array_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_array_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 452
            self.match(ZCodeParser.LSB)
            self.state = 453
            self.comma_separate_number()
            self.state = 454
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def comma_separate_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Comma_separate_exprContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value" ):
                return visitor.visitArray_value(self)
            else:
                return visitor.visitChildren(self)




    def array_value(self):

        localctx = ZCodeParser.Array_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_array_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.match(ZCodeParser.LSB)
            self.state = 457
            self.comma_separate_expr()
            self.state = 458
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comma_separate_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def digit_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Digit_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_comma_separate_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma_separate_number" ):
                return visitor.visitComma_separate_number(self)
            else:
                return visitor.visitChildren(self)




    def comma_separate_number(self):

        localctx = ZCodeParser.Comma_separate_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_comma_separate_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(ZCodeParser.NUMBER_LIT)
            self.state = 461
            self.digit_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Digit_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def digit_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Digit_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_digit_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDigit_tail" ):
                return visitor.visitDigit_tail(self)
            else:
                return visitor.visitChildren(self)




    def digit_tail(self):

        localctx = ZCodeParser.Digit_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_digit_tail)
        try:
            self.state = 467
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.match(ZCodeParser.CM)
                self.state = 464
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 465
                self.digit_tail()
                pass
            elif token in [ZCodeParser.RSB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comma_separate_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def expr_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_comma_separate_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma_separate_expr" ):
                return visitor.visitComma_separate_expr(self)
            else:
                return visitor.visitChildren(self)




    def comma_separate_expr(self):

        localctx = ZCodeParser.Comma_separate_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_comma_separate_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.expr()
            self.state = 470
            self.expr_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(ZCodeParser.CM, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def expr_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_tail" ):
                return visitor.visitExpr_tail(self)
            else:
                return visitor.visitChildren(self)




    def expr_tail(self):

        localctx = ZCodeParser.Expr_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_expr_tail)
        try:
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.match(ZCodeParser.CM)
                self.state = 473
                self.expr()
                self.state = 474
                self.expr_tail()
                pass
            elif token in [ZCodeParser.RRB, ZCodeParser.RSB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Newline_separateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_separate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_separate" ):
                return visitor.visitNewline_separate(self)
            else:
                return visitor.visitChildren(self)




    def newline_separate(self):

        localctx = ZCodeParser.Newline_separateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_newline_separate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 479
                self.match(ZCodeParser.NEWLINE)
                self.state = 482 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Newline_separate_optionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_separate_optional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_separate_optional" ):
                return visitor.visitNewline_separate_optional(self)
            else:
                return visitor.visitChildren(self)




    def newline_separate_optional(self):

        localctx = ZCodeParser.Newline_separate_optionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_newline_separate_optional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 484
                self.match(ZCodeParser.NEWLINE)
                self.state = 489
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[48] = self.expr2_sempred
        self._predicates[49] = self.expr3_sempred
        self._predicates[50] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




