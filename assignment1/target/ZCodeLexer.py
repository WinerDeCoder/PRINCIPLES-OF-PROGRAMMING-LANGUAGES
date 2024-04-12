# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u01f8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\7\b\u00d2\n\b\f\b\16\b\u00d5\13")
        buf.write("\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00df\n\n\3\n\6")
        buf.write("\n\u00e2\n\n\r\n\16\n\u00e3\5\n\u00e6\n\n\3\13\3\13\5")
        buf.write("\13\u00ea\n\13\3\f\3\f\3\f\3\f\7\f\u00f0\n\f\f\f\16\f")
        buf.write("\u00f3\13\f\3\f\3\f\3\f\3\r\3\r\3\16\6\16\u00fb\n\16\r")
        buf.write("\16\16\16\u00fc\3\17\3\17\7\17\u0101\n\17\f\17\16\17\u0104")
        buf.write("\13\17\3\20\3\20\5\20\u0108\n\20\3\20\6\20\u010b\n\20")
        buf.write("\r\20\16\20\u010c\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3")
        buf.write("\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$")
        buf.write("\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3.\3.\3")
        buf.write(".\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\38\38\39\39\39\3:\3:\3:\3;\3;\3<\3<\3<\3=\3")
        buf.write("=\3>\3>\3>\3?\3?\3?\3?\3@\3@\3@\3A\3A\3A\3A\7A\u01c9\n")
        buf.write("A\fA\16A\u01cc\13A\3A\3A\3B\3B\3B\5B\u01d3\nB\3C\6C\u01d6")
        buf.write("\nC\rC\16C\u01d7\3C\3C\3D\3D\3D\3D\7D\u01e0\nD\fD\16D")
        buf.write("\u01e3\13D\3D\3D\3D\3E\3E\3E\3E\7E\u01ec\nE\fE\16E\u01ef")
        buf.write("\13E\3E\5E\u01f2\nE\3E\3E\3F\3F\3F\2\2G\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\2\23\n\25\13\27\f\31\2\33\2\35\2\37")
        buf.write("\2!\2#\2%\2\'\r)\16+\17-\20/\21\61\22\63\23\65\24\67\25")
        buf.write("9\26;\27=\30?\31A\32C\33E\34G\35I\36K\37M O!Q\"S#U$W%")
        buf.write("Y&[\'](_)a*c+e,g-i.k/m\60o\61q\62s\63u\64w\65y\66{\67")
        buf.write("}8\1779\u0081:\u0083\2\u0085;\u0087<\u0089=\u008b>\3\2")
        buf.write("\13\5\2C\\aac|\3\2\62;\4\2GGgg\4\2--//\6\2\n\f\16\17$")
        buf.write("$^^\t\2))^^ddhhppttvv\4\2\f\f\60\60\5\2\n\13\16\16\"\"")
        buf.write("\5\3\n\f\16\17^^\2\u0205\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u008d\3\2\2")
        buf.write("\2\5\u0098\3\2\2\2\7\u00a4\3\2\2\2\t\u00ad\3\2\2\2\13")
        buf.write("\u00b7\3\2\2\2\r\u00c2\3\2\2\2\17\u00ce\3\2\2\2\21\u00d6")
        buf.write("\3\2\2\2\23\u00e5\3\2\2\2\25\u00e9\3\2\2\2\27\u00eb\3")
        buf.write("\2\2\2\31\u00f7\3\2\2\2\33\u00fa\3\2\2\2\35\u00fe\3\2")
        buf.write("\2\2\37\u0105\3\2\2\2!\u010e\3\2\2\2#\u0110\3\2\2\2%\u0113")
        buf.write("\3\2\2\2\'\u0116\3\2\2\2)\u0118\3\2\2\2+\u011a\3\2\2\2")
        buf.write("-\u011c\3\2\2\2/\u011e\3\2\2\2\61\u0120\3\2\2\2\63\u0122")
        buf.write("\3\2\2\2\65\u0127\3\2\2\2\67\u012c\3\2\2\29\u0132\3\2")
        buf.write("\2\2;\u0139\3\2\2\2=\u013e\3\2\2\2?\u0145\3\2\2\2A\u014c")
        buf.write("\3\2\2\2C\u0150\3\2\2\2E\u0158\3\2\2\2G\u015c\3\2\2\2")
        buf.write("I\u0162\3\2\2\2K\u0165\3\2\2\2M\u016b\3\2\2\2O\u0174\3")
        buf.write("\2\2\2Q\u0177\3\2\2\2S\u017c\3\2\2\2U\u0181\3\2\2\2W\u0187")
        buf.write("\3\2\2\2Y\u018b\3\2\2\2[\u018f\3\2\2\2]\u0193\3\2\2\2")
        buf.write("_\u0196\3\2\2\2a\u0198\3\2\2\2c\u019a\3\2\2\2e\u019c\3")
        buf.write("\2\2\2g\u019e\3\2\2\2i\u01a0\3\2\2\2k\u01a4\3\2\2\2m\u01a8")
        buf.write("\3\2\2\2o\u01ab\3\2\2\2q\u01ad\3\2\2\2s\u01b0\3\2\2\2")
        buf.write("u\u01b3\3\2\2\2w\u01b5\3\2\2\2y\u01b8\3\2\2\2{\u01ba\3")
        buf.write("\2\2\2}\u01bd\3\2\2\2\177\u01c1\3\2\2\2\u0081\u01c4\3")
        buf.write("\2\2\2\u0083\u01d2\3\2\2\2\u0085\u01d5\3\2\2\2\u0087\u01db")
        buf.write("\3\2\2\2\u0089\u01e7\3\2\2\2\u008b\u01f5\3\2\2\2\u008d")
        buf.write("\u008e\7t\2\2\u008e\u008f\7g\2\2\u008f\u0090\7c\2\2\u0090")
        buf.write("\u0091\7f\2\2\u0091\u0092\7P\2\2\u0092\u0093\7w\2\2\u0093")
        buf.write("\u0094\7o\2\2\u0094\u0095\7d\2\2\u0095\u0096\7g\2\2\u0096")
        buf.write("\u0097\7t\2\2\u0097\4\3\2\2\2\u0098\u0099\7y\2\2\u0099")
        buf.write("\u009a\7t\2\2\u009a\u009b\7k\2\2\u009b\u009c\7v\2\2\u009c")
        buf.write("\u009d\7g\2\2\u009d\u009e\7P\2\2\u009e\u009f\7w\2\2\u009f")
        buf.write("\u00a0\7o\2\2\u00a0\u00a1\7d\2\2\u00a1\u00a2\7g\2\2\u00a2")
        buf.write("\u00a3\7t\2\2\u00a3\6\3\2\2\2\u00a4\u00a5\7t\2\2\u00a5")
        buf.write("\u00a6\7g\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8\7f\2\2\u00a8")
        buf.write("\u00a9\7D\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab\7q\2\2\u00ab")
        buf.write("\u00ac\7n\2\2\u00ac\b\3\2\2\2\u00ad\u00ae\7y\2\2\u00ae")
        buf.write("\u00af\7t\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7v\2\2\u00b1")
        buf.write("\u00b2\7g\2\2\u00b2\u00b3\7D\2\2\u00b3\u00b4\7q\2\2\u00b4")
        buf.write("\u00b5\7q\2\2\u00b5\u00b6\7n\2\2\u00b6\n\3\2\2\2\u00b7")
        buf.write("\u00b8\7t\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7c\2\2\u00ba")
        buf.write("\u00bb\7f\2\2\u00bb\u00bc\7U\2\2\u00bc\u00bd\7v\2\2\u00bd")
        buf.write("\u00be\7t\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7p\2\2\u00c0")
        buf.write("\u00c1\7i\2\2\u00c1\f\3\2\2\2\u00c2\u00c3\7y\2\2\u00c3")
        buf.write("\u00c4\7t\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7v\2\2\u00c6")
        buf.write("\u00c7\7g\2\2\u00c7\u00c8\7U\2\2\u00c8\u00c9\7v\2\2\u00c9")
        buf.write("\u00ca\7t\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7p\2\2\u00cc")
        buf.write("\u00cd\7i\2\2\u00cd\16\3\2\2\2\u00ce\u00d3\5\21\t\2\u00cf")
        buf.write("\u00d2\5\21\t\2\u00d0\u00d2\5\31\r\2\u00d1\u00cf\3\2\2")
        buf.write("\2\u00d1\u00d0\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1")
        buf.write("\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\20\3\2\2\2\u00d5\u00d3")
        buf.write("\3\2\2\2\u00d6\u00d7\t\2\2\2\u00d7\22\3\2\2\2\u00d8\u00d9")
        buf.write("\5\33\16\2\u00d9\u00da\5\37\20\2\u00da\u00e6\3\2\2\2\u00db")
        buf.write("\u00dc\5\33\16\2\u00dc\u00de\5\35\17\2\u00dd\u00df\5\37")
        buf.write("\20\2\u00de\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e6")
        buf.write("\3\2\2\2\u00e0\u00e2\t\3\2\2\u00e1\u00e0\3\2\2\2\u00e2")
        buf.write("\u00e3\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2")
        buf.write("\u00e4\u00e6\3\2\2\2\u00e5\u00d8\3\2\2\2\u00e5\u00db\3")
        buf.write("\2\2\2\u00e5\u00e1\3\2\2\2\u00e6\24\3\2\2\2\u00e7\u00ea")
        buf.write("\5\65\33\2\u00e8\u00ea\5\67\34\2\u00e9\u00e7\3\2\2\2\u00e9")
        buf.write("\u00e8\3\2\2\2\u00ea\26\3\2\2\2\u00eb\u00f1\7$\2\2\u00ec")
        buf.write("\u00f0\5!\21\2\u00ed\u00f0\5#\22\2\u00ee\u00f0\5%\23\2")
        buf.write("\u00ef\u00ec\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3")
        buf.write("\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2")
        buf.write("\3\2\2\2\u00f2\u00f4\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4")
        buf.write("\u00f5\7$\2\2\u00f5\u00f6\b\f\2\2\u00f6\30\3\2\2\2\u00f7")
        buf.write("\u00f8\t\3\2\2\u00f8\32\3\2\2\2\u00f9\u00fb\5\31\r\2\u00fa")
        buf.write("\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fa\3\2\2\2")
        buf.write("\u00fc\u00fd\3\2\2\2\u00fd\34\3\2\2\2\u00fe\u0102\7\60")
        buf.write("\2\2\u00ff\u0101\5\31\r\2\u0100\u00ff\3\2\2\2\u0101\u0104")
        buf.write("\3\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103")
        buf.write("\36\3\2\2\2\u0104\u0102\3\2\2\2\u0105\u0107\t\4\2\2\u0106")
        buf.write("\u0108\t\5\2\2\u0107\u0106\3\2\2\2\u0107\u0108\3\2\2\2")
        buf.write("\u0108\u010a\3\2\2\2\u0109\u010b\5\31\r\2\u010a\u0109")
        buf.write("\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010a\3\2\2\2\u010c")
        buf.write("\u010d\3\2\2\2\u010d \3\2\2\2\u010e\u010f\n\6\2\2\u010f")
        buf.write("\"\3\2\2\2\u0110\u0111\7^\2\2\u0111\u0112\t\7\2\2\u0112")
        buf.write("$\3\2\2\2\u0113\u0114\7)\2\2\u0114\u0115\7$\2\2\u0115")
        buf.write("&\3\2\2\2\u0116\u0117\7.\2\2\u0117(\3\2\2\2\u0118\u0119")
        buf.write("\7\f\2\2\u0119*\3\2\2\2\u011a\u011b\7*\2\2\u011b,\3\2")
        buf.write("\2\2\u011c\u011d\7+\2\2\u011d.\3\2\2\2\u011e\u011f\7]")
        buf.write("\2\2\u011f\60\3\2\2\2\u0120\u0121\7_\2\2\u0121\62\3\2")
        buf.write("\2\2\u0122\u0123\7h\2\2\u0123\u0124\7w\2\2\u0124\u0125")
        buf.write("\7p\2\2\u0125\u0126\7e\2\2\u0126\64\3\2\2\2\u0127\u0128")
        buf.write("\7v\2\2\u0128\u0129\7t\2\2\u0129\u012a\7w\2\2\u012a\u012b")
        buf.write("\7g\2\2\u012b\66\3\2\2\2\u012c\u012d\7h\2\2\u012d\u012e")
        buf.write("\7c\2\2\u012e\u012f\7n\2\2\u012f\u0130\7u\2\2\u0130\u0131")
        buf.write("\7g\2\2\u01318\3\2\2\2\u0132\u0133\7p\2\2\u0133\u0134")
        buf.write("\7w\2\2\u0134\u0135\7o\2\2\u0135\u0136\7d\2\2\u0136\u0137")
        buf.write("\7g\2\2\u0137\u0138\7t\2\2\u0138:\3\2\2\2\u0139\u013a")
        buf.write("\7d\2\2\u013a\u013b\7q\2\2\u013b\u013c\7q\2\2\u013c\u013d")
        buf.write("\7n\2\2\u013d<\3\2\2\2\u013e\u013f\7u\2\2\u013f\u0140")
        buf.write("\7v\2\2\u0140\u0141\7t\2\2\u0141\u0142\7k\2\2\u0142\u0143")
        buf.write("\7p\2\2\u0143\u0144\7i\2\2\u0144>\3\2\2\2\u0145\u0146")
        buf.write("\7t\2\2\u0146\u0147\7g\2\2\u0147\u0148\7v\2\2\u0148\u0149")
        buf.write("\7w\2\2\u0149\u014a\7t\2\2\u014a\u014b\7p\2\2\u014b@\3")
        buf.write("\2\2\2\u014c\u014d\7x\2\2\u014d\u014e\7c\2\2\u014e\u014f")
        buf.write("\7t\2\2\u014fB\3\2\2\2\u0150\u0151\7f\2\2\u0151\u0152")
        buf.write("\7{\2\2\u0152\u0153\7p\2\2\u0153\u0154\7c\2\2\u0154\u0155")
        buf.write("\7o\2\2\u0155\u0156\7k\2\2\u0156\u0157\7e\2\2\u0157D\3")
        buf.write("\2\2\2\u0158\u0159\7h\2\2\u0159\u015a\7q\2\2\u015a\u015b")
        buf.write("\7t\2\2\u015bF\3\2\2\2\u015c\u015d\7w\2\2\u015d\u015e")
        buf.write("\7p\2\2\u015e\u015f\7v\2\2\u015f\u0160\7k\2\2\u0160\u0161")
        buf.write("\7n\2\2\u0161H\3\2\2\2\u0162\u0163\7d\2\2\u0163\u0164")
        buf.write("\7{\2\2\u0164J\3\2\2\2\u0165\u0166\7d\2\2\u0166\u0167")
        buf.write("\7t\2\2\u0167\u0168\7g\2\2\u0168\u0169\7c\2\2\u0169\u016a")
        buf.write("\7m\2\2\u016aL\3\2\2\2\u016b\u016c\7e\2\2\u016c\u016d")
        buf.write("\7q\2\2\u016d\u016e\7p\2\2\u016e\u016f\7v\2\2\u016f\u0170")
        buf.write("\7k\2\2\u0170\u0171\7p\2\2\u0171\u0172\7w\2\2\u0172\u0173")
        buf.write("\7g\2\2\u0173N\3\2\2\2\u0174\u0175\7k\2\2\u0175\u0176")
        buf.write("\7h\2\2\u0176P\3\2\2\2\u0177\u0178\7g\2\2\u0178\u0179")
        buf.write("\7n\2\2\u0179\u017a\7u\2\2\u017a\u017b\7g\2\2\u017bR\3")
        buf.write("\2\2\2\u017c\u017d\7g\2\2\u017d\u017e\7n\2\2\u017e\u017f")
        buf.write("\7k\2\2\u017f\u0180\7h\2\2\u0180T\3\2\2\2\u0181\u0182")
        buf.write("\7d\2\2\u0182\u0183\7g\2\2\u0183\u0184\7i\2\2\u0184\u0185")
        buf.write("\7k\2\2\u0185\u0186\7p\2\2\u0186V\3\2\2\2\u0187\u0188")
        buf.write("\7g\2\2\u0188\u0189\7p\2\2\u0189\u018a\7f\2\2\u018aX\3")
        buf.write("\2\2\2\u018b\u018c\7p\2\2\u018c\u018d\7q\2\2\u018d\u018e")
        buf.write("\7v\2\2\u018eZ\3\2\2\2\u018f\u0190\7c\2\2\u0190\u0191")
        buf.write("\7p\2\2\u0191\u0192\7f\2\2\u0192\\\3\2\2\2\u0193\u0194")
        buf.write("\7q\2\2\u0194\u0195\7t\2\2\u0195^\3\2\2\2\u0196\u0197")
        buf.write("\7-\2\2\u0197`\3\2\2\2\u0198\u0199\7/\2\2\u0199b\3\2\2")
        buf.write("\2\u019a\u019b\7,\2\2\u019bd\3\2\2\2\u019c\u019d\7\61")
        buf.write("\2\2\u019df\3\2\2\2\u019e\u019f\7\'\2\2\u019fh\3\2\2\2")
        buf.write("\u01a0\u01a1\7p\2\2\u01a1\u01a2\7q\2\2\u01a2\u01a3\7v")
        buf.write("\2\2\u01a3j\3\2\2\2\u01a4\u01a5\7c\2\2\u01a5\u01a6\7p")
        buf.write("\2\2\u01a6\u01a7\7f\2\2\u01a7l\3\2\2\2\u01a8\u01a9\7q")
        buf.write("\2\2\u01a9\u01aa\7t\2\2\u01aan\3\2\2\2\u01ab\u01ac\7?")
        buf.write("\2\2\u01acp\3\2\2\2\u01ad\u01ae\7>\2\2\u01ae\u01af\7/")
        buf.write("\2\2\u01afr\3\2\2\2\u01b0\u01b1\7#\2\2\u01b1\u01b2\7?")
        buf.write("\2\2\u01b2t\3\2\2\2\u01b3\u01b4\7>\2\2\u01b4v\3\2\2\2")
        buf.write("\u01b5\u01b6\7>\2\2\u01b6\u01b7\7?\2\2\u01b7x\3\2\2\2")
        buf.write("\u01b8\u01b9\7@\2\2\u01b9z\3\2\2\2\u01ba\u01bb\7@\2\2")
        buf.write("\u01bb\u01bc\7?\2\2\u01bc|\3\2\2\2\u01bd\u01be\7\60\2")
        buf.write("\2\u01be\u01bf\7\60\2\2\u01bf\u01c0\7\60\2\2\u01c0~\3")
        buf.write("\2\2\2\u01c1\u01c2\7?\2\2\u01c2\u01c3\7?\2\2\u01c3\u0080")
        buf.write("\3\2\2\2\u01c4\u01c5\7%\2\2\u01c5\u01c6\7%\2\2\u01c6\u01ca")
        buf.write("\3\2\2\2\u01c7\u01c9\t\b\2\2\u01c8\u01c7\3\2\2\2\u01c9")
        buf.write("\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2")
        buf.write("\u01cb\u01cd\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01ce\b")
        buf.write("A\3\2\u01ce\u0082\3\2\2\2\u01cf\u01d0\7^\2\2\u01d0\u01d3")
        buf.write("\n\7\2\2\u01d1\u01d3\7^\2\2\u01d2\u01cf\3\2\2\2\u01d2")
        buf.write("\u01d1\3\2\2\2\u01d3\u0084\3\2\2\2\u01d4\u01d6\t\t\2\2")
        buf.write("\u01d5\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d5\3")
        buf.write("\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da")
        buf.write("\bC\3\2\u01da\u0086\3\2\2\2\u01db\u01e1\7$\2\2\u01dc\u01e0")
        buf.write("\5!\21\2\u01dd\u01e0\5#\22\2\u01de\u01e0\5%\23\2\u01df")
        buf.write("\u01dc\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01de\3\2\2\2")
        buf.write("\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e2\3")
        buf.write("\2\2\2\u01e2\u01e4\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4\u01e5")
        buf.write("\5\u0083B\2\u01e5\u01e6\bD\4\2\u01e6\u0088\3\2\2\2\u01e7")
        buf.write("\u01ed\7$\2\2\u01e8\u01ec\5!\21\2\u01e9\u01ec\5#\22\2")
        buf.write("\u01ea\u01ec\5%\23\2\u01eb\u01e8\3\2\2\2\u01eb\u01e9\3")
        buf.write("\2\2\2\u01eb\u01ea\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01eb")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f1\3\2\2\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01f0\u01f2\t\n\2\2\u01f1\u01f0\3\2\2\2")
        buf.write("\u01f2\u01f3\3\2\2\2\u01f3\u01f4\bE\5\2\u01f4\u008a\3")
        buf.write("\2\2\2\u01f5\u01f6\13\2\2\2\u01f6\u01f7\bF\6\2\u01f7\u008c")
        buf.write("\3\2\2\2\30\2\u00d1\u00d3\u00de\u00e3\u00e5\u00e9\u00ef")
        buf.write("\u00f1\u00fc\u0102\u0107\u010c\u01c8\u01ca\u01d2\u01d7")
        buf.write("\u01df\u01e1\u01eb\u01ed\u01f1\7\3\f\2\b\2\2\3D\3\3E\4")
        buf.write("\3F\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    IDENTIFIER = 7
    NUMBER_LIT = 8
    BOOLEAN_LIT = 9
    STRING_LIT = 10
    CM = 11
    NEWLINE = 12
    LRB = 13
    RRB = 14
    LSB = 15
    RSB = 16
    FUNC = 17
    TRUE = 18
    FALSE = 19
    NUMBER = 20
    BOOL = 21
    STRING = 22
    RETURN = 23
    VAR = 24
    DYNAMIC = 25
    FOR = 26
    UNTIL = 27
    BY = 28
    BREAK = 29
    CONTINUE = 30
    IF = 31
    ELSE = 32
    ELIF = 33
    BEGIN = 34
    END = 35
    NOT = 36
    AND = 37
    OR = 38
    PLUS = 39
    MINUS = 40
    MUL = 41
    DIV = 42
    MOD = 43
    NOT_OP = 44
    AND_OP = 45
    OR_OP = 46
    EQUAL = 47
    ASSIGN = 48
    NOT_EQUAL = 49
    SMALLER = 50
    SMALLER_EQUAL = 51
    LARGER = 52
    LARGER_EQUAL = 53
    THREE_DOT = 54
    DOUBLE_EQUAL = 55
    COMMENT = 56
    WS = 57
    ILLEGAL_ESCAPE = 58
    UNCLOSE_STRING = 59
    ERROR_TOKEN = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readNumber'", "'writeNumber'", "'readBool'", "'writeBool'", 
            "'readString'", "'writeString'", "','", "'\n'", "'('", "')'", 
            "'['", "']'", "'func'", "'true'", "'false'", "'number'", "'bool'", 
            "'string'", "'return'", "'var'", "'dynamic'", "'for'", "'until'", 
            "'by'", "'break'", "'continue'", "'if'", "'else'", "'elif'", 
            "'begin'", "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", 
            "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", "'...'", "'=='" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "NUMBER_LIT", "BOOLEAN_LIT", "STRING_LIT", "CM", 
            "NEWLINE", "LRB", "RRB", "LSB", "RSB", "FUNC", "TRUE", "FALSE", 
            "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FOR", 
            "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
            "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
            "NOT_OP", "AND_OP", "OR_OP", "EQUAL", "ASSIGN", "NOT_EQUAL", 
            "SMALLER", "SMALLER_EQUAL", "LARGER", "LARGER_EQUAL", "THREE_DOT", 
            "DOUBLE_EQUAL", "COMMENT", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "ERROR_TOKEN" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "IDENTIFIER", 
                  "Letter", "NUMBER_LIT", "BOOLEAN_LIT", "STRING_LIT", "DIGIT", 
                  "INTEGER_PART", "DECIMAL_PART", "EXPONENT_PART", "Character", 
                  "Escape_seq", "Double_quote_instring", "CM", "NEWLINE", 
                  "LRB", "RRB", "LSB", "RSB", "FUNC", "TRUE", "FALSE", "NUMBER", 
                  "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FOR", "UNTIL", 
                  "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                  "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MUL", "DIV", 
                  "MOD", "NOT_OP", "AND_OP", "OR_OP", "EQUAL", "ASSIGN", 
                  "NOT_EQUAL", "SMALLER", "SMALLER_EQUAL", "LARGER", "LARGER_EQUAL", 
                  "THREE_DOT", "DOUBLE_EQUAL", "COMMENT", "Illigal_escape", 
                  "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_TOKEN" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[10] = self.STRING_LIT_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.UNCLOSE_STRING_action 
            actions[68] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                string_to_illegal = str(self.text)
                raise IllegalEscape(string_to_illegal[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise UncloseString(self.text[1:])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)

     


