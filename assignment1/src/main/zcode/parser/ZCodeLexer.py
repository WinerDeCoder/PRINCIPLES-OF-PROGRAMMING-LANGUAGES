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
        buf.write("\u01f3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3/\3/\7/\u0171\n/\f/\16/\u0174\13/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\5\60\u017c\n\60\3\60\6\60\u017f\n")
        buf.write("\60\r\60\16\60\u0180\5\60\u0183\n\60\3\61\3\61\5\61\u0187")
        buf.write("\n\61\3\62\3\62\3\62\3\62\7\62\u018d\n\62\f\62\16\62\u0190")
        buf.write("\13\62\3\62\3\62\3\62\3\63\3\63\3\64\6\64\u0198\n\64\r")
        buf.write("\64\16\64\u0199\3\65\3\65\7\65\u019e\n\65\f\65\16\65\u01a1")
        buf.write("\13\65\3\66\3\66\5\66\u01a5\n\66\3\66\6\66\u01a8\n\66")
        buf.write("\r\66\16\66\u01a9\3\67\3\67\38\38\38\39\39\39\3:\3:\3")
        buf.write(";\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3@\3@\7@\u01c4\n@\f")
        buf.write("@\16@\u01c7\13@\3@\3@\3A\3A\3A\5A\u01ce\nA\3B\6B\u01d1")
        buf.write("\nB\rB\16B\u01d2\3B\3B\3C\3C\3C\3C\7C\u01db\nC\fC\16C")
        buf.write("\u01de\13C\3C\3C\3C\3D\3D\3D\3D\7D\u01e7\nD\fD\16D\u01ea")
        buf.write("\13D\3D\5D\u01ed\nD\3D\3D\3E\3E\3E\2\2F\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\2g\2i\2k\2m\2o\2q\2s\64u\65w\66y\67{8}9")
        buf.write("\177:\u0081\2\u0083;\u0085<\u0087=\u0089>\3\2\f\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--//\6\2\n\f\16")
        buf.write("\17$$^^\t\2))^^ddhhppttvv\4\2\f\f\60\60\5\2\n\13\16\16")
        buf.write("\"\"\5\3\n\f\16\17^^\2\u0200\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2")
        buf.write("\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\3\u008b")
        buf.write("\3\2\2\2\5\u0096\3\2\2\2\7\u00a2\3\2\2\2\t\u00ab\3\2\2")
        buf.write("\2\13\u00b5\3\2\2\2\r\u00c0\3\2\2\2\17\u00cc\3\2\2\2\21")
        buf.write("\u00ce\3\2\2\2\23\u00d0\3\2\2\2\25\u00d2\3\2\2\2\27\u00d4")
        buf.write("\3\2\2\2\31\u00d6\3\2\2\2\33\u00da\3\2\2\2\35\u00de\3")
        buf.write("\2\2\2\37\u00e1\3\2\2\2!\u00e3\3\2\2\2#\u00e6\3\2\2\2")
        buf.write("%\u00e9\3\2\2\2\'\u00eb\3\2\2\2)\u00ee\3\2\2\2+\u00f0")
        buf.write("\3\2\2\2-\u00f3\3\2\2\2/\u00f7\3\2\2\2\61\u00fa\3\2\2")
        buf.write("\2\63\u00ff\3\2\2\2\65\u0104\3\2\2\2\67\u010a\3\2\2\2")
        buf.write("9\u0111\3\2\2\2;\u0116\3\2\2\2=\u011d\3\2\2\2?\u0124\3")
        buf.write("\2\2\2A\u0128\3\2\2\2C\u0130\3\2\2\2E\u0134\3\2\2\2G\u013a")
        buf.write("\3\2\2\2I\u013d\3\2\2\2K\u0143\3\2\2\2M\u014c\3\2\2\2")
        buf.write("O\u014f\3\2\2\2Q\u0154\3\2\2\2S\u0159\3\2\2\2U\u015f\3")
        buf.write("\2\2\2W\u0163\3\2\2\2Y\u0167\3\2\2\2[\u016b\3\2\2\2]\u016e")
        buf.write("\3\2\2\2_\u0182\3\2\2\2a\u0186\3\2\2\2c\u0188\3\2\2\2")
        buf.write("e\u0194\3\2\2\2g\u0197\3\2\2\2i\u019b\3\2\2\2k\u01a2\3")
        buf.write("\2\2\2m\u01ab\3\2\2\2o\u01ad\3\2\2\2q\u01b0\3\2\2\2s\u01b3")
        buf.write("\3\2\2\2u\u01b5\3\2\2\2w\u01b7\3\2\2\2y\u01b9\3\2\2\2")
        buf.write("{\u01bb\3\2\2\2}\u01bd\3\2\2\2\177\u01bf\3\2\2\2\u0081")
        buf.write("\u01cd\3\2\2\2\u0083\u01d0\3\2\2\2\u0085\u01d6\3\2\2\2")
        buf.write("\u0087\u01e2\3\2\2\2\u0089\u01f0\3\2\2\2\u008b\u008c\7")
        buf.write("t\2\2\u008c\u008d\7g\2\2\u008d\u008e\7c\2\2\u008e\u008f")
        buf.write("\7f\2\2\u008f\u0090\7P\2\2\u0090\u0091\7w\2\2\u0091\u0092")
        buf.write("\7o\2\2\u0092\u0093\7d\2\2\u0093\u0094\7g\2\2\u0094\u0095")
        buf.write("\7t\2\2\u0095\4\3\2\2\2\u0096\u0097\7y\2\2\u0097\u0098")
        buf.write("\7t\2\2\u0098\u0099\7k\2\2\u0099\u009a\7v\2\2\u009a\u009b")
        buf.write("\7g\2\2\u009b\u009c\7P\2\2\u009c\u009d\7w\2\2\u009d\u009e")
        buf.write("\7o\2\2\u009e\u009f\7d\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1")
        buf.write("\7t\2\2\u00a1\6\3\2\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4")
        buf.write("\7g\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7f\2\2\u00a6\u00a7")
        buf.write("\7D\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa")
        buf.write("\7n\2\2\u00aa\b\3\2\2\2\u00ab\u00ac\7y\2\2\u00ac\u00ad")
        buf.write("\7t\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af\7v\2\2\u00af\u00b0")
        buf.write("\7g\2\2\u00b0\u00b1\7D\2\2\u00b1\u00b2\7q\2\2\u00b2\u00b3")
        buf.write("\7q\2\2\u00b3\u00b4\7n\2\2\u00b4\n\3\2\2\2\u00b5\u00b6")
        buf.write("\7t\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7c\2\2\u00b8\u00b9")
        buf.write("\7f\2\2\u00b9\u00ba\7U\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be\7p\2\2\u00be\u00bf")
        buf.write("\7i\2\2\u00bf\f\3\2\2\2\u00c0\u00c1\7y\2\2\u00c1\u00c2")
        buf.write("\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\u00c6\7U\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb")
        buf.write("\7i\2\2\u00cb\16\3\2\2\2\u00cc\u00cd\7-\2\2\u00cd\20\3")
        buf.write("\2\2\2\u00ce\u00cf\7/\2\2\u00cf\22\3\2\2\2\u00d0\u00d1")
        buf.write("\7,\2\2\u00d1\24\3\2\2\2\u00d2\u00d3\7\61\2\2\u00d3\26")
        buf.write("\3\2\2\2\u00d4\u00d5\7\'\2\2\u00d5\30\3\2\2\2\u00d6\u00d7")
        buf.write("\7p\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7v\2\2\u00d9\32")
        buf.write("\3\2\2\2\u00da\u00db\7c\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd")
        buf.write("\7f\2\2\u00dd\34\3\2\2\2\u00de\u00df\7q\2\2\u00df\u00e0")
        buf.write("\7t\2\2\u00e0\36\3\2\2\2\u00e1\u00e2\7?\2\2\u00e2 \3\2")
        buf.write("\2\2\u00e3\u00e4\7>\2\2\u00e4\u00e5\7/\2\2\u00e5\"\3\2")
        buf.write("\2\2\u00e6\u00e7\7#\2\2\u00e7\u00e8\7?\2\2\u00e8$\3\2")
        buf.write("\2\2\u00e9\u00ea\7>\2\2\u00ea&\3\2\2\2\u00eb\u00ec\7>")
        buf.write("\2\2\u00ec\u00ed\7?\2\2\u00ed(\3\2\2\2\u00ee\u00ef\7@")
        buf.write("\2\2\u00ef*\3\2\2\2\u00f0\u00f1\7@\2\2\u00f1\u00f2\7?")
        buf.write("\2\2\u00f2,\3\2\2\2\u00f3\u00f4\7\60\2\2\u00f4\u00f5\7")
        buf.write("\60\2\2\u00f5\u00f6\7\60\2\2\u00f6.\3\2\2\2\u00f7\u00f8")
        buf.write("\7?\2\2\u00f8\u00f9\7?\2\2\u00f9\60\3\2\2\2\u00fa\u00fb")
        buf.write("\7h\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe")
        buf.write("\7e\2\2\u00fe\62\3\2\2\2\u00ff\u0100\7v\2\2\u0100\u0101")
        buf.write("\7t\2\2\u0101\u0102\7w\2\2\u0102\u0103\7g\2\2\u0103\64")
        buf.write("\3\2\2\2\u0104\u0105\7h\2\2\u0105\u0106\7c\2\2\u0106\u0107")
        buf.write("\7n\2\2\u0107\u0108\7u\2\2\u0108\u0109\7g\2\2\u0109\66")
        buf.write("\3\2\2\2\u010a\u010b\7p\2\2\u010b\u010c\7w\2\2\u010c\u010d")
        buf.write("\7o\2\2\u010d\u010e\7d\2\2\u010e\u010f\7g\2\2\u010f\u0110")
        buf.write("\7t\2\2\u01108\3\2\2\2\u0111\u0112\7d\2\2\u0112\u0113")
        buf.write("\7q\2\2\u0113\u0114\7q\2\2\u0114\u0115\7n\2\2\u0115:\3")
        buf.write("\2\2\2\u0116\u0117\7u\2\2\u0117\u0118\7v\2\2\u0118\u0119")
        buf.write("\7t\2\2\u0119\u011a\7k\2\2\u011a\u011b\7p\2\2\u011b\u011c")
        buf.write("\7i\2\2\u011c<\3\2\2\2\u011d\u011e\7t\2\2\u011e\u011f")
        buf.write("\7g\2\2\u011f\u0120\7v\2\2\u0120\u0121\7w\2\2\u0121\u0122")
        buf.write("\7t\2\2\u0122\u0123\7p\2\2\u0123>\3\2\2\2\u0124\u0125")
        buf.write("\7x\2\2\u0125\u0126\7c\2\2\u0126\u0127\7t\2\2\u0127@\3")
        buf.write("\2\2\2\u0128\u0129\7f\2\2\u0129\u012a\7{\2\2\u012a\u012b")
        buf.write("\7p\2\2\u012b\u012c\7c\2\2\u012c\u012d\7o\2\2\u012d\u012e")
        buf.write("\7k\2\2\u012e\u012f\7e\2\2\u012fB\3\2\2\2\u0130\u0131")
        buf.write("\7h\2\2\u0131\u0132\7q\2\2\u0132\u0133\7t\2\2\u0133D\3")
        buf.write("\2\2\2\u0134\u0135\7w\2\2\u0135\u0136\7p\2\2\u0136\u0137")
        buf.write("\7v\2\2\u0137\u0138\7k\2\2\u0138\u0139\7n\2\2\u0139F\3")
        buf.write("\2\2\2\u013a\u013b\7d\2\2\u013b\u013c\7{\2\2\u013cH\3")
        buf.write("\2\2\2\u013d\u013e\7d\2\2\u013e\u013f\7t\2\2\u013f\u0140")
        buf.write("\7g\2\2\u0140\u0141\7c\2\2\u0141\u0142\7m\2\2\u0142J\3")
        buf.write("\2\2\2\u0143\u0144\7e\2\2\u0144\u0145\7q\2\2\u0145\u0146")
        buf.write("\7p\2\2\u0146\u0147\7v\2\2\u0147\u0148\7k\2\2\u0148\u0149")
        buf.write("\7p\2\2\u0149\u014a\7w\2\2\u014a\u014b\7g\2\2\u014bL\3")
        buf.write("\2\2\2\u014c\u014d\7k\2\2\u014d\u014e\7h\2\2\u014eN\3")
        buf.write("\2\2\2\u014f\u0150\7g\2\2\u0150\u0151\7n\2\2\u0151\u0152")
        buf.write("\7u\2\2\u0152\u0153\7g\2\2\u0153P\3\2\2\2\u0154\u0155")
        buf.write("\7g\2\2\u0155\u0156\7n\2\2\u0156\u0157\7k\2\2\u0157\u0158")
        buf.write("\7h\2\2\u0158R\3\2\2\2\u0159\u015a\7d\2\2\u015a\u015b")
        buf.write("\7g\2\2\u015b\u015c\7i\2\2\u015c\u015d\7k\2\2\u015d\u015e")
        buf.write("\7p\2\2\u015eT\3\2\2\2\u015f\u0160\7g\2\2\u0160\u0161")
        buf.write("\7p\2\2\u0161\u0162\7f\2\2\u0162V\3\2\2\2\u0163\u0164")
        buf.write("\7p\2\2\u0164\u0165\7q\2\2\u0165\u0166\7v\2\2\u0166X\3")
        buf.write("\2\2\2\u0167\u0168\7c\2\2\u0168\u0169\7p\2\2\u0169\u016a")
        buf.write("\7f\2\2\u016aZ\3\2\2\2\u016b\u016c\7q\2\2\u016c\u016d")
        buf.write("\7t\2\2\u016d\\\3\2\2\2\u016e\u0172\t\2\2\2\u016f\u0171")
        buf.write("\t\3\2\2\u0170\u016f\3\2\2\2\u0171\u0174\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173^\3\2\2\2\u0174")
        buf.write("\u0172\3\2\2\2\u0175\u0176\5g\64\2\u0176\u0177\5k\66\2")
        buf.write("\u0177\u0183\3\2\2\2\u0178\u0179\5g\64\2\u0179\u017b\5")
        buf.write("i\65\2\u017a\u017c\5k\66\2\u017b\u017a\3\2\2\2\u017b\u017c")
        buf.write("\3\2\2\2\u017c\u0183\3\2\2\2\u017d\u017f\t\4\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u017e\3\2\2\2")
        buf.write("\u0180\u0181\3\2\2\2\u0181\u0183\3\2\2\2\u0182\u0175\3")
        buf.write("\2\2\2\u0182\u0178\3\2\2\2\u0182\u017e\3\2\2\2\u0183`")
        buf.write("\3\2\2\2\u0184\u0187\5\63\32\2\u0185\u0187\5\65\33\2\u0186")
        buf.write("\u0184\3\2\2\2\u0186\u0185\3\2\2\2\u0187b\3\2\2\2\u0188")
        buf.write("\u018e\7$\2\2\u0189\u018d\5m\67\2\u018a\u018d\5o8\2\u018b")
        buf.write("\u018d\5q9\2\u018c\u0189\3\2\2\2\u018c\u018a\3\2\2\2\u018c")
        buf.write("\u018b\3\2\2\2\u018d\u0190\3\2\2\2\u018e\u018c\3\2\2\2")
        buf.write("\u018e\u018f\3\2\2\2\u018f\u0191\3\2\2\2\u0190\u018e\3")
        buf.write("\2\2\2\u0191\u0192\7$\2\2\u0192\u0193\b\62\2\2\u0193d")
        buf.write("\3\2\2\2\u0194\u0195\t\4\2\2\u0195f\3\2\2\2\u0196\u0198")
        buf.write("\5e\63\2\u0197\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019ah\3\2\2\2\u019b")
        buf.write("\u019f\7\60\2\2\u019c\u019e\5e\63\2\u019d\u019c\3\2\2")
        buf.write("\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0")
        buf.write("\3\2\2\2\u01a0j\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a4")
        buf.write("\t\5\2\2\u01a3\u01a5\t\6\2\2\u01a4\u01a3\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5\u01a7\3\2\2\2\u01a6\u01a8\5e\63\2")
        buf.write("\u01a7\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01a7\3")
        buf.write("\2\2\2\u01a9\u01aa\3\2\2\2\u01aal\3\2\2\2\u01ab\u01ac")
        buf.write("\n\7\2\2\u01acn\3\2\2\2\u01ad\u01ae\7^\2\2\u01ae\u01af")
        buf.write("\t\b\2\2\u01afp\3\2\2\2\u01b0\u01b1\7)\2\2\u01b1\u01b2")
        buf.write("\7$\2\2\u01b2r\3\2\2\2\u01b3\u01b4\7.\2\2\u01b4t\3\2\2")
        buf.write("\2\u01b5\u01b6\7\f\2\2\u01b6v\3\2\2\2\u01b7\u01b8\7*\2")
        buf.write("\2\u01b8x\3\2\2\2\u01b9\u01ba\7+\2\2\u01baz\3\2\2\2\u01bb")
        buf.write("\u01bc\7]\2\2\u01bc|\3\2\2\2\u01bd\u01be\7_\2\2\u01be")
        buf.write("~\3\2\2\2\u01bf\u01c0\7%\2\2\u01c0\u01c1\7%\2\2\u01c1")
        buf.write("\u01c5\3\2\2\2\u01c2\u01c4\t\t\2\2\u01c3\u01c2\3\2\2\2")
        buf.write("\u01c4\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3")
        buf.write("\2\2\2\u01c6\u01c8\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01c9")
        buf.write("\b@\3\2\u01c9\u0080\3\2\2\2\u01ca\u01cb\7^\2\2\u01cb\u01ce")
        buf.write("\n\b\2\2\u01cc\u01ce\7^\2\2\u01cd\u01ca\3\2\2\2\u01cd")
        buf.write("\u01cc\3\2\2\2\u01ce\u0082\3\2\2\2\u01cf\u01d1\t\n\2\2")
        buf.write("\u01d0\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d0\3")
        buf.write("\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5")
        buf.write("\bB\3\2\u01d5\u0084\3\2\2\2\u01d6\u01dc\7$\2\2\u01d7\u01db")
        buf.write("\5m\67\2\u01d8\u01db\5o8\2\u01d9\u01db\5q9\2\u01da\u01d7")
        buf.write("\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01d9\3\2\2\2\u01db")
        buf.write("\u01de\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2")
        buf.write("\u01dd\u01df\3\2\2\2\u01de\u01dc\3\2\2\2\u01df\u01e0\5")
        buf.write("\u0081A\2\u01e0\u01e1\bC\4\2\u01e1\u0086\3\2\2\2\u01e2")
        buf.write("\u01e8\7$\2\2\u01e3\u01e7\5m\67\2\u01e4\u01e7\5o8\2\u01e5")
        buf.write("\u01e7\5q9\2\u01e6\u01e3\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6")
        buf.write("\u01e5\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3\2\2\2")
        buf.write("\u01e8\u01e9\3\2\2\2\u01e9\u01ec\3\2\2\2\u01ea\u01e8\3")
        buf.write("\2\2\2\u01eb\u01ed\t\13\2\2\u01ec\u01eb\3\2\2\2\u01ed")
        buf.write("\u01ee\3\2\2\2\u01ee\u01ef\bD\5\2\u01ef\u0088\3\2\2\2")
        buf.write("\u01f0\u01f1\13\2\2\2\u01f1\u01f2\bE\6\2\u01f2\u008a\3")
        buf.write("\2\2\2\27\2\u0172\u017b\u0180\u0182\u0186\u018c\u018e")
        buf.write("\u0199\u019f\u01a4\u01a9\u01c3\u01c5\u01cd\u01d2\u01da")
        buf.write("\u01dc\u01e6\u01e8\u01ec\7\3\62\2\b\2\2\3C\3\3D\4\3E\5")
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
    PLUS = 7
    MINUS = 8
    MUL = 9
    DIV = 10
    MOD = 11
    NOT_OP = 12
    AND_OP = 13
    OR_OP = 14
    EQUAL = 15
    ASSIGN = 16
    NOT_EQUAL = 17
    SMALLER = 18
    SMALLER_EQUAL = 19
    LARGER = 20
    LARGER_EQUAL = 21
    THREE_DOT = 22
    DOUBLE_EQUAL = 23
    FUNCTION = 24
    TRUE = 25
    FALSE = 26
    NUMBER = 27
    BOOL = 28
    STRING = 29
    RETURN = 30
    VAR = 31
    DYNAMIC = 32
    FOR = 33
    UNTIL = 34
    BY = 35
    BREAK = 36
    CONTINUE = 37
    IF = 38
    ELSE = 39
    ELIF = 40
    BEGIN = 41
    END = 42
    NOT = 43
    AND = 44
    OR = 45
    IDENTIFIER = 46
    NUMBER_LIT = 47
    BOOLEAN_LIT = 48
    STRING_LIT = 49
    CM = 50
    NEWLINE = 51
    LRB = 52
    RRB = 53
    LSB = 54
    RSB = 55
    COMMENT = 56
    WS = 57
    ILLEGAL_ESCAPE = 58
    UNCLOSE_STRING = 59
    ERROR_TOKEN = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readNumber'", "'writeNumber'", "'readBool'", "'writeBool'", 
            "'readString'", "'writeString'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'func'", "'true'", "'false'", "'number'", 
            "'bool'", "'string'", "'return'", "'var'", "'dynamic'", "'for'", 
            "'until'", "'by'", "'break'", "'continue'", "'if'", "'else'", 
            "'elif'", "'begin'", "'end'", "','", "'\n'", "'('", "')'", "'['", 
            "']'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "MUL", "DIV", "MOD", "NOT_OP", "AND_OP", "OR_OP", 
            "EQUAL", "ASSIGN", "NOT_EQUAL", "SMALLER", "SMALLER_EQUAL", 
            "LARGER", "LARGER_EQUAL", "THREE_DOT", "DOUBLE_EQUAL", "FUNCTION", 
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", 
            "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "IDENTIFIER", 
            "NUMBER_LIT", "BOOLEAN_LIT", "STRING_LIT", "CM", "NEWLINE", 
            "LRB", "RRB", "LSB", "RSB", "COMMENT", "WS", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_TOKEN" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "PLUS", 
                  "MINUS", "MUL", "DIV", "MOD", "NOT_OP", "AND_OP", "OR_OP", 
                  "EQUAL", "ASSIGN", "NOT_EQUAL", "SMALLER", "SMALLER_EQUAL", 
                  "LARGER", "LARGER_EQUAL", "THREE_DOT", "DOUBLE_EQUAL", 
                  "FUNCTION", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                  "RETURN", "VAR", "DYNAMIC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "IDENTIFIER", "NUMBER_LIT", "BOOLEAN_LIT", 
                  "STRING_LIT", "DIGIT", "INTEGER_PART", "DECIMAL_PART", 
                  "EXPONENT_PART", "Character", "Escape_seq", "Double_quote_instring", 
                  "CM", "NEWLINE", "LRB", "RRB", "LSB", "RSB", "COMMENT", 
                  "Illigal_escape", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "ERROR_TOKEN" ]

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
            actions[48] = self.STRING_LIT_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[67] = self.ERROR_TOKEN_action 
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

            	if self.text[-1] in ['\b', '\t', '\f', '\r', '\n' ]:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)

     


