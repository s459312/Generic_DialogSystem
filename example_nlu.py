import jsgf

book_grammar = jsgf.parse_grammar_file('grammar1.jsgf')
book_grammar


def get_dialog_act(rule):
    slots = []
    get_slots(rule.expansion, slots)
    return {'act': rule.grammar.name, 'slots': slots}

def get_slots(expansion, slots):
    if expansion.tag != '':
        slots.append((expansion.tag, expansion.current_match))
        return

    for child in expansion.children:
        get_slots(child, slots)

    if not expansion.children and isinstance(expansion, jsgf.NamedRuleRef):
        get_slots(expansion.referenced_rule.expansion, slots)

def nlu(utterance):
    matched = book_grammar.find_matching_rules(utterance)

    if matched:
        return get_dialog_act(matched[0])
    else:
        return {'act': 'null', 'slots': []}




utterance = 'chciałbym zarezerwować stolik na jutro na godzinę dwunastą trzydzieści na pięć osób'
matched = book_grammar.find_matching_rules(utterance)
matched

nlu('chciałbym zarezerwować stolik na jutro na godzinę dziesiątą dla trzech osób')

get_dialog_act(matched[0])