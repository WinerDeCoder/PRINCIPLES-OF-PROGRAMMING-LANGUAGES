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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u01b4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2\3\3\3")
        buf.write("\3\6\3v\n\3\r\3\16\3w\3\4\3\4\5\4|\n\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u008c\n\6")
        buf.write("\3\7\3\7\3\7\7\7\u0091\n\7\f\7\16\7\u0094\13\7\3\7\5\7")
        buf.write("\u0097\n\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u009f\n\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\5\b\u00a6\n\b\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\5\13\u00b0\n\13\3\f\3\f\7\f\u00b4\n\f\f\f\16")
        buf.write("\f\u00b7\13\f\3\f\5\f\u00ba\n\f\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\5\24\u00da\n\24\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\26\3\26\3\26\7\26\u00e4\n\26\f\26\16\26\u00e7\13")
        buf.write("\26\3\26\5\26\u00ea\n\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\7\30\u00f3\n\30\f\30\16\30\u00f6\13\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0101\n\31\3")
        buf.write("\32\3\32\3\32\3\33\3\33\5\33\u0108\n\33\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\5\35\u0111\n\35\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\5\36\u0119\n\36\3\37\3\37\5\37\u011d\n\37")
        buf.write("\3 \3 \3 \3!\3!\3\"\3\"\5\"\u0126\n\"\3#\3#\3#\3$\3$\3")
        buf.write("$\3%\3%\3%\3%\3%\5%\u0133\n%\3&\3&\3&\3&\3&\5&\u013a\n")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u0142\n\'\f\'\16\'\u0145")
        buf.write("\13\'\3(\3(\3(\3(\3(\3(\7(\u014d\n(\f(\16(\u0150\13(\3")
        buf.write(")\3)\3)\3)\3)\3)\7)\u0158\n)\f)\16)\u015b\13)\3*\3*\3")
        buf.write("*\5*\u0160\n*\3+\3+\3+\5+\u0165\n+\3,\3,\3,\3,\3,\5,\u016c")
        buf.write("\n,\3-\3-\3-\3-\3-\3.\3.\3.\7.\u0176\n.\f.\16.\u0179\13")
        buf.write(".\3/\3/\5/\u017d\n/\3\60\3\60\5\60\u0181\n\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\5\61\u0189\n\61\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\7\65\u019c\n\65\f\65\16\65\u019f\13\65")
        buf.write("\3\66\3\66\3\66\7\66\u01a4\n\66\f\66\16\66\u01a7\13\66")
        buf.write("\3\67\6\67\u01aa\n\67\r\67\16\67\u01ab\38\78\u01af\n8")
        buf.write("\f8\168\u01b2\138\38\2\5LNP9\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjln\2\7\3\2\25\27\5\2\13\13\r\21\23\23\3\2&\'\3")
        buf.write("\2\6\7\3\2\b\n\2\u01ac\2p\3\2\2\2\4s\3\2\2\2\6{\3\2\2")
        buf.write("\2\b}\3\2\2\2\n\u008b\3\2\2\2\f\u0096\3\2\2\2\16\u00a5")
        buf.write("\3\2\2\2\20\u00a7\3\2\2\2\22\u00a9\3\2\2\2\24\u00af\3")
        buf.write("\2\2\2\26\u00b1\3\2\2\2\30\u00bb\3\2\2\2\32\u00be\3\2")
        buf.write("\2\2\34\u00c1\3\2\2\2\36\u00c4\3\2\2\2 \u00ca\3\2\2\2")
        buf.write("\"\u00d3\3\2\2\2$\u00d5\3\2\2\2&\u00d7\3\2\2\2(\u00db")
        buf.write("\3\2\2\2*\u00e9\3\2\2\2,\u00eb\3\2\2\2.\u00f4\3\2\2\2")
        buf.write("\60\u0100\3\2\2\2\62\u0102\3\2\2\2\64\u0107\3\2\2\2\66")
        buf.write("\u0109\3\2\2\28\u010d\3\2\2\2:\u0112\3\2\2\2<\u011a\3")
        buf.write("\2\2\2>\u011e\3\2\2\2@\u0121\3\2\2\2B\u0125\3\2\2\2D\u0127")
        buf.write("\3\2\2\2F\u012a\3\2\2\2H\u0132\3\2\2\2J\u0139\3\2\2\2")
        buf.write("L\u013b\3\2\2\2N\u0146\3\2\2\2P\u0151\3\2\2\2R\u015f\3")
        buf.write("\2\2\2T\u0164\3\2\2\2V\u016b\3\2\2\2X\u016d\3\2\2\2Z\u0172")
        buf.write("\3\2\2\2\\\u017c\3\2\2\2^\u0180\3\2\2\2`\u0188\3\2\2\2")
        buf.write("b\u018a\3\2\2\2d\u018f\3\2\2\2f\u0194\3\2\2\2h\u0198\3")
        buf.write("\2\2\2j\u01a0\3\2\2\2l\u01a9\3\2\2\2n\u01b0\3\2\2\2pq")
        buf.write("\5\4\3\2qr\7\2\2\3r\3\3\2\2\2su\5n8\2tv\5\6\4\2ut\3\2")
        buf.write("\2\2vw\3\2\2\2wu\3\2\2\2wx\3\2\2\2x\5\3\2\2\2y|\5\b\5")
        buf.write("\2z|\5\60\31\2{y\3\2\2\2{z\3\2\2\2|\7\3\2\2\2}~\7\24\2")
        buf.write("\2~\177\7+\2\2\177\u0080\7.\2\2\u0080\u0081\5\f\7\2\u0081")
        buf.write("\u0082\7/\2\2\u0082\u0083\5\n\6\2\u0083\u0084\5l\67\2")
        buf.write("\u0084\t\3\2\2\2\u0085\u0086\5n8\2\u0086\u0087\5&\24\2")
        buf.write("\u0087\u008c\3\2\2\2\u0088\u0089\5n8\2\u0089\u008a\5,")
        buf.write("\27\2\u008a\u008c\3\2\2\2\u008b\u0085\3\2\2\2\u008b\u0088")
        buf.write("\3\2\2\2\u008b\u008c\3\2\2\2\u008c\13\3\2\2\2\u008d\u0092")
        buf.write("\5B\"\2\u008e\u008f\7\3\2\2\u008f\u0091\5B\"\2\u0090\u008e")
        buf.write("\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092")
        buf.write("\u0093\3\2\2\2\u0093\u0097\3\2\2\2\u0094\u0092\3\2\2\2")
        buf.write("\u0095\u0097\3\2\2\2\u0096\u008d\3\2\2\2\u0096\u0095\3")
        buf.write("\2\2\2\u0097\r\3\2\2\2\u0098\u009f\5\22\n\2\u0099\u009f")
        buf.write("\5\"\22\2\u009a\u009f\5$\23\2\u009b\u009f\5&\24\2\u009c")
        buf.write("\u009f\5(\25\2\u009d\u009f\5,\27\2\u009e\u0098\3\2\2\2")
        buf.write("\u009e\u0099\3\2\2\2\u009e\u009a\3\2\2\2\u009e\u009b\3")
        buf.write("\2\2\2\u009e\u009c\3\2\2\2\u009e\u009d\3\2\2\2\u009f\u00a0")
        buf.write("\3\2\2\2\u00a0\u00a1\5l\67\2\u00a1\u00a6\3\2\2\2\u00a2")
        buf.write("\u00a6\5\20\t\2\u00a3\u00a6\5\26\f\2\u00a4\u00a6\5 \21")
        buf.write("\2\u00a5\u009e\3\2\2\2\u00a5\u00a2\3\2\2\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\17\3\2\2\2\u00a7\u00a8")
        buf.write("\5\60\31\2\u00a8\21\3\2\2\2\u00a9\u00aa\5\24\13\2\u00aa")
        buf.write("\u00ab\7\f\2\2\u00ab\u00ac\5H%\2\u00ac\23\3\2\2\2\u00ad")
        buf.write("\u00b0\7+\2\2\u00ae\u00b0\5X-\2\u00af\u00ad\3\2\2\2\u00af")
        buf.write("\u00ae\3\2\2\2\u00b0\25\3\2\2\2\u00b1\u00b5\5\30\r\2\u00b2")
        buf.write("\u00b4\5\32\16\2\u00b3\u00b2\3\2\2\2\u00b4\u00b7\3\2\2")
        buf.write("\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b9")
        buf.write("\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00ba\5\34\17\2\u00b9")
        buf.write("\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\27\3\2\2\2\u00bb")
        buf.write("\u00bc\7 \2\2\u00bc\u00bd\5\36\20\2\u00bd\31\3\2\2\2\u00be")
        buf.write("\u00bf\7\"\2\2\u00bf\u00c0\5\36\20\2\u00c0\33\3\2\2\2")
        buf.write("\u00c1\u00c2\7!\2\2\u00c2\u00c3\5\16\b\2\u00c3\35\3\2")
        buf.write("\2\2\u00c4\u00c5\7.\2\2\u00c5\u00c6\5H%\2\u00c6\u00c7")
        buf.write("\7/\2\2\u00c7\u00c8\5n8\2\u00c8\u00c9\5\16\b\2\u00c9\37")
        buf.write("\3\2\2\2\u00ca\u00cb\7\33\2\2\u00cb\u00cc\7+\2\2\u00cc")
        buf.write("\u00cd\7\34\2\2\u00cd\u00ce\5H%\2\u00ce\u00cf\7\35\2\2")
        buf.write("\u00cf\u00d0\5H%\2\u00d0\u00d1\5n8\2\u00d1\u00d2\5\16")
        buf.write("\b\2\u00d2!\3\2\2\2\u00d3\u00d4\7\36\2\2\u00d4#\3\2\2")
        buf.write("\2\u00d5\u00d6\7\37\2\2\u00d6%\3\2\2\2\u00d7\u00d9\7\30")
        buf.write("\2\2\u00d8\u00da\5H%\2\u00d9\u00d8\3\2\2\2\u00d9\u00da")
        buf.write("\3\2\2\2\u00da\'\3\2\2\2\u00db\u00dc\7+\2\2\u00dc\u00dd")
        buf.write("\7.\2\2\u00dd\u00de\5*\26\2\u00de\u00df\7/\2\2\u00df)")
        buf.write("\3\2\2\2\u00e0\u00e5\5H%\2\u00e1\u00e2\7\3\2\2\u00e2\u00e4")
        buf.write("\5H%\2\u00e3\u00e1\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00ea\3\2\2\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e8\u00ea\3\2\2\2\u00e9\u00e0\3\2\2\2")
        buf.write("\u00e9\u00e8\3\2\2\2\u00ea+\3\2\2\2\u00eb\u00ec\7#\2\2")
        buf.write("\u00ec\u00ed\5l\67\2\u00ed\u00ee\5.\30\2\u00ee\u00ef\7")
        buf.write("$\2\2\u00ef\u00f0\5n8\2\u00f0-\3\2\2\2\u00f1\u00f3\5\16")
        buf.write("\b\2\u00f2\u00f1\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2")
        buf.write("\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5/\3\2\2\2\u00f6\u00f4")
        buf.write("\3\2\2\2\u00f7\u00f8\5\62\32\2\u00f8\u00f9\5l\67\2\u00f9")
        buf.write("\u0101\3\2\2\2\u00fa\u00fb\5\64\33\2\u00fb\u00fc\5l\67")
        buf.write("\2\u00fc\u0101\3\2\2\2\u00fd\u00fe\5:\36\2\u00fe\u00ff")
        buf.write("\5l\67\2\u00ff\u0101\3\2\2\2\u0100\u00f7\3\2\2\2\u0100")
        buf.write("\u00fa\3\2\2\2\u0100\u00fd\3\2\2\2\u0101\61\3\2\2\2\u0102")
        buf.write("\u0103\5@!\2\u0103\u0104\5<\37\2\u0104\63\3\2\2\2\u0105")
        buf.write("\u0108\5\66\34\2\u0106\u0108\58\35\2\u0107\u0105\3\2\2")
        buf.write("\2\u0107\u0106\3\2\2\2\u0108\65\3\2\2\2\u0109\u010a\7")
        buf.write("\31\2\2\u010a\u010b\7+\2\2\u010b\u010c\5> \2\u010c\67")
        buf.write("\3\2\2\2\u010d\u010e\7\32\2\2\u010e\u0110\7+\2\2\u010f")
        buf.write("\u0111\5> \2\u0110\u010f\3\2\2\2\u0110\u0111\3\2\2\2\u0111")
        buf.write("9\3\2\2\2\u0112\u0113\5@!\2\u0113\u0114\7+\2\2\u0114\u0115")
        buf.write("\7\60\2\2\u0115\u0116\5h\65\2\u0116\u0118\7\61\2\2\u0117")
        buf.write("\u0119\5> \2\u0118\u0117\3\2\2\2\u0118\u0119\3\2\2\2\u0119")
        buf.write(";\3\2\2\2\u011a\u011c\7+\2\2\u011b\u011d\5> \2\u011c\u011b")
        buf.write("\3\2\2\2\u011c\u011d\3\2\2\2\u011d=\3\2\2\2\u011e\u011f")
        buf.write("\7\f\2\2\u011f\u0120\5H%\2\u0120?\3\2\2\2\u0121\u0122")
        buf.write("\t\2\2\2\u0122A\3\2\2\2\u0123\u0126\5D#\2\u0124\u0126")
        buf.write("\5F$\2\u0125\u0123\3\2\2\2\u0125\u0124\3\2\2\2\u0126C")
        buf.write("\3\2\2\2\u0127\u0128\5@!\2\u0128\u0129\7+\2\2\u0129E\3")
        buf.write("\2\2\2\u012a\u012b\5@!\2\u012b\u012c\5d\63\2\u012cG\3")
        buf.write("\2\2\2\u012d\u012e\5J&\2\u012e\u012f\7\22\2\2\u012f\u0130")
        buf.write("\5J&\2\u0130\u0133\3\2\2\2\u0131\u0133\5J&\2\u0132\u012d")
        buf.write("\3\2\2\2\u0132\u0131\3\2\2\2\u0133I\3\2\2\2\u0134\u0135")
        buf.write("\5L\'\2\u0135\u0136\t\3\2\2\u0136\u0137\5L\'\2\u0137\u013a")
        buf.write("\3\2\2\2\u0138\u013a\5L\'\2\u0139\u0134\3\2\2\2\u0139")
        buf.write("\u0138\3\2\2\2\u013aK\3\2\2\2\u013b\u013c\b\'\1\2\u013c")
        buf.write("\u013d\5N(\2\u013d\u0143\3\2\2\2\u013e\u013f\f\4\2\2\u013f")
        buf.write("\u0140\t\4\2\2\u0140\u0142\5N(\2\u0141\u013e\3\2\2\2\u0142")
        buf.write("\u0145\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2")
        buf.write("\u0144M\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0147\b(\1\2")
        buf.write("\u0147\u0148\5P)\2\u0148\u014e\3\2\2\2\u0149\u014a\f\4")
        buf.write("\2\2\u014a\u014b\t\5\2\2\u014b\u014d\5P)\2\u014c\u0149")
        buf.write("\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014fO\3\2\2\2\u0150\u014e\3\2\2\2\u0151")
        buf.write("\u0152\b)\1\2\u0152\u0153\5R*\2\u0153\u0159\3\2\2\2\u0154")
        buf.write("\u0155\f\4\2\2\u0155\u0156\t\6\2\2\u0156\u0158\5R*\2\u0157")
        buf.write("\u0154\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2")
        buf.write("\u0159\u015a\3\2\2\2\u015aQ\3\2\2\2\u015b\u0159\3\2\2")
        buf.write("\2\u015c\u015d\7%\2\2\u015d\u0160\5R*\2\u015e\u0160\5")
        buf.write("T+\2\u015f\u015c\3\2\2\2\u015f\u015e\3\2\2\2\u0160S\3")
        buf.write("\2\2\2\u0161\u0162\7\7\2\2\u0162\u0165\5T+\2\u0163\u0165")
        buf.write("\5V,\2\u0164\u0161\3\2\2\2\u0164\u0163\3\2\2\2\u0165U")
        buf.write("\3\2\2\2\u0166\u0167\7.\2\2\u0167\u0168\5H%\2\u0168\u0169")
        buf.write("\7/\2\2\u0169\u016c\3\2\2\2\u016a\u016c\5^\60\2\u016b")
        buf.write("\u0166\3\2\2\2\u016b\u016a\3\2\2\2\u016cW\3\2\2\2\u016d")
        buf.write("\u016e\5\\/\2\u016e\u016f\7\60\2\2\u016f\u0170\5Z.\2\u0170")
        buf.write("\u0171\7\61\2\2\u0171Y\3\2\2\2\u0172\u0177\5H%\2\u0173")
        buf.write("\u0174\7\3\2\2\u0174\u0176\5H%\2\u0175\u0173\3\2\2\2\u0176")
        buf.write("\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178[\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u017d\7+\2\2")
        buf.write("\u017b\u017d\5b\62\2\u017c\u017a\3\2\2\2\u017c\u017b\3")
        buf.write("\2\2\2\u017d]\3\2\2\2\u017e\u0181\5`\61\2\u017f\u0181")
        buf.write("\5b\62\2\u0180\u017e\3\2\2\2\u0180\u017f\3\2\2\2\u0181")
        buf.write("_\3\2\2\2\u0182\u0189\7(\2\2\u0183\u0189\7+\2\2\u0184")
        buf.write("\u0189\7,\2\2\u0185\u0189\7-\2\2\u0186\u0189\5f\64\2\u0187")
        buf.write("\u0189\5X-\2\u0188\u0182\3\2\2\2\u0188\u0183\3\2\2\2\u0188")
        buf.write("\u0184\3\2\2\2\u0188\u0185\3\2\2\2\u0188\u0186\3\2\2\2")
        buf.write("\u0188\u0187\3\2\2\2\u0189a\3\2\2\2\u018a\u018b\7+\2\2")
        buf.write("\u018b\u018c\7.\2\2\u018c\u018d\5*\26\2\u018d\u018e\7")
        buf.write("/\2\2\u018ec\3\2\2\2\u018f\u0190\7+\2\2\u0190\u0191\7")
        buf.write("\60\2\2\u0191\u0192\5h\65\2\u0192\u0193\7\61\2\2\u0193")
        buf.write("e\3\2\2\2\u0194\u0195\7\60\2\2\u0195\u0196\5j\66\2\u0196")
        buf.write("\u0197\7\61\2\2\u0197g\3\2\2\2\u0198\u019d\7,\2\2\u0199")
        buf.write("\u019a\7\3\2\2\u019a\u019c\7,\2\2\u019b\u0199\3\2\2\2")
        buf.write("\u019c\u019f\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3")
        buf.write("\2\2\2\u019ei\3\2\2\2\u019f\u019d\3\2\2\2\u01a0\u01a5")
        buf.write("\5H%\2\u01a1\u01a2\7\3\2\2\u01a2\u01a4\5H%\2\u01a3\u01a1")
        buf.write("\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5")
        buf.write("\u01a6\3\2\2\2\u01a6k\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8")
        buf.write("\u01aa\7\4\2\2\u01a9\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2")
        buf.write("\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01acm\3\2\2")
        buf.write("\2\u01ad\u01af\7\4\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b2")
        buf.write("\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1")
        buf.write("o\3\2\2\2\u01b2\u01b0\3\2\2\2&w{\u008b\u0092\u0096\u009e")
        buf.write("\u00a5\u00af\u00b5\u00b9\u00d9\u00e5\u00e9\u00f4\u0100")
        buf.write("\u0107\u0110\u0118\u011c\u0125\u0132\u0139\u0143\u014e")
        buf.write("\u0159\u015f\u0164\u016b\u0177\u017c\u0180\u0188\u019d")
        buf.write("\u01a5\u01ab\u01b0")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "<INVALID>", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'func'", 
                     "'number'", "'bool'", "'string'", "'return'", "'var'", 
                     "'dynamic'", "'for'", "'until'", "'by'", "'break'", 
                     "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
                     "'end'", "'not'", "'and'", "'or'", "<INVALID>", "'true'", 
                     "'false'", "<INVALID>", "<INVALID>", "<INVALID>", "'('", 
                     "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "CM", "NEWLINE", "COMMENT", "PLUS", "MINUS", 
                      "MUL", "DIV", "MOD", "EQUAL", "ASSIGN", "NOT_EQUAL", 
                      "SMALLER", "SMALLER_EQUAL", "LARGER", "LARGER_EQUAL", 
                      "THREE_DOT", "DOUBLE_EQUAL", "FUNCTION", "NUMBER", 
                      "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FOR", 
                      "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "BOOLEAN_LIT", 
                      "TRUE", "FALSE", "IDENTIFIER", "NUMBER_LIT", "STRING_LIT", 
                      "LRB", "RRB", "LSB", "RSB", "WS", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_manydeclare = 1
    RULE_declare = 2
    RULE_function_dec = 3
    RULE_body = 4
    RULE_comma_separate_param = 5
    RULE_statement = 6
    RULE_variable_dec_stmt = 7
    RULE_assign_stmt = 8
    RULE_lhs = 9
    RULE_if_stmt = 10
    RULE_if_part = 11
    RULE_elif_part = 12
    RULE_else_part = 13
    RULE_condition_action = 14
    RULE_for_stmt = 15
    RULE_break_stmt = 16
    RULE_continue_stmt = 17
    RULE_return_stmt = 18
    RULE_func_call_stmt = 19
    RULE_comma_separate_argument = 20
    RULE_block_stmt = 21
    RULE_list_statement_nullable = 22
    RULE_variable_dec = 23
    RULE_vardec_normal_type = 24
    RULE_vardec_implicit_type = 25
    RULE_var_type = 26
    RULE_dynamic_type = 27
    RULE_vardec_array_type = 28
    RULE_single_dec = 29
    RULE_value_init = 30
    RULE_variable_type = 31
    RULE_parameter = 32
    RULE_vardec_normal_param = 33
    RULE_vardec_array_param = 34
    RULE_expr = 35
    RULE_expr1 = 36
    RULE_expr2 = 37
    RULE_expr3 = 38
    RULE_expr4 = 39
    RULE_expr5 = 40
    RULE_expr6 = 41
    RULE_expr7 = 42
    RULE_element_expr = 43
    RULE_index_operators = 44
    RULE_expr_array_type = 45
    RULE_operand = 46
    RULE_variables = 47
    RULE_function_call = 48
    RULE_array_dec = 49
    RULE_array_value = 50
    RULE_comma_separate_number = 51
    RULE_comma_separate_expr = 52
    RULE_newline_separate = 53
    RULE_newline_separate_optional = 54

    ruleNames =  [ "program", "manydeclare", "declare", "function_dec", 
                   "body", "comma_separate_param", "statement", "variable_dec_stmt", 
                   "assign_stmt", "lhs", "if_stmt", "if_part", "elif_part", 
                   "else_part", "condition_action", "for_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "func_call_stmt", "comma_separate_argument", 
                   "block_stmt", "list_statement_nullable", "variable_dec", 
                   "vardec_normal_type", "vardec_implicit_type", "var_type", 
                   "dynamic_type", "vardec_array_type", "single_dec", "value_init", 
                   "variable_type", "parameter", "vardec_normal_param", 
                   "vardec_array_param", "expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "element_expr", "index_operators", 
                   "expr_array_type", "operand", "variables", "function_call", 
                   "array_dec", "array_value", "comma_separate_number", 
                   "comma_separate_expr", "newline_separate", "newline_separate_optional" ]

    EOF = Token.EOF
    CM=1
    NEWLINE=2
    COMMENT=3
    PLUS=4
    MINUS=5
    MUL=6
    DIV=7
    MOD=8
    EQUAL=9
    ASSIGN=10
    NOT_EQUAL=11
    SMALLER=12
    SMALLER_EQUAL=13
    LARGER=14
    LARGER_EQUAL=15
    THREE_DOT=16
    DOUBLE_EQUAL=17
    FUNCTION=18
    NUMBER=19
    BOOL=20
    STRING=21
    RETURN=22
    VAR=23
    DYNAMIC=24
    FOR=25
    UNTIL=26
    BY=27
    BREAK=28
    CONTINUE=29
    IF=30
    ELSE=31
    ELIF=32
    BEGIN=33
    END=34
    NOT=35
    AND=36
    OR=37
    BOOLEAN_LIT=38
    TRUE=39
    FALSE=40
    IDENTIFIER=41
    NUMBER_LIT=42
    STRING_LIT=43
    LRB=44
    RRB=45
    LSB=46
    RSB=47
    WS=48
    ILLEGAL_ESCAPE=49
    UNCLOSE_STRING=50
    ERROR_TOKEN=51

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
            self.state = 110
            self.manydeclare()
            self.state = 111
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

        def newline_separate_optional(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_separate_optionalContext,0)


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
            self.state = 113
            self.newline_separate_optional()
            self.state = 115 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 114
                self.declare()
                self.state = 117 
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
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.function_dec()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
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

        def body(self):
            return self.getTypedRuleContext(ZCodeParser.BodyContext,0)


        def newline_separate(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_separateContext,0)


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
            self.state = 123
            self.match(ZCodeParser.FUNCTION)
            self.state = 124
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 125
            self.match(ZCodeParser.LRB)
            self.state = 126
            self.comma_separate_param()
            self.state = 127
            self.match(ZCodeParser.RRB)
            self.state = 128
            self.body()
            self.state = 129
            self.newline_separate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_separate_optional(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_separate_optionalContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = ZCodeParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 131
                self.newline_separate_optional()
                self.state = 132
                self.return_stmt()

            elif la_ == 2:
                self.state = 134
                self.newline_separate_optional()
                self.state = 135
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

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ParameterContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ParameterContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.CM)
            else:
                return self.getToken(ZCodeParser.CM, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_comma_separate_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma_separate_param" ):
                return visitor.visitComma_separate_param(self)
            else:
                return visitor.visitChildren(self)




    def comma_separate_param(self):

        localctx = ZCodeParser.Comma_separate_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comma_separate_param)
        self._la = 0 # Token type
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.parameter()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.CM:
                    self.state = 140
                    self.match(ZCodeParser.CM)
                    self.state = 141
                    self.parameter()
                    self.state = 146
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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

        def newline_separate(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_separateContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_stmtContext,0)


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


        def variable_dec_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_dec_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


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
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 150
                    self.assign_stmt()
                    pass

                elif la_ == 2:
                    self.state = 151
                    self.break_stmt()
                    pass

                elif la_ == 3:
                    self.state = 152
                    self.continue_stmt()
                    pass

                elif la_ == 4:
                    self.state = 153
                    self.return_stmt()
                    pass

                elif la_ == 5:
                    self.state = 154
                    self.func_call_stmt()
                    pass

                elif la_ == 6:
                    self.state = 155
                    self.block_stmt()
                    pass


                self.state = 158
                self.newline_separate()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.variable_dec_stmt()
                pass
            elif token in [ZCodeParser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.if_stmt()
                pass
            elif token in [ZCodeParser.FOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.for_stmt()
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
            self.state = 165
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
            self.state = 167
            self.lhs()
            self.state = 168
            self.match(ZCodeParser.ASSIGN)
            self.state = 169
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def element_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Element_exprContext,0)


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
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.element_expr()
                pass


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
        self.enterRule(localctx, 20, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.if_part()
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 176
                    self.elif_part() 
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 182
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
        self.enterRule(localctx, 22, self.RULE_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(ZCodeParser.IF)
            self.state = 186
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
        self.enterRule(localctx, 24, self.RULE_elif_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(ZCodeParser.ELIF)
            self.state = 189
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

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = ZCodeParser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_else_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(ZCodeParser.ELSE)
            self.state = 192
            self.statement()
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

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


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
        self.enterRule(localctx, 28, self.RULE_condition_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(ZCodeParser.LRB)
            self.state = 195
            self.expr()
            self.state = 196
            self.match(ZCodeParser.RRB)
            self.state = 197
            self.newline_separate_optional()
            self.state = 198
            self.statement()
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

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
        self.enterRule(localctx, 30, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(ZCodeParser.FOR)
            self.state = 201
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 202
            self.match(ZCodeParser.UNTIL)
            self.state = 203
            self.expr()
            self.state = 204
            self.match(ZCodeParser.BY)
            self.state = 205
            self.expr()
            self.state = 206
            self.newline_separate_optional()
            self.state = 207
            self.statement()
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
        self.enterRule(localctx, 32, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
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
        self.enterRule(localctx, 34, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
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
        self.enterRule(localctx, 36, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(ZCodeParser.RETURN)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.BOOLEAN_LIT) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.LRB) | (1 << ZCodeParser.LSB))) != 0):
                self.state = 214
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LRB(self):
            return self.getToken(ZCodeParser.LRB, 0)

        def comma_separate_argument(self):
            return self.getTypedRuleContext(ZCodeParser.Comma_separate_argumentContext,0)


        def RRB(self):
            return self.getToken(ZCodeParser.RRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_stmt" ):
                return visitor.visitFunc_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def func_call_stmt(self):

        localctx = ZCodeParser.Func_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_func_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 218
            self.match(ZCodeParser.LRB)
            self.state = 219
            self.comma_separate_argument()
            self.state = 220
            self.match(ZCodeParser.RRB)
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.CM)
            else:
                return self.getToken(ZCodeParser.CM, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_comma_separate_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma_separate_argument" ):
                return visitor.visitComma_separate_argument(self)
            else:
                return visitor.visitChildren(self)




    def comma_separate_argument(self):

        localctx = ZCodeParser.Comma_separate_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_comma_separate_argument)
        self._la = 0 # Token type
        try:
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.BOOLEAN_LIT, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.LRB, ZCodeParser.LSB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.expr()
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.CM:
                    self.state = 223
                    self.match(ZCodeParser.CM)
                    self.state = 224
                    self.expr()
                    self.state = 229
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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

        def newline_separate(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_separateContext,0)


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
        self.enterRule(localctx, 42, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(ZCodeParser.BEGIN)
            self.state = 234
            self.newline_separate()
            self.state = 235
            self.list_statement_nullable()
            self.state = 236
            self.match(ZCodeParser.END)
            self.state = 237
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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_statement_nullable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement_nullable" ):
                return visitor.visitList_statement_nullable(self)
            else:
                return visitor.visitChildren(self)




    def list_statement_nullable(self):

        localctx = ZCodeParser.List_statement_nullableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list_statement_nullable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 239
                self.statement()
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def newline_separate(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_separateContext,0)


        def vardec_implicit_type(self):
            return self.getTypedRuleContext(ZCodeParser.Vardec_implicit_typeContext,0)


        def vardec_array_type(self):
            return self.getTypedRuleContext(ZCodeParser.Vardec_array_typeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_dec" ):
                return visitor.visitVariable_dec(self)
            else:
                return visitor.visitChildren(self)




    def variable_dec(self):

        localctx = ZCodeParser.Variable_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_variable_dec)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.vardec_normal_type()
                self.state = 246
                self.newline_separate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.vardec_implicit_type()
                self.state = 249
                self.newline_separate()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.vardec_array_type()
                self.state = 252
                self.newline_separate()
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

        def variable_type(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_typeContext,0)


        def single_dec(self):
            return self.getTypedRuleContext(ZCodeParser.Single_decContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardec_normal_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardec_normal_type" ):
                return visitor.visitVardec_normal_type(self)
            else:
                return visitor.visitChildren(self)




    def vardec_normal_type(self):

        localctx = ZCodeParser.Vardec_normal_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_vardec_normal_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.variable_type()
            self.state = 257
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
        self.enterRule(localctx, 50, self.RULE_vardec_implicit_type)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.var_type()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
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
        self.enterRule(localctx, 52, self.RULE_var_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(ZCodeParser.VAR)
            self.state = 264
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 265
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
        self.enterRule(localctx, 54, self.RULE_dynamic_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(ZCodeParser.DYNAMIC)
            self.state = 268
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 269
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

        def variable_type(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def comma_separate_number(self):
            return self.getTypedRuleContext(ZCodeParser.Comma_separate_numberContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

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
        self.enterRule(localctx, 56, self.RULE_vardec_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.variable_type()
            self.state = 273
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 274
            self.match(ZCodeParser.LSB)
            self.state = 275
            self.comma_separate_number()
            self.state = 276
            self.match(ZCodeParser.RSB)
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
        self.enterRule(localctx, 58, self.RULE_single_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 281
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
        self.enterRule(localctx, 60, self.RULE_value_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(ZCodeParser.ASSIGN)
            self.state = 285
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_type" ):
                return visitor.visitVariable_type(self)
            else:
                return visitor.visitChildren(self)




    def variable_type(self):

        localctx = ZCodeParser.Variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_variable_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self.enterRule(localctx, 64, self.RULE_parameter)
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.vardec_normal_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
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

        def variable_type(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vardec_normal_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardec_normal_param" ):
                return visitor.visitVardec_normal_param(self)
            else:
                return visitor.visitChildren(self)




    def vardec_normal_param(self):

        localctx = ZCodeParser.Vardec_normal_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_vardec_normal_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.variable_type()
            self.state = 294
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

        def variable_type(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_typeContext,0)


        def array_dec(self):
            return self.getTypedRuleContext(ZCodeParser.Array_decContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardec_array_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardec_array_param" ):
                return visitor.visitVardec_array_param(self)
            else:
                return visitor.visitChildren(self)




    def vardec_array_param(self):

        localctx = ZCodeParser.Vardec_array_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_vardec_array_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.variable_type()
            self.state = 297
            self.array_dec()
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
        self.enterRule(localctx, 70, self.RULE_expr)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.expr1()
                self.state = 300
                self.match(ZCodeParser.THREE_DOT)
                self.state = 301
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
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
        self.enterRule(localctx, 72, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.expr2(0)
                self.state = 307
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.SMALLER) | (1 << ZCodeParser.SMALLER_EQUAL) | (1 << ZCodeParser.LARGER) | (1 << ZCodeParser.LARGER_EQUAL) | (1 << ZCodeParser.DOUBLE_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 308
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 321
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 316
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 317
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 318
                    self.expr3(0) 
                self.state = 323
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 332
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 327
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 328
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 329
                    self.expr4(0) 
                self.state = 334
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 343
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 338
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 339
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 340
                    self.expr5() 
                self.state = 345
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_expr5)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(ZCodeParser.NOT)
                self.state = 347
                self.expr5()
                pass
            elif token in [ZCodeParser.MINUS, ZCodeParser.BOOLEAN_LIT, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.LRB, ZCodeParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
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
        self.enterRule(localctx, 82, self.RULE_expr6)
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.match(ZCodeParser.MINUS)
                self.state = 352
                self.expr6()
                pass
            elif token in [ZCodeParser.BOOLEAN_LIT, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.LRB, ZCodeParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
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
        self.enterRule(localctx, 84, self.RULE_expr7)
        try:
            self.state = 361
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LRB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(ZCodeParser.LRB)
                self.state = 357
                self.expr()
                self.state = 358
                self.match(ZCodeParser.RRB)
                pass
            elif token in [ZCodeParser.BOOLEAN_LIT, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
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
        self.enterRule(localctx, 86, self.RULE_element_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.expr_array_type()
            self.state = 364
            self.match(ZCodeParser.LSB)
            self.state = 365
            self.index_operators()
            self.state = 366
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.CM)
            else:
                return self.getToken(ZCodeParser.CM, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_index_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.expr()
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.CM:
                self.state = 369
                self.match(ZCodeParser.CM)
                self.state = 370
                self.expr()
                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 90, self.RULE_expr_array_type)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
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
        self.enterRule(localctx, 92, self.RULE_operand)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.variables()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
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

        def BOOLEAN_LIT(self):
            return self.getToken(ZCodeParser.BOOLEAN_LIT, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def array_value(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valueContext,0)


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
        self.enterRule(localctx, 94, self.RULE_variables)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.match(ZCodeParser.BOOLEAN_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                self.match(ZCodeParser.NUMBER_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 387
                self.match(ZCodeParser.STRING_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 388
                self.array_value()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 389
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
        self.enterRule(localctx, 96, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 393
            self.match(ZCodeParser.LRB)
            self.state = 394
            self.comma_separate_argument()
            self.state = 395
            self.match(ZCodeParser.RRB)
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
        self.enterRule(localctx, 98, self.RULE_array_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 398
            self.match(ZCodeParser.LSB)
            self.state = 399
            self.comma_separate_number()
            self.state = 400
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
        self.enterRule(localctx, 100, self.RULE_array_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(ZCodeParser.LSB)
            self.state = 403
            self.comma_separate_expr()
            self.state = 404
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

        def NUMBER_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NUMBER_LIT)
            else:
                return self.getToken(ZCodeParser.NUMBER_LIT, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.CM)
            else:
                return self.getToken(ZCodeParser.CM, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_comma_separate_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma_separate_number" ):
                return visitor.visitComma_separate_number(self)
            else:
                return visitor.visitChildren(self)




    def comma_separate_number(self):

        localctx = ZCodeParser.Comma_separate_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_comma_separate_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(ZCodeParser.NUMBER_LIT)
            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.CM:
                self.state = 407
                self.match(ZCodeParser.CM)
                self.state = 408
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 413
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.CM)
            else:
                return self.getToken(ZCodeParser.CM, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_comma_separate_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma_separate_expr" ):
                return visitor.visitComma_separate_expr(self)
            else:
                return visitor.visitChildren(self)




    def comma_separate_expr(self):

        localctx = ZCodeParser.Comma_separate_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_comma_separate_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.expr()
            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.CM:
                self.state = 415
                self.match(ZCodeParser.CM)
                self.state = 416
                self.expr()
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 106, self.RULE_newline_separate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 422
                self.match(ZCodeParser.NEWLINE)
                self.state = 425 
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
        self.enterRule(localctx, 108, self.RULE_newline_separate_optional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 427
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 432
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        self._predicates[37] = self.expr2_sempred
        self._predicates[38] = self.expr3_sempred
        self._predicates[39] = self.expr4_sempred
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
         




