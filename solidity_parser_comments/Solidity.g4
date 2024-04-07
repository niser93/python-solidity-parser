// Copyright 2020 Gonçalo Sá <goncalo.sa@consensys.net>
// Copyright 2016-2019 Federico Bond <federicobond@gmail.com>
// Licensed under the MIT license. See LICENSE file in the project root for details.

grammar Solidity;

sourceUnit
  : (comment | line_comment | CODE_LINE)* EOF ;

comment : COMMENT;
line_comment : LINE_COMMENT;

COMMENT
    : '/*' .*? '*/'
    ;

LINE_COMMENT
    : '//' ~[\r\n]*
    ;

CODE_LINE
    : ANYCHAR+ ~[\r\n]*
    ;

ANYCHAR : .;