# rules_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def fact1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'Television', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'Mean',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'Television', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'Toilet',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'Toilet', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'Happy',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact4(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'Toilet', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'Telephone',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact5(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'Telephone', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'Temperate',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact6(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'Telephone', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'Refrigerator',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact7(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'Refrigerator', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'Large',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact8(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'Refrigerator', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'PersonalComputer',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact9(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'PersonalComputer', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'Earthy',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact10(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'PersonalComputer', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'CompactDisc',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact11(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'CompactDisc', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'Blue',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact12(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'CompactDisc', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'DVD',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact13(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'DVD', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'Dull',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact14(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'DVD', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'GPS',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact15(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'AirConditioner', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'Dull',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact16(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'GPS', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'Sour',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fact17(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'GPS', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'IDCard',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  fc_rule.fc_rule('fact1', This_rule_base, fact1,
    (('facts', 'Television',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('fact2', This_rule_base, fact2,
    (('facts', 'Television',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('fact3', This_rule_base, fact3,
    (('facts', 'Toilet',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('fact4', This_rule_base, fact4,
    (('facts', 'Toilet',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('fact5', This_rule_base, fact5,
    (('facts', 'Telephone',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('fact6', This_rule_base, fact6,
    (('facts', 'Telephone',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('fact7', This_rule_base, fact7,
    (('facts', 'Refrigerator',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('fact8', This_rule_base, fact8,
    (('facts', 'Refrigerator',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('fact9', This_rule_base, fact9,
    (('facts', 'PersonalComputer',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('fact10', This_rule_base, fact10,
    (('facts', 'PersonalComputer',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('fact11', This_rule_base, fact11,
    (('facts', 'CompactDisc',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('fact12', This_rule_base, fact12,
    (('facts', 'CompactDisc',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('fact13', This_rule_base, fact13,
    (('facts', 'DVD',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(False),))
  
  fc_rule.fc_rule('fact14', This_rule_base, fact14,
    (('facts', 'DVD',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('fact15', This_rule_base, fact15,
    (('facts', 'AirConditioner',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('fact16', This_rule_base, fact16,
    (('facts', 'GPS',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(True),))
  
  fc_rule.fc_rule('fact17', This_rule_base, fact17,
    (('facts', 'GPS',
      (contexts.variable('x'),
       pattern.pattern_literal(True),),
      False),),
    (contexts.variable('x'),
     pattern.pattern_literal(True),))


Krb_filename = '..\\.cache_program\\rules.krb'
Krb_lineno_map = (
    ((12, 16), (3, 3)),
    ((17, 19), (5, 5)),
    ((28, 32), (9, 9)),
    ((33, 35), (11, 11)),
    ((44, 48), (15, 15)),
    ((49, 51), (17, 17)),
    ((60, 64), (21, 21)),
    ((65, 67), (23, 23)),
    ((76, 80), (27, 27)),
    ((81, 83), (29, 29)),
    ((92, 96), (33, 33)),
    ((97, 99), (35, 35)),
    ((108, 112), (39, 39)),
    ((113, 115), (41, 41)),
    ((124, 128), (45, 45)),
    ((129, 131), (47, 47)),
    ((140, 144), (51, 51)),
    ((145, 147), (53, 53)),
    ((156, 160), (57, 57)),
    ((161, 163), (59, 59)),
    ((172, 176), (63, 63)),
    ((177, 179), (65, 65)),
    ((188, 192), (69, 69)),
    ((193, 195), (71, 71)),
    ((204, 208), (75, 75)),
    ((209, 211), (77, 77)),
    ((220, 224), (81, 81)),
    ((225, 227), (83, 83)),
    ((236, 240), (87, 87)),
    ((241, 243), (89, 89)),
    ((252, 256), (93, 93)),
    ((257, 259), (95, 95)),
    ((268, 272), (99, 99)),
    ((273, 275), (101, 101)),
)
