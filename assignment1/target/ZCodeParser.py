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
        buf.write("\u01da\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\5\6\u009a\n\6\3\7\3\7\3\7\3\7\3\7\5\7")
        buf.write("\u00a1\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00ac")
        buf.write("\n\b\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\5\13\u00b6\n\13")
        buf.write("\3\f\3\f\3\r\3\r\7\r\u00bc\n\r\f\r\16\r\u00bf\13\r\3\r")
        buf.write("\5\r\u00c2\n\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\5\30\u00e8\n\30\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\5\32\u00f0\n\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u00fb\n\34\3\35\3")
        buf.write("\35\3\35\3\35\5\35\u0101\n\35\3\36\3\36\3\36\5\36\u0106")
        buf.write("\n\36\3\36\5\36\u0109\n\36\3\37\3\37\3\37\3 \3 \5 \u0110")
        buf.write("\n \3!\3!\3!\3!\3\"\3\"\3\"\5\"\u0119\n\"\3#\3#\3#\3#")
        buf.write("\3#\3#\5#\u0121\n#\3$\3$\5$\u0125\n$\3%\3%\3%\3&\3&\5")
        buf.write("&\u012c\n&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3)\5)\u013a")
        buf.write("\n)\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3")
        buf.write(".\3.\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\5\60")
        buf.write("\u015a\n\60\3\61\3\61\3\61\3\61\3\61\5\61\u0161\n\61\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\7\62\u0169\n\62\f\62\16\62")
        buf.write("\u016c\13\62\3\63\3\63\3\63\3\63\3\63\3\63\7\63\u0174")
        buf.write("\n\63\f\63\16\63\u0177\13\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\7\64\u017f\n\64\f\64\16\64\u0182\13\64\3\65\3\65")
        buf.write("\3\65\5\65\u0187\n\65\3\66\3\66\3\66\5\66\u018c\n\66\3")
        buf.write("\67\3\67\3\67\3\67\3\67\5\67\u0193\n\67\38\38\38\38\3")
        buf.write("8\39\39\39\39\39\59\u019f\n9\3:\3:\5:\u01a3\n:\3;\3;\5")
        buf.write(";\u01a7\n;\3<\3<\3<\3<\3<\5<\u01ae\n<\3=\3=\3=\3=\3=\3")
        buf.write("=\5=\u01b6\n=\3>\3>\3>\3>\3>\3?\3?\3?\3?\3@\3@\3@\3A\3")
        buf.write("A\3A\3A\5A\u01c8\nA\3B\3B\3B\3C\3C\3C\3C\3C\5C\u01d2\n")
        buf.write("C\3D\7D\u01d5\nD\fD\16D\u01d8\13D\3D\2\5bdfE\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write("\2\7\3\2\26\30\5\2\61\61\63\6799\3\2\'(\3\2)*\3\2+,\2")
        buf.write("\u01c7\2\u0088\3\2\2\2\4\u008b\3\2\2\2\6\u008d\3\2\2\2")
        buf.write("\b\u008f\3\2\2\2\n\u0099\3\2\2\2\f\u00a0\3\2\2\2\16\u00ab")
        buf.write("\3\2\2\2\20\u00ad\3\2\2\2\22\u00af\3\2\2\2\24\u00b5\3")
        buf.write("\2\2\2\26\u00b7\3\2\2\2\30\u00b9\3\2\2\2\32\u00c3\3\2")
        buf.write("\2\2\34\u00c6\3\2\2\2\36\u00c9\3\2\2\2 \u00cc\3\2\2\2")
        buf.write("\"\u00d2\3\2\2\2$\u00d4\3\2\2\2&\u00dd\3\2\2\2(\u00df")
        buf.write("\3\2\2\2*\u00e1\3\2\2\2,\u00e3\3\2\2\2.\u00e5\3\2\2\2")
        buf.write("\60\u00e9\3\2\2\2\62\u00ef\3\2\2\2\64\u00f1\3\2\2\2\66")
        buf.write("\u00fa\3\2\2\28\u0100\3\2\2\2:\u0108\3\2\2\2<\u010a\3")
        buf.write("\2\2\2>\u010f\3\2\2\2@\u0111\3\2\2\2B\u0115\3\2\2\2D\u011a")
        buf.write("\3\2\2\2F\u0122\3\2\2\2H\u0126\3\2\2\2J\u012b\3\2\2\2")
        buf.write("L\u012d\3\2\2\2N\u0130\3\2\2\2P\u0139\3\2\2\2R\u013b\3")
        buf.write("\2\2\2T\u013d\3\2\2\2V\u0142\3\2\2\2X\u0146\3\2\2\2Z\u014b")
        buf.write("\3\2\2\2\\\u014f\3\2\2\2^\u0159\3\2\2\2`\u0160\3\2\2\2")
        buf.write("b\u0162\3\2\2\2d\u016d\3\2\2\2f\u0178\3\2\2\2h\u0186\3")
        buf.write("\2\2\2j\u018b\3\2\2\2l\u0192\3\2\2\2n\u0194\3\2\2\2p\u019e")
        buf.write("\3\2\2\2r\u01a2\3\2\2\2t\u01a6\3\2\2\2v\u01ad\3\2\2\2")
        buf.write("x\u01b5\3\2\2\2z\u01b7\3\2\2\2|\u01bc\3\2\2\2~\u01c0\3")
        buf.write("\2\2\2\u0080\u01c7\3\2\2\2\u0082\u01c9\3\2\2\2\u0084\u01d1")
        buf.write("\3\2\2\2\u0086\u01d6\3\2\2\2\u0088\u0089\5\4\3\2\u0089")
        buf.write("\u008a\7\2\2\3\u008a\3\3\2\2\2\u008b\u008c\5\6\4\2\u008c")
        buf.write("\5\3\2\2\2\u008d\u008e\5\b\5\2\u008e\7\3\2\2\2\u008f\u0090")
        buf.write("\7\23\2\2\u0090\u0091\7\t\2\2\u0091\u0092\7\17\2\2\u0092")
        buf.write("\u0093\5\n\6\2\u0093\u0094\7\20\2\2\u0094\t\3\2\2\2\u0095")
        buf.write("\u0096\5J&\2\u0096\u0097\5\f\7\2\u0097\u009a\3\2\2\2\u0098")
        buf.write("\u009a\3\2\2\2\u0099\u0095\3\2\2\2\u0099\u0098\3\2\2\2")
        buf.write("\u009a\13\3\2\2\2\u009b\u009c\7\r\2\2\u009c\u009d\5J&")
        buf.write("\2\u009d\u009e\5\f\7\2\u009e\u00a1\3\2\2\2\u009f\u00a1")
        buf.write("\3\2\2\2\u00a0\u009b\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1")
        buf.write("\r\3\2\2\2\u00a2\u00ac\5\20\t\2\u00a3\u00ac\5\22\n\2\u00a4")
        buf.write("\u00ac\5\30\r\2\u00a5\u00ac\5$\23\2\u00a6\u00ac\5*\26")
        buf.write("\2\u00a7\u00ac\5,\27\2\u00a8\u00ac\5.\30\2\u00a9\u00ac")
        buf.write("\5\60\31\2\u00aa\u00ac\5\64\33\2\u00ab\u00a2\3\2\2\2\u00ab")
        buf.write("\u00a3\3\2\2\2\u00ab\u00a4\3\2\2\2\u00ab\u00a5\3\2\2\2")
        buf.write("\u00ab\u00a6\3\2\2\2\u00ab\u00a7\3\2\2\2\u00ab\u00a8\3")
        buf.write("\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\17")
        buf.write("\3\2\2\2\u00ad\u00ae\5:\36\2\u00ae\21\3\2\2\2\u00af\u00b0")
        buf.write("\5\24\13\2\u00b0\u00b1\7\62\2\2\u00b1\u00b2\5^\60\2\u00b2")
        buf.write("\23\3\2\2\2\u00b3\u00b6\5\26\f\2\u00b4\u00b6\5z>\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\25\3\2\2\2\u00b7")
        buf.write("\u00b8\7\t\2\2\u00b8\27\3\2\2\2\u00b9\u00bd\5\32\16\2")
        buf.write("\u00ba\u00bc\5\34\17\2\u00bb\u00ba\3\2\2\2\u00bc\u00bf")
        buf.write("\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00c2\5\36\20")
        buf.write("\2\u00c1\u00c0\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\31\3")
        buf.write("\2\2\2\u00c3\u00c4\7!\2\2\u00c4\u00c5\5 \21\2\u00c5\33")
        buf.write("\3\2\2\2\u00c6\u00c7\7#\2\2\u00c7\u00c8\5 \21\2\u00c8")
        buf.write("\35\3\2\2\2\u00c9\u00ca\7\"\2\2\u00ca\u00cb\5 \21\2\u00cb")
        buf.write("\37\3\2\2\2\u00cc\u00cd\7\17\2\2\u00cd\u00ce\5\"\22\2")
        buf.write("\u00ce\u00cf\7\20\2\2\u00cf\u00d0\5\u0086D\2\u00d0\u00d1")
        buf.write("\5\16\b\2\u00d1!\3\2\2\2\u00d2\u00d3\5^\60\2\u00d3#\3")
        buf.write("\2\2\2\u00d4\u00d5\7\34\2\2\u00d5\u00d6\5&\24\2\u00d6")
        buf.write("\u00d7\7\35\2\2\u00d7\u00d8\5\"\22\2\u00d8\u00d9\7\36")
        buf.write("\2\2\u00d9\u00da\5(\25\2\u00da\u00db\5\u0086D\2\u00db")
        buf.write("\u00dc\5\16\b\2\u00dc%\3\2\2\2\u00dd\u00de\5\26\f\2\u00de")
        buf.write("\'\3\2\2\2\u00df\u00e0\5^\60\2\u00e0)\3\2\2\2\u00e1\u00e2")
        buf.write("\7\37\2\2\u00e2+\3\2\2\2\u00e3\u00e4\7 \2\2\u00e4-\3\2")
        buf.write("\2\2\u00e5\u00e7\7\31\2\2\u00e6\u00e8\5^\60\2\u00e7\u00e6")
        buf.write("\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8/\3\2\2\2\u00e9\u00ea")
        buf.write("\5x=\2\u00ea\61\3\2\2\2\u00eb\u00ec\5^\60\2\u00ec\u00ed")
        buf.write("\5\u0084C\2\u00ed\u00f0\3\2\2\2\u00ee\u00f0\3\2\2\2\u00ef")
        buf.write("\u00eb\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0\63\3\2\2\2\u00f1")
        buf.write("\u00f2\7$\2\2\u00f2\u00f3\5\66\34\2\u00f3\u00f4\7%\2\2")
        buf.write("\u00f4\u00f5\5\u0086D\2\u00f5\65\3\2\2\2\u00f6\u00f7\5")
        buf.write("\16\b\2\u00f7\u00f8\58\35\2\u00f8\u00fb\3\2\2\2\u00f9")
        buf.write("\u00fb\3\2\2\2\u00fa\u00f6\3\2\2\2\u00fa\u00f9\3\2\2\2")
        buf.write("\u00fb\67\3\2\2\2\u00fc\u00fd\5\16\b\2\u00fd\u00fe\58")
        buf.write("\35\2\u00fe\u0101\3\2\2\2\u00ff\u0101\3\2\2\2\u0100\u00fc")
        buf.write("\3\2\2\2\u0100\u00ff\3\2\2\2\u01019\3\2\2\2\u0102\u0106")
        buf.write("\5<\37\2\u0103\u0106\5> \2\u0104\u0106\5D#\2\u0105\u0102")
        buf.write("\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0104\3\2\2\2\u0106")
        buf.write("\u0109\3\2\2\2\u0107\u0109\5J&\2\u0108\u0105\3\2\2\2\u0108")
        buf.write("\u0107\3\2\2\2\u0109;\3\2\2\2\u010a\u010b\t\2\2\2\u010b")
        buf.write("\u010c\5F$\2\u010c=\3\2\2\2\u010d\u0110\5@!\2\u010e\u0110")
        buf.write("\5B\"\2\u010f\u010d\3\2\2\2\u010f\u010e\3\2\2\2\u0110")
        buf.write("?\3\2\2\2\u0111\u0112\7\32\2\2\u0112\u0113\7\t\2\2\u0113")
        buf.write("\u0114\5H%\2\u0114A\3\2\2\2\u0115\u0116\7\33\2\2\u0116")
        buf.write("\u0118\7\t\2\2\u0117\u0119\5H%\2\u0118\u0117\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0119C\3\2\2\2\u011a\u011b\t\2\2\2\u011b")
        buf.write("\u011c\7\t\2\2\u011c\u011d\7\21\2\2\u011d\u011e\5~@\2")
        buf.write("\u011e\u0120\7\22\2\2\u011f\u0121\5H%\2\u0120\u011f\3")
        buf.write("\2\2\2\u0120\u0121\3\2\2\2\u0121E\3\2\2\2\u0122\u0124")
        buf.write("\7\t\2\2\u0123\u0125\5H%\2\u0124\u0123\3\2\2\2\u0124\u0125")
        buf.write("\3\2\2\2\u0125G\3\2\2\2\u0126\u0127\7\62\2\2\u0127\u0128")
        buf.write("\5^\60\2\u0128I\3\2\2\2\u0129\u012c\5L\'\2\u012a\u012c")
        buf.write("\5N(\2\u012b\u0129\3\2\2\2\u012b\u012a\3\2\2\2\u012cK")
        buf.write("\3\2\2\2\u012d\u012e\t\2\2\2\u012e\u012f\7\t\2\2\u012f")
        buf.write("M\3\2\2\2\u0130\u0131\t\2\2\2\u0131\u0132\5z>\2\u0132")
        buf.write("O\3\2\2\2\u0133\u013a\5R*\2\u0134\u013a\5T+\2\u0135\u013a")
        buf.write("\5V,\2\u0136\u013a\5X-\2\u0137\u013a\5Z.\2\u0138\u013a")
        buf.write("\5\\/\2\u0139\u0133\3\2\2\2\u0139\u0134\3\2\2\2\u0139")
        buf.write("\u0135\3\2\2\2\u0139\u0136\3\2\2\2\u0139\u0137\3\2\2\2")
        buf.write("\u0139\u0138\3\2\2\2\u013aQ\3\2\2\2\u013b\u013c\7\3\2")
        buf.write("\2\u013cS\3\2\2\2\u013d\u013e\7\4\2\2\u013e\u013f\7\17")
        buf.write("\2\2\u013f\u0140\5^\60\2\u0140\u0141\7\20\2\2\u0141U\3")
        buf.write("\2\2\2\u0142\u0143\7\5\2\2\u0143\u0144\7\17\2\2\u0144")
        buf.write("\u0145\7\20\2\2\u0145W\3\2\2\2\u0146\u0147\7\6\2\2\u0147")
        buf.write("\u0148\7\17\2\2\u0148\u0149\5^\60\2\u0149\u014a\7\20\2")
        buf.write("\2\u014aY\3\2\2\2\u014b\u014c\7\7\2\2\u014c\u014d\7\17")
        buf.write("\2\2\u014d\u014e\7\20\2\2\u014e[\3\2\2\2\u014f\u0150\7")
        buf.write("\b\2\2\u0150\u0151\7\17\2\2\u0151\u0152\5^\60\2\u0152")
        buf.write("\u0153\7\20\2\2\u0153]\3\2\2\2\u0154\u0155\5`\61\2\u0155")
        buf.write("\u0156\78\2\2\u0156\u0157\5`\61\2\u0157\u015a\3\2\2\2")
        buf.write("\u0158\u015a\5`\61\2\u0159\u0154\3\2\2\2\u0159\u0158\3")
        buf.write("\2\2\2\u015a_\3\2\2\2\u015b\u015c\5b\62\2\u015c\u015d")
        buf.write("\t\3\2\2\u015d\u015e\5b\62\2\u015e\u0161\3\2\2\2\u015f")
        buf.write("\u0161\5b\62\2\u0160\u015b\3\2\2\2\u0160\u015f\3\2\2\2")
        buf.write("\u0161a\3\2\2\2\u0162\u0163\b\62\1\2\u0163\u0164\5d\63")
        buf.write("\2\u0164\u016a\3\2\2\2\u0165\u0166\f\4\2\2\u0166\u0167")
        buf.write("\t\4\2\2\u0167\u0169\5d\63\2\u0168\u0165\3\2\2\2\u0169")
        buf.write("\u016c\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2")
        buf.write("\u016bc\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u016e\b\63\1")
        buf.write("\2\u016e\u016f\5f\64\2\u016f\u0175\3\2\2\2\u0170\u0171")
        buf.write("\f\4\2\2\u0171\u0172\t\5\2\2\u0172\u0174\5f\64\2\u0173")
        buf.write("\u0170\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2")
        buf.write("\u0175\u0176\3\2\2\2\u0176e\3\2\2\2\u0177\u0175\3\2\2")
        buf.write("\2\u0178\u0179\b\64\1\2\u0179\u017a\5h\65\2\u017a\u0180")
        buf.write("\3\2\2\2\u017b\u017c\f\4\2\2\u017c\u017d\t\6\2\2\u017d")
        buf.write("\u017f\5h\65\2\u017e\u017b\3\2\2\2\u017f\u0182\3\2\2\2")
        buf.write("\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181g\3\2\2")
        buf.write("\2\u0182\u0180\3\2\2\2\u0183\u0184\7&\2\2\u0184\u0187")
        buf.write("\5h\65\2\u0185\u0187\5j\66\2\u0186\u0183\3\2\2\2\u0186")
        buf.write("\u0185\3\2\2\2\u0187i\3\2\2\2\u0188\u0189\7*\2\2\u0189")
        buf.write("\u018c\5j\66\2\u018a\u018c\5l\67\2\u018b\u0188\3\2\2\2")
        buf.write("\u018b\u018a\3\2\2\2\u018ck\3\2\2\2\u018d\u018e\7\17\2")
        buf.write("\2\u018e\u018f\5^\60\2\u018f\u0190\7\20\2\2\u0190\u0193")
        buf.write("\3\2\2\2\u0191\u0193\5t;\2\u0192\u018d\3\2\2\2\u0192\u0191")
        buf.write("\3\2\2\2\u0193m\3\2\2\2\u0194\u0195\5r:\2\u0195\u0196")
        buf.write("\7\21\2\2\u0196\u0197\5p9\2\u0197\u0198\7\22\2\2\u0198")
        buf.write("o\3\2\2\2\u0199\u019f\5^\60\2\u019a\u019b\5^\60\2\u019b")
        buf.write("\u019c\7\r\2\2\u019c\u019d\5p9\2\u019d\u019f\3\2\2\2\u019e")
        buf.write("\u0199\3\2\2\2\u019e\u019a\3\2\2\2\u019fq\3\2\2\2\u01a0")
        buf.write("\u01a3\7\t\2\2\u01a1\u01a3\5x=\2\u01a2\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a1\3\2\2\2\u01a3s\3\2\2\2\u01a4\u01a7\5v<\2\u01a5")
        buf.write("\u01a7\5x=\2\u01a6\u01a4\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7")
        buf.write("u\3\2\2\2\u01a8\u01ae\7\t\2\2\u01a9\u01ae\7\n\2\2\u01aa")
        buf.write("\u01ae\7\13\2\2\u01ab\u01ae\7\f\2\2\u01ac\u01ae\5n8\2")
        buf.write("\u01ad\u01a8\3\2\2\2\u01ad\u01a9\3\2\2\2\u01ad\u01aa\3")
        buf.write("\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac\3\2\2\2\u01aew")
        buf.write("\3\2\2\2\u01af\u01b6\5P)\2\u01b0\u01b1\7\t\2\2\u01b1\u01b2")
        buf.write("\7\17\2\2\u01b2\u01b3\5\62\32\2\u01b3\u01b4\7\20\2\2\u01b4")
        buf.write("\u01b6\3\2\2\2\u01b5\u01af\3\2\2\2\u01b5\u01b0\3\2\2\2")
        buf.write("\u01b6y\3\2\2\2\u01b7\u01b8\7\t\2\2\u01b8\u01b9\7\21\2")
        buf.write("\2\u01b9\u01ba\5~@\2\u01ba\u01bb\7\22\2\2\u01bb{\3\2\2")
        buf.write("\2\u01bc\u01bd\7\21\2\2\u01bd\u01be\5\u0082B\2\u01be\u01bf")
        buf.write("\7\22\2\2\u01bf}\3\2\2\2\u01c0\u01c1\7\n\2\2\u01c1\u01c2")
        buf.write("\5\u0080A\2\u01c2\177\3\2\2\2\u01c3\u01c4\7\r\2\2\u01c4")
        buf.write("\u01c5\7\n\2\2\u01c5\u01c8\5\u0080A\2\u01c6\u01c8\3\2")
        buf.write("\2\2\u01c7\u01c3\3\2\2\2\u01c7\u01c6\3\2\2\2\u01c8\u0081")
        buf.write("\3\2\2\2\u01c9\u01ca\5^\60\2\u01ca\u01cb\5\u0084C\2\u01cb")
        buf.write("\u0083\3\2\2\2\u01cc\u01cd\7\r\2\2\u01cd\u01ce\5^\60\2")
        buf.write("\u01ce\u01cf\5\u0084C\2\u01cf\u01d2\3\2\2\2\u01d0\u01d2")
        buf.write("\3\2\2\2\u01d1\u01cc\3\2\2\2\u01d1\u01d0\3\2\2\2\u01d2")
        buf.write("\u0085\3\2\2\2\u01d3\u01d5\7\16\2\2\u01d4\u01d3\3\2\2")
        buf.write("\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7\u0087\3\2\2\2\u01d8\u01d6\3\2\2\2$\u0099")
        buf.write("\u00a0\u00ab\u00b5\u00bd\u00c1\u00e7\u00ef\u00fa\u0100")
        buf.write("\u0105\u0108\u010f\u0118\u0120\u0124\u012b\u0139\u0159")
        buf.write("\u0160\u016a\u0175\u0180\u0186\u018b\u0192\u019e\u01a2")
        buf.write("\u01a6\u01ad\u01b5\u01c7\u01d1\u01d6")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'readNumber'", "'writeNumber'", "'readBool'", 
                     "'writeBool'", "'readString'", "'writeString'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "','", "'\n'", 
                     "'('", "')'", "'['", "']'", "'func'", "'true'", "'false'", 
                     "'number'", "'bool'", "'string'", "'return'", "'var'", 
                     "'dynamic'", "'for'", "'until'", "'by'", "'break'", 
                     "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
                     "'end'", "<INVALID>", "<INVALID>", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='", "'<-'", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'...'", "'=='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "NUMBER_LIT", "BOOLEAN_LIT", "STRING_LIT", "CM", "NEWLINE", 
                      "LRB", "RRB", "LSB", "RSB", "FUNC", "TRUE", "FALSE", 
                      "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", 
                      "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "PLUS", 
                      "MINUS", "MUL", "DIV", "MOD", "NOT_OP", "AND_OP", 
                      "OR_OP", "EQUAL", "ASSIGN", "NOT_EQUAL", "SMALLER", 
                      "SMALLER_EQUAL", "LARGER", "LARGER_EQUAL", "THREE_DOT", 
                      "DOUBLE_EQUAL", "COMMENT", "WS", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_manydeclare = 1
    RULE_declare = 2
    RULE_function_declare = 3
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
    RULE_newline_separate_optional = 66

    ruleNames =  [ "program", "manydeclare", "declare", "function_declare", 
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
                   "comma_separate_expr", "expr_tail", "newline_separate_optional" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    IDENTIFIER=7
    NUMBER_LIT=8
    BOOLEAN_LIT=9
    STRING_LIT=10
    CM=11
    NEWLINE=12
    LRB=13
    RRB=14
    LSB=15
    RSB=16
    FUNC=17
    TRUE=18
    FALSE=19
    NUMBER=20
    BOOL=21
    STRING=22
    RETURN=23
    VAR=24
    DYNAMIC=25
    FOR=26
    UNTIL=27
    BY=28
    BREAK=29
    CONTINUE=30
    IF=31
    ELSE=32
    ELIF=33
    BEGIN=34
    END=35
    NOT=36
    AND=37
    OR=38
    PLUS=39
    MINUS=40
    MUL=41
    DIV=42
    MOD=43
    NOT_OP=44
    AND_OP=45
    OR_OP=46
    EQUAL=47
    ASSIGN=48
    NOT_EQUAL=49
    SMALLER=50
    SMALLER_EQUAL=51
    LARGER=52
    LARGER_EQUAL=53
    THREE_DOT=54
    DOUBLE_EQUAL=55
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
            self.state = 134
            self.manydeclare()
            self.state = 135
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

        def declare(self):
            return self.getTypedRuleContext(ZCodeParser.DeclareContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.declare()
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

        def function_declare(self):
            return self.getTypedRuleContext(ZCodeParser.Function_declareContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.function_declare()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def comma_separate_param(self):
            return self.getTypedRuleContext(ZCodeParser.Comma_separate_paramContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declare" ):
                return visitor.visitFunction_declare(self)
            else:
                return visitor.visitChildren(self)




    def function_declare(self):

        localctx = ZCodeParser.Function_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(ZCodeParser.FUNC)
            self.state = 142
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 143
            self.match(ZCodeParser.LRB)
            self.state = 144
            self.comma_separate_param()
            self.state = 145
            self.match(ZCodeParser.RRB)
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
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.parameter()
                self.state = 148
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
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(ZCodeParser.CM)
                self.state = 154
                self.parameter()
                self.state = 155
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
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 160
                self.variable_dec_stmt()
                pass

            elif la_ == 2:
                self.state = 161
                self.assign_stmt()
                pass

            elif la_ == 3:
                self.state = 162
                self.if_stmt()
                pass

            elif la_ == 4:
                self.state = 163
                self.for_stmt()
                pass

            elif la_ == 5:
                self.state = 164
                self.break_stmt()
                pass

            elif la_ == 6:
                self.state = 165
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.state = 166
                self.return_stmt()
                pass

            elif la_ == 8:
                self.state = 167
                self.func_call_stmt()
                pass

            elif la_ == 9:
                self.state = 168
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
            self.state = 171
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
            self.state = 173
            self.lhs()
            self.state = 174
            self.match(ZCodeParser.ASSIGN)
            self.state = 175
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
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
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
            self.state = 181
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
            self.state = 183
            self.if_part()
            self.state = 187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 184
                    self.elif_part() 
                self.state = 189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 190
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
            self.state = 193
            self.match(ZCodeParser.IF)
            self.state = 194
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
            self.state = 196
            self.match(ZCodeParser.ELIF)
            self.state = 197
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
            self.state = 199
            self.match(ZCodeParser.ELSE)
            self.state = 200
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
            self.state = 202
            self.match(ZCodeParser.LRB)
            self.state = 203
            self.condition_expr()
            self.state = 204
            self.match(ZCodeParser.RRB)
            self.state = 205
            self.newline_separate_optional()
            self.state = 206
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
            self.state = 208
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
            self.state = 210
            self.match(ZCodeParser.FOR)
            self.state = 211
            self.number_variable()
            self.state = 212
            self.match(ZCodeParser.UNTIL)
            self.state = 213
            self.condition_expr()
            self.state = 214
            self.match(ZCodeParser.BY)
            self.state = 215
            self.update_expr()
            self.state = 216
            self.newline_separate_optional()
            self.state = 217
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
            self.state = 219
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
            self.state = 221
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
            self.state = 223
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
            self.state = 225
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
            self.state = 227
            self.match(ZCodeParser.RETURN)
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 228
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
            self.state = 231
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
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.BOOLEAN_LIT, ZCodeParser.STRING_LIT, ZCodeParser.LRB, ZCodeParser.NOT, ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.expr()
                self.state = 234
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
            self.state = 239
            self.match(ZCodeParser.BEGIN)
            self.state = 240
            self.list_statement_nullable()
            self.state = 241
            self.match(ZCodeParser.END)
            self.state = 242
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
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.statement()
                self.state = 245
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
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.statement()
                self.state = 251
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
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 256
                    self.vardec_normal_type()
                    pass

                elif la_ == 2:
                    self.state = 257
                    self.vardec_implicit_type()
                    pass

                elif la_ == 3:
                    self.state = 258
                    self.vardec_array_type()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
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
            self.state = 264
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 265
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
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.var_type()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
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
            self.state = 271
            self.match(ZCodeParser.VAR)
            self.state = 272
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 273
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
            self.state = 275
            self.match(ZCodeParser.DYNAMIC)
            self.state = 276
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 277
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
            self.state = 280
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 281
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 282
            self.match(ZCodeParser.LSB)
            self.state = 283
            self.comma_separate_number()
            self.state = 284
            self.match(ZCodeParser.RSB)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 285
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
            self.state = 288
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 289
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
            self.state = 292
            self.match(ZCodeParser.ASSIGN)
            self.state = 293
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
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.vardec_normal_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
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
            self.state = 299
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 300
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
            self.state = 302
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 303
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
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.readNumber()
                pass
            elif token in [ZCodeParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.writeNumber()
                pass
            elif token in [ZCodeParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 307
                self.readBool()
                pass
            elif token in [ZCodeParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 308
                self.writeBool()
                pass
            elif token in [ZCodeParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 309
                self.readString()
                pass
            elif token in [ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 310
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
            self.state = 313
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
            self.state = 315
            self.match(ZCodeParser.T__1)
            self.state = 316
            self.match(ZCodeParser.LRB)
            self.state = 317
            self.expr()
            self.state = 318
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
            self.state = 320
            self.match(ZCodeParser.T__2)
            self.state = 321
            self.match(ZCodeParser.LRB)
            self.state = 322
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
            self.state = 324
            self.match(ZCodeParser.T__3)
            self.state = 325
            self.match(ZCodeParser.LRB)
            self.state = 326
            self.expr()
            self.state = 327
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
            self.state = 329
            self.match(ZCodeParser.T__4)
            self.state = 330
            self.match(ZCodeParser.LRB)
            self.state = 331
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
            self.state = 333
            self.match(ZCodeParser.T__5)
            self.state = 334
            self.match(ZCodeParser.LRB)
            self.state = 335
            self.expr()
            self.state = 336
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
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.expr1()
                self.state = 339
                self.match(ZCodeParser.THREE_DOT)
                self.state = 340
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
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
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.expr2(0)
                self.state = 346
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.SMALLER) | (1 << ZCodeParser.SMALLER_EQUAL) | (1 << ZCodeParser.LARGER) | (1 << ZCodeParser.LARGER_EQUAL) | (1 << ZCodeParser.DOUBLE_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 347
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
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
            self.state = 353
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 360
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 355
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 356
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 357
                    self.expr3(0) 
                self.state = 362
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
            self.state = 364
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 371
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 366
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 367
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 368
                    self.expr4(0) 
                self.state = 373
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
            self.state = 375
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 382
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 377
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 378
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.MUL or _la==ZCodeParser.DIV):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 379
                    self.expr5() 
                self.state = 384
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.match(ZCodeParser.NOT)
                self.state = 386
                self.expr5()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.BOOLEAN_LIT, ZCodeParser.STRING_LIT, ZCodeParser.LRB, ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
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
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.match(ZCodeParser.MINUS)
                self.state = 391
                self.expr6()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.BOOLEAN_LIT, ZCodeParser.STRING_LIT, ZCodeParser.LRB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
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
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LRB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.match(ZCodeParser.LRB)
                self.state = 396
                self.expr()
                self.state = 397
                self.match(ZCodeParser.RRB)
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.BOOLEAN_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
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
            self.state = 402
            self.expr_array_type()
            self.state = 403
            self.match(ZCodeParser.LSB)
            self.state = 404
            self.index_operators()
            self.state = 405
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
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.expr()
                self.state = 409
                self.match(ZCodeParser.CM)
                self.state = 410
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
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
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
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.variables()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
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
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.match(ZCodeParser.NUMBER_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 424
                self.match(ZCodeParser.BOOLEAN_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 425
                self.match(ZCodeParser.STRING_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 426
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
            self.state = 435
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.build_in_func()
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 431
                self.match(ZCodeParser.LRB)
                self.state = 432
                self.comma_separate_argument()
                self.state = 433
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
            self.state = 437
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 438
            self.match(ZCodeParser.LSB)
            self.state = 439
            self.comma_separate_number()
            self.state = 440
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
            self.state = 442
            self.match(ZCodeParser.LSB)
            self.state = 443
            self.comma_separate_expr()
            self.state = 444
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
            self.state = 446
            self.match(ZCodeParser.NUMBER_LIT)
            self.state = 447
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
            self.state = 453
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.match(ZCodeParser.CM)
                self.state = 450
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 451
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
            self.state = 455
            self.expr()
            self.state = 456
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
            self.state = 463
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.match(ZCodeParser.CM)
                self.state = 459
                self.expr()
                self.state = 460
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
        self.enterRule(localctx, 132, self.RULE_newline_separate_optional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 465
                self.match(ZCodeParser.NEWLINE)
                self.state = 470
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
         




