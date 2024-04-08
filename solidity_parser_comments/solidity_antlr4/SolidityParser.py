# Generated from solidity-antlr4/Solidity.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("\21\4\2\t\2\4\3\t\3\3\2\7\2\b\n\2\f\2\16\2\13\13\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\2\2\4\2\4\2\3\3\2\3\4\2\17\2\t\3\2\2")
        buf.write("\2\4\16\3\2\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\13\3\2\2\2\t")
        buf.write("\7\3\2\2\2\t\n\3\2\2\2\n\f\3\2\2\2\13\t\3\2\2\2\f\r\7")
        buf.write("\2\2\3\r\3\3\2\2\2\16\17\t\2\2\2\17\5\3\2\2\2\3\t")
        return buf.getvalue()


class SolidityParser ( Parser ):

    grammarFileName = "Solidity.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "COMMENT", "LINE_COMMENT", "UNKNOWN", 
                      "WS" ]

    RULE_sourceUnit = 0
    RULE_comment = 1

    ruleNames =  [ "sourceUnit", "comment" ]

    EOF = Token.EOF
    COMMENT=1
    LINE_COMMENT=2
    UNKNOWN=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SourceUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SolidityParser.EOF, 0)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SolidityParser.CommentContext)
            else:
                return self.getTypedRuleContext(SolidityParser.CommentContext,i)


        def getRuleIndex(self):
            return SolidityParser.RULE_sourceUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceUnit" ):
                listener.enterSourceUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceUnit" ):
                listener.exitSourceUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSourceUnit" ):
                return visitor.visitSourceUnit(self)
            else:
                return visitor.visitChildren(self)




    def sourceUnit(self):

        localctx = SolidityParser.SourceUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sourceUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SolidityParser.COMMENT or _la==SolidityParser.LINE_COMMENT:
                self.state = 4
                self.comment()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(SolidityParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(SolidityParser.COMMENT, 0)

        def LINE_COMMENT(self):
            return self.getToken(SolidityParser.LINE_COMMENT, 0)

        def getRuleIndex(self):
            return SolidityParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = SolidityParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            _la = self._input.LA(1)
            if not(_la==SolidityParser.COMMENT or _la==SolidityParser.LINE_COMMENT):
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





