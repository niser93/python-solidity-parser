# Generated from solidity-antlr4/Solidity.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SolidityParser import SolidityParser
else:
    from SolidityParser import SolidityParser

# This class defines a complete listener for a parse tree produced by SolidityParser.
class SolidityListener(ParseTreeListener):

    # Enter a parse tree produced by SolidityParser#sourceUnit.
    def enterSourceUnit(self, ctx:SolidityParser.SourceUnitContext):
        pass

    # Exit a parse tree produced by SolidityParser#sourceUnit.
    def exitSourceUnit(self, ctx:SolidityParser.SourceUnitContext):
        pass


    # Enter a parse tree produced by SolidityParser#comment.
    def enterComment(self, ctx:SolidityParser.CommentContext):
        pass

    # Exit a parse tree produced by SolidityParser#comment.
    def exitComment(self, ctx:SolidityParser.CommentContext):
        pass



del SolidityParser