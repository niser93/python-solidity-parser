# Generated from solidity-antlr4/Solidity.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SolidityParser import SolidityParser
else:
    from SolidityParser import SolidityParser

# This class defines a complete generic visitor for a parse tree produced by SolidityParser.

class SolidityVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SolidityParser#sourceUnit.
    def visitSourceUnit(self, ctx:SolidityParser.SourceUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SolidityParser#comment.
    def visitComment(self, ctx:SolidityParser.CommentContext):
        return self.visitChildren(ctx)



del SolidityParser