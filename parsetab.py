
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASIGNAR DIVIDIR ID LLAVED LLAVEI MULTI NUM PAREND PARENI RESTA SEMICOLON SUMAprogram : blockblock : LLAVEI statements LLAVEDstatements : statement statements\n                  | emptystatement : assign_statement\n                 | expression_statementassign_statement : ID ASIGNAR expression SEMICOLONexpression_statement : expression SEMICOLONexpression : expression SUMA term\n                  | expression RESTA term\n                  | termterm : term MULTI factor\n            | term DIVIDIR factor\n            | factorfactor : NUM\n              | ID\n              | PARENI expression PARENDempty :'
    
_lr_action_items = {'LLAVEI':([0,],[3,]),'$end':([1,2,15,],[0,-1,-2,]),'LLAVED':([3,4,5,6,7,8,16,18,31,],[-18,15,-18,-4,-5,-6,-3,-8,-7,]),'ID':([3,5,7,8,14,17,18,19,20,21,22,31,],[9,9,-5,-6,24,24,-8,24,24,24,24,-7,]),'NUM':([3,5,7,8,14,17,18,19,20,21,22,31,],[13,13,-5,-6,13,13,-8,13,13,13,13,-7,]),'PARENI':([3,5,7,8,14,17,18,19,20,21,22,31,],[14,14,-5,-6,14,14,-8,14,14,14,14,-7,]),'ASIGNAR':([9,],[17,]),'MULTI':([9,11,12,13,24,26,27,28,29,30,],[-16,21,-14,-15,-16,21,21,-12,-13,-17,]),'DIVIDIR':([9,11,12,13,24,26,27,28,29,30,],[-16,22,-14,-15,-16,22,22,-12,-13,-17,]),'SEMICOLON':([9,10,11,12,13,24,25,26,27,28,29,30,],[-16,18,-11,-14,-15,-16,31,-9,-10,-12,-13,-17,]),'SUMA':([9,10,11,12,13,23,24,25,26,27,28,29,30,],[-16,19,-11,-14,-15,19,-16,19,-9,-10,-12,-13,-17,]),'RESTA':([9,10,11,12,13,23,24,25,26,27,28,29,30,],[-16,20,-11,-14,-15,20,-16,20,-9,-10,-12,-13,-17,]),'PAREND':([11,12,13,23,24,26,27,28,29,30,],[-11,-14,-15,30,-16,-9,-10,-12,-13,-17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block':([0,],[2,]),'statements':([3,5,],[4,16,]),'statement':([3,5,],[5,5,]),'empty':([3,5,],[6,6,]),'assign_statement':([3,5,],[7,7,]),'expression_statement':([3,5,],[8,8,]),'expression':([3,5,14,17,],[10,10,23,25,]),'term':([3,5,14,17,19,20,],[11,11,11,11,26,27,]),'factor':([3,5,14,17,19,20,21,22,],[12,12,12,12,12,12,28,29,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> block','program',1,'p_program','main.py',43),
  ('block -> LLAVEI statements LLAVED','block',3,'p_block','main.py',47),
  ('statements -> statement statements','statements',2,'p_statements','main.py',51),
  ('statements -> empty','statements',1,'p_statements','main.py',52),
  ('statement -> assign_statement','statement',1,'p_statement','main.py',59),
  ('statement -> expression_statement','statement',1,'p_statement','main.py',60),
  ('assign_statement -> ID ASIGNAR expression SEMICOLON','assign_statement',4,'p_assign_statement','main.py',64),
  ('expression_statement -> expression SEMICOLON','expression_statement',2,'p_expression_statement','main.py',68),
  ('expression -> expression SUMA term','expression',3,'p_expression','main.py',72),
  ('expression -> expression RESTA term','expression',3,'p_expression','main.py',73),
  ('expression -> term','expression',1,'p_expression','main.py',74),
  ('term -> term MULTI factor','term',3,'p_term','main.py',84),
  ('term -> term DIVIDIR factor','term',3,'p_term','main.py',85),
  ('term -> factor','term',1,'p_term','main.py',86),
  ('factor -> NUM','factor',1,'p_factor','main.py',96),
  ('factor -> ID','factor',1,'p_factor','main.py',97),
  ('factor -> PARENI expression PAREND','factor',3,'p_factor','main.py',98),
  ('empty -> <empty>','empty',0,'p_empty','main.py',105),
]
