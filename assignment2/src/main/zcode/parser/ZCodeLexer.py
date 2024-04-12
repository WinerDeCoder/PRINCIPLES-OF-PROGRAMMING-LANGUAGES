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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u019c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\3\3\3\3\3\5\3\177\n\3\5\3\u0081")
        buf.write("\n\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u0089\n\4\f\4\16\4\u008c")
        buf.write("\13\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\5")
        buf.write("\'\u011e\n\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\7")
        buf.write("*\u012d\n*\f*\16*\u0130\13*\3+\3+\3+\3+\3+\3+\5+\u0138")
        buf.write("\n+\3+\6+\u013b\n+\r+\16+\u013c\5+\u013f\n+\3,\3,\3,\3")
        buf.write(",\7,\u0145\n,\f,\16,\u0148\13,\3,\3,\3,\3-\3-\3.\6.\u0150")
        buf.write("\n.\r.\16.\u0151\3/\3/\7/\u0156\n/\f/\16/\u0159\13/\3")
        buf.write("\60\3\60\5\60\u015d\n\60\3\60\6\60\u0160\n\60\r\60\16")
        buf.write("\60\u0161\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\58\u0177")
        buf.write("\n8\39\69\u017a\n9\r9\169\u017b\39\39\3:\3:\3:\3:\7:\u0184")
        buf.write("\n:\f:\16:\u0187\13:\3:\3:\3:\3;\3;\3;\3;\7;\u0190\n;")
        buf.write("\f;\16;\u0193\13;\3;\5;\u0196\n;\3;\3;\3<\3<\3<\2\2=\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y\2[\2]\2_\2a\2c\2e\2g.i/k\60m\61o\2q\62s\63u\64")
        buf.write("w\65\3\2\f\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2")
        buf.write("\62;\4\2GGgg\4\2--//\6\2\n\f\16\17$$^^\t\2))^^ddhhppt")
        buf.write("tvv\5\2\n\13\16\16\"\"\5\3\n\f\16\17^^\2\u01ab\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3")
        buf.write("y\3\2\2\2\5\u0080\3\2\2\2\7\u0084\3\2\2\2\t\u008f\3\2")
        buf.write("\2\2\13\u0091\3\2\2\2\r\u0093\3\2\2\2\17\u0095\3\2\2\2")
        buf.write("\21\u0097\3\2\2\2\23\u0099\3\2\2\2\25\u009b\3\2\2\2\27")
        buf.write("\u009e\3\2\2\2\31\u00a1\3\2\2\2\33\u00a3\3\2\2\2\35\u00a6")
        buf.write("\3\2\2\2\37\u00a8\3\2\2\2!\u00ab\3\2\2\2#\u00af\3\2\2")
        buf.write("\2%\u00b2\3\2\2\2\'\u00b7\3\2\2\2)\u00be\3\2\2\2+\u00c3")
        buf.write("\3\2\2\2-\u00ca\3\2\2\2/\u00d1\3\2\2\2\61\u00d5\3\2\2")
        buf.write("\2\63\u00dd\3\2\2\2\65\u00e1\3\2\2\2\67\u00e7\3\2\2\2")
        buf.write("9\u00ea\3\2\2\2;\u00f0\3\2\2\2=\u00f9\3\2\2\2?\u00fc\3")
        buf.write("\2\2\2A\u0101\3\2\2\2C\u0106\3\2\2\2E\u010c\3\2\2\2G\u0110")
        buf.write("\3\2\2\2I\u0114\3\2\2\2K\u0118\3\2\2\2M\u011d\3\2\2\2")
        buf.write("O\u011f\3\2\2\2Q\u0124\3\2\2\2S\u012a\3\2\2\2U\u013e\3")
        buf.write("\2\2\2W\u0140\3\2\2\2Y\u014c\3\2\2\2[\u014f\3\2\2\2]\u0153")
        buf.write("\3\2\2\2_\u015a\3\2\2\2a\u0163\3\2\2\2c\u0165\3\2\2\2")
        buf.write("e\u0168\3\2\2\2g\u016b\3\2\2\2i\u016d\3\2\2\2k\u016f\3")
        buf.write("\2\2\2m\u0171\3\2\2\2o\u0176\3\2\2\2q\u0179\3\2\2\2s\u017f")
        buf.write("\3\2\2\2u\u018b\3\2\2\2w\u0199\3\2\2\2yz\7.\2\2z\4\3\2")
        buf.write("\2\2{\u0081\7\f\2\2|~\7\17\2\2}\177\7\f\2\2~}\3\2\2\2")
        buf.write("~\177\3\2\2\2\177\u0081\3\2\2\2\u0080{\3\2\2\2\u0080|")
        buf.write("\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\b\3\2\2\u0083")
        buf.write("\6\3\2\2\2\u0084\u0085\7%\2\2\u0085\u0086\7%\2\2\u0086")
        buf.write("\u008a\3\2\2\2\u0087\u0089\n\2\2\2\u0088\u0087\3\2\2\2")
        buf.write("\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3")
        buf.write("\2\2\2\u008b\u008d\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u008e")
        buf.write("\b\4\3\2\u008e\b\3\2\2\2\u008f\u0090\7-\2\2\u0090\n\3")
        buf.write("\2\2\2\u0091\u0092\7/\2\2\u0092\f\3\2\2\2\u0093\u0094")
        buf.write("\7,\2\2\u0094\16\3\2\2\2\u0095\u0096\7\61\2\2\u0096\20")
        buf.write("\3\2\2\2\u0097\u0098\7\'\2\2\u0098\22\3\2\2\2\u0099\u009a")
        buf.write("\7?\2\2\u009a\24\3\2\2\2\u009b\u009c\7>\2\2\u009c\u009d")
        buf.write("\7/\2\2\u009d\26\3\2\2\2\u009e\u009f\7#\2\2\u009f\u00a0")
        buf.write("\7?\2\2\u00a0\30\3\2\2\2\u00a1\u00a2\7>\2\2\u00a2\32\3")
        buf.write("\2\2\2\u00a3\u00a4\7>\2\2\u00a4\u00a5\7?\2\2\u00a5\34")
        buf.write("\3\2\2\2\u00a6\u00a7\7@\2\2\u00a7\36\3\2\2\2\u00a8\u00a9")
        buf.write("\7@\2\2\u00a9\u00aa\7?\2\2\u00aa \3\2\2\2\u00ab\u00ac")
        buf.write("\7\60\2\2\u00ac\u00ad\7\60\2\2\u00ad\u00ae\7\60\2\2\u00ae")
        buf.write("\"\3\2\2\2\u00af\u00b0\7?\2\2\u00b0\u00b1\7?\2\2\u00b1")
        buf.write("$\3\2\2\2\u00b2\u00b3\7h\2\2\u00b3\u00b4\7w\2\2\u00b4")
        buf.write("\u00b5\7p\2\2\u00b5\u00b6\7e\2\2\u00b6&\3\2\2\2\u00b7")
        buf.write("\u00b8\7p\2\2\u00b8\u00b9\7w\2\2\u00b9\u00ba\7o\2\2\u00ba")
        buf.write("\u00bb\7d\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd\7t\2\2\u00bd")
        buf.write("(\3\2\2\2\u00be\u00bf\7d\2\2\u00bf\u00c0\7q\2\2\u00c0")
        buf.write("\u00c1\7q\2\2\u00c1\u00c2\7n\2\2\u00c2*\3\2\2\2\u00c3")
        buf.write("\u00c4\7u\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6\7t\2\2\u00c6")
        buf.write("\u00c7\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9\7i\2\2\u00c9")
        buf.write(",\3\2\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7g\2\2\u00cc")
        buf.write("\u00cd\7v\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf\7t\2\2\u00cf")
        buf.write("\u00d0\7p\2\2\u00d0.\3\2\2\2\u00d1\u00d2\7x\2\2\u00d2")
        buf.write("\u00d3\7c\2\2\u00d3\u00d4\7t\2\2\u00d4\60\3\2\2\2\u00d5")
        buf.write("\u00d6\7f\2\2\u00d6\u00d7\7{\2\2\u00d7\u00d8\7p\2\2\u00d8")
        buf.write("\u00d9\7c\2\2\u00d9\u00da\7o\2\2\u00da\u00db\7k\2\2\u00db")
        buf.write("\u00dc\7e\2\2\u00dc\62\3\2\2\2\u00dd\u00de\7h\2\2\u00de")
        buf.write("\u00df\7q\2\2\u00df\u00e0\7t\2\2\u00e0\64\3\2\2\2\u00e1")
        buf.write("\u00e2\7w\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7v\2\2\u00e4")
        buf.write("\u00e5\7k\2\2\u00e5\u00e6\7n\2\2\u00e6\66\3\2\2\2\u00e7")
        buf.write("\u00e8\7d\2\2\u00e8\u00e9\7{\2\2\u00e98\3\2\2\2\u00ea")
        buf.write("\u00eb\7d\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed\7g\2\2\u00ed")
        buf.write("\u00ee\7c\2\2\u00ee\u00ef\7m\2\2\u00ef:\3\2\2\2\u00f0")
        buf.write("\u00f1\7e\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7p\2\2\u00f3")
        buf.write("\u00f4\7v\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7p\2\2\u00f6")
        buf.write("\u00f7\7w\2\2\u00f7\u00f8\7g\2\2\u00f8<\3\2\2\2\u00f9")
        buf.write("\u00fa\7k\2\2\u00fa\u00fb\7h\2\2\u00fb>\3\2\2\2\u00fc")
        buf.write("\u00fd\7g\2\2\u00fd\u00fe\7n\2\2\u00fe\u00ff\7u\2\2\u00ff")
        buf.write("\u0100\7g\2\2\u0100@\3\2\2\2\u0101\u0102\7g\2\2\u0102")
        buf.write("\u0103\7n\2\2\u0103\u0104\7k\2\2\u0104\u0105\7h\2\2\u0105")
        buf.write("B\3\2\2\2\u0106\u0107\7d\2\2\u0107\u0108\7g\2\2\u0108")
        buf.write("\u0109\7i\2\2\u0109\u010a\7k\2\2\u010a\u010b\7p\2\2\u010b")
        buf.write("D\3\2\2\2\u010c\u010d\7g\2\2\u010d\u010e\7p\2\2\u010e")
        buf.write("\u010f\7f\2\2\u010fF\3\2\2\2\u0110\u0111\7p\2\2\u0111")
        buf.write("\u0112\7q\2\2\u0112\u0113\7v\2\2\u0113H\3\2\2\2\u0114")
        buf.write("\u0115\7c\2\2\u0115\u0116\7p\2\2\u0116\u0117\7f\2\2\u0117")
        buf.write("J\3\2\2\2\u0118\u0119\7q\2\2\u0119\u011a\7t\2\2\u011a")
        buf.write("L\3\2\2\2\u011b\u011e\5O(\2\u011c\u011e\5Q)\2\u011d\u011b")
        buf.write("\3\2\2\2\u011d\u011c\3\2\2\2\u011eN\3\2\2\2\u011f\u0120")
        buf.write("\7v\2\2\u0120\u0121\7t\2\2\u0121\u0122\7w\2\2\u0122\u0123")
        buf.write("\7g\2\2\u0123P\3\2\2\2\u0124\u0125\7h\2\2\u0125\u0126")
        buf.write("\7c\2\2\u0126\u0127\7n\2\2\u0127\u0128\7u\2\2\u0128\u0129")
        buf.write("\7g\2\2\u0129R\3\2\2\2\u012a\u012e\t\3\2\2\u012b\u012d")
        buf.write("\t\4\2\2\u012c\u012b\3\2\2\2\u012d\u0130\3\2\2\2\u012e")
        buf.write("\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012fT\3\2\2\2\u0130")
        buf.write("\u012e\3\2\2\2\u0131\u0132\5[.\2\u0132\u0133\5_\60\2\u0133")
        buf.write("\u013f\3\2\2\2\u0134\u0135\5[.\2\u0135\u0137\5]/\2\u0136")
        buf.write("\u0138\5_\60\2\u0137\u0136\3\2\2\2\u0137\u0138\3\2\2\2")
        buf.write("\u0138\u013f\3\2\2\2\u0139\u013b\t\5\2\2\u013a\u0139\3")
        buf.write("\2\2\2\u013b\u013c\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d")
        buf.write("\3\2\2\2\u013d\u013f\3\2\2\2\u013e\u0131\3\2\2\2\u013e")
        buf.write("\u0134\3\2\2\2\u013e\u013a\3\2\2\2\u013fV\3\2\2\2\u0140")
        buf.write("\u0146\7$\2\2\u0141\u0145\5a\61\2\u0142\u0145\5c\62\2")
        buf.write("\u0143\u0145\5e\63\2\u0144\u0141\3\2\2\2\u0144\u0142\3")
        buf.write("\2\2\2\u0144\u0143\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0149\3\2\2\2\u0148")
        buf.write("\u0146\3\2\2\2\u0149\u014a\7$\2\2\u014a\u014b\b,\4\2\u014b")
        buf.write("X\3\2\2\2\u014c\u014d\t\5\2\2\u014dZ\3\2\2\2\u014e\u0150")
        buf.write("\5Y-\2\u014f\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u014f")
        buf.write("\3\2\2\2\u0151\u0152\3\2\2\2\u0152\\\3\2\2\2\u0153\u0157")
        buf.write("\7\60\2\2\u0154\u0156\5Y-\2\u0155\u0154\3\2\2\2\u0156")
        buf.write("\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158^\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015c\t\6\2")
        buf.write("\2\u015b\u015d\t\7\2\2\u015c\u015b\3\2\2\2\u015c\u015d")
        buf.write("\3\2\2\2\u015d\u015f\3\2\2\2\u015e\u0160\5Y-\2\u015f\u015e")
        buf.write("\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u015f\3\2\2\2\u0161")
        buf.write("\u0162\3\2\2\2\u0162`\3\2\2\2\u0163\u0164\n\b\2\2\u0164")
        buf.write("b\3\2\2\2\u0165\u0166\7^\2\2\u0166\u0167\t\t\2\2\u0167")
        buf.write("d\3\2\2\2\u0168\u0169\7)\2\2\u0169\u016a\7$\2\2\u016a")
        buf.write("f\3\2\2\2\u016b\u016c\7*\2\2\u016ch\3\2\2\2\u016d\u016e")
        buf.write("\7+\2\2\u016ej\3\2\2\2\u016f\u0170\7]\2\2\u0170l\3\2\2")
        buf.write("\2\u0171\u0172\7_\2\2\u0172n\3\2\2\2\u0173\u0174\7^\2")
        buf.write("\2\u0174\u0177\n\t\2\2\u0175\u0177\7^\2\2\u0176\u0173")
        buf.write("\3\2\2\2\u0176\u0175\3\2\2\2\u0177p\3\2\2\2\u0178\u017a")
        buf.write("\t\n\2\2\u0179\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017d\3\2\2\2")
        buf.write("\u017d\u017e\b9\3\2\u017er\3\2\2\2\u017f\u0185\7$\2\2")
        buf.write("\u0180\u0184\5a\61\2\u0181\u0184\5c\62\2\u0182\u0184\5")
        buf.write("e\63\2\u0183\u0180\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0182")
        buf.write("\3\2\2\2\u0184\u0187\3\2\2\2\u0185\u0183\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186\u0188\3\2\2\2\u0187\u0185\3\2\2\2")
        buf.write("\u0188\u0189\5o8\2\u0189\u018a\b:\5\2\u018at\3\2\2\2\u018b")
        buf.write("\u0191\7$\2\2\u018c\u0190\5a\61\2\u018d\u0190\5c\62\2")
        buf.write("\u018e\u0190\5e\63\2\u018f\u018c\3\2\2\2\u018f\u018d\3")
        buf.write("\2\2\2\u018f\u018e\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0195\3\2\2\2\u0193")
        buf.write("\u0191\3\2\2\2\u0194\u0196\t\13\2\2\u0195\u0194\3\2\2")
        buf.write("\2\u0196\u0197\3\2\2\2\u0197\u0198\b;\6\2\u0198v\3\2\2")
        buf.write("\2\u0199\u019a\13\2\2\2\u019a\u019b\b<\7\2\u019bx\3\2")
        buf.write("\2\2\30\2~\u0080\u008a\u011d\u012e\u0137\u013c\u013e\u0144")
        buf.write("\u0146\u0151\u0157\u015c\u0161\u0176\u017b\u0183\u0185")
        buf.write("\u018f\u0191\u0195\b\3\3\2\b\2\2\3,\3\3:\4\3;\5\3<\6")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CM = 1
    NEWLINE = 2
    COMMENT = 3
    PLUS = 4
    MINUS = 5
    MUL = 6
    DIV = 7
    MOD = 8
    EQUAL = 9
    ASSIGN = 10
    NOT_EQUAL = 11
    SMALLER = 12
    SMALLER_EQUAL = 13
    LARGER = 14
    LARGER_EQUAL = 15
    THREE_DOT = 16
    DOUBLE_EQUAL = 17
    FUNCTION = 18
    NUMBER = 19
    BOOL = 20
    STRING = 21
    RETURN = 22
    VAR = 23
    DYNAMIC = 24
    FOR = 25
    UNTIL = 26
    BY = 27
    BREAK = 28
    CONTINUE = 29
    IF = 30
    ELSE = 31
    ELIF = 32
    BEGIN = 33
    END = 34
    NOT = 35
    AND = 36
    OR = 37
    BOOLEAN_LIT = 38
    TRUE = 39
    FALSE = 40
    IDENTIFIER = 41
    NUMBER_LIT = 42
    STRING_LIT = 43
    LRB = 44
    RRB = 45
    LSB = 46
    RSB = 47
    WS = 48
    ILLEGAL_ESCAPE = 49
    UNCLOSE_STRING = 50
    ERROR_TOKEN = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'func'", "'number'", 
            "'bool'", "'string'", "'return'", "'var'", "'dynamic'", "'for'", 
            "'until'", "'by'", "'break'", "'continue'", "'if'", "'else'", 
            "'elif'", "'begin'", "'end'", "'not'", "'and'", "'or'", "'true'", 
            "'false'", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "CM", "NEWLINE", "COMMENT", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
            "EQUAL", "ASSIGN", "NOT_EQUAL", "SMALLER", "SMALLER_EQUAL", 
            "LARGER", "LARGER_EQUAL", "THREE_DOT", "DOUBLE_EQUAL", "FUNCTION", 
            "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FOR", 
            "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
            "END", "NOT", "AND", "OR", "BOOLEAN_LIT", "TRUE", "FALSE", "IDENTIFIER", 
            "NUMBER_LIT", "STRING_LIT", "LRB", "RRB", "LSB", "RSB", "WS", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_TOKEN" ]

    ruleNames = [ "CM", "NEWLINE", "COMMENT", "PLUS", "MINUS", "MUL", "DIV", 
                  "MOD", "EQUAL", "ASSIGN", "NOT_EQUAL", "SMALLER", "SMALLER_EQUAL", 
                  "LARGER", "LARGER_EQUAL", "THREE_DOT", "DOUBLE_EQUAL", 
                  "FUNCTION", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
                  "DYNAMIC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", 
                  "BOOLEAN_LIT", "TRUE", "FALSE", "IDENTIFIER", "NUMBER_LIT", 
                  "STRING_LIT", "DIGIT", "INTEGER_PART", "DECIMAL_PART", 
                  "EXPONENT_PART", "Character", "Escape_seq", "Double_quote_instring", 
                  "LRB", "RRB", "LSB", "RSB", "Illigal_escape", "WS", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_TOKEN" ]

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
            actions[1] = self.NEWLINE_action 
            actions[42] = self.STRING_LIT_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            actions[57] = self.UNCLOSE_STRING_action 
            actions[58] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = '\n'
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                string_to_illegal = str(self.text)
                raise IllegalEscape(string_to_illegal[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		raise UncloseString(self.text[1:])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)

     


