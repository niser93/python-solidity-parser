# Generated from solidity-antlr4/Solidity.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("/\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\2\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\7\3\36\n\3\f\3\16\3!\13\3\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\6\6\6*\n\6\r\6\16\6+\3\6\3\6\3\23\2\7\3\3\5\4")
        buf.write("\7\2\t\5\13\6\3\2\4\4\2\f\f\17\17\5\2\13\f\16\17\"\"\2")
        buf.write("\60\2\3\3\2\2\2\2\5\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3")
        buf.write("\r\3\2\2\2\5\31\3\2\2\2\7\"\3\2\2\2\t$\3\2\2\2\13)\3\2")
        buf.write("\2\2\r\16\7\61\2\2\16\17\7,\2\2\17\23\3\2\2\2\20\22\5")
        buf.write("\7\4\2\21\20\3\2\2\2\22\25\3\2\2\2\23\24\3\2\2\2\23\21")
        buf.write("\3\2\2\2\24\26\3\2\2\2\25\23\3\2\2\2\26\27\7,\2\2\27\30")
        buf.write("\7\61\2\2\30\4\3\2\2\2\31\32\7\61\2\2\32\33\7\61\2\2\33")
        buf.write("\37\3\2\2\2\34\36\n\2\2\2\35\34\3\2\2\2\36!\3\2\2\2\37")
        buf.write("\35\3\2\2\2\37 \3\2\2\2 \6\3\2\2\2!\37\3\2\2\2\"#\13\2")
        buf.write("\2\2#\b\3\2\2\2$%\13\2\2\2%&\3\2\2\2&\'\b\5\2\2\'\n\3")
        buf.write("\2\2\2(*\t\3\2\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2\2")
        buf.write("\2,-\3\2\2\2-.\b\6\2\2.\f\3\2\2\2\6\2\23\37+\3\b\2\2")
        return buf.getvalue()


class SolidityLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    LINE_COMMENT = 2
    UNKNOWN = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "LINE_COMMENT", "UNKNOWN", "WS" ]

    ruleNames = [ "COMMENT", "LINE_COMMENT", "ANYCHAR", "UNKNOWN", "WS" ]

    grammarFileName = "Solidity.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


