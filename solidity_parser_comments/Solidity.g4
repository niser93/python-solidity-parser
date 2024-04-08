// Copyright 2020 Gonçalo Sá <goncalo.sa@consensys.net>
// Copyright 2016-2019 Federico Bond <federicobond@gmail.com>
// Licensed under the MIT license. See LICENSE file in the project root for details.

grammar Solidity;

sourceUnit
  : (comment)* EOF ;

comment : COMMENT | LINE_COMMENT;

COMMENT
    : '/*' ANYCHAR*? '*/'
    ;

LINE_COMMENT : '//' ~[\r\n]*;

fragment ANYCHAR : .;
UNKNOWN: . -> skip;

WS
  : [ \t\r\n\u000C]+ -> skip ;