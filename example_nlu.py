import jsgf
from pathlib import Path
import os

__location__ = Path().resolve()

book_grammar = jsgf.parse_grammar_file(os.path.join(__location__, "grammar3.jsgf"))
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


def predict(utterance):
    utterance = utterance.lower()
    punctuation = '''!;:/?,.*'''

    for i in utterance:
        if i in punctuation:
            utterance = utterance.replace(i, "")
        
        
    matched = book_grammar.find_matching_rules(utterance)
    nlu(utterance)

    try:
        print(get_dialog_act(matched[0]))
    except:
        pass

    return matched