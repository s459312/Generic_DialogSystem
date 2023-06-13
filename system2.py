import json
import random
import jsgf
from pathlib import Path
import os
from collections import defaultdict
from convlab.policy.policy import Policy

__location__ = Path().resolve()

book_grammar = jsgf.parse_grammar_file(os.path.join(__location__, "grammar3.jsgf"))

class DST():
    def __init__(self):
        self.state = json.load(open('dictionary.json'))

    def update(self, user_act=None):
        for intent, domain, slot, value in user_act:
            domain = domain.lower()
            intent = intent.lower()
            slot = slot.lower()
            
            if domain not in self.state['belief_state']:
                continue

            if intent == 'inform':
                if slot == 'none' or slot == '':
                    continue

                domain_dic = self.state['belief_state'][domain]

                if slot in domain_dic:
                    self.state['belief_state'][domain][slot] = value

            elif intent == 'request':
                if domain not in self.state['request_state']:
                    self.state['request_state'][domain] = {}
                if slot not in self.state['request_state'][domain]:
                    self.state['request_state'][domain][slot] = 0
                    
        self.state['user_act'] = user_act
        return self.state
    
    def init_session(self):
        self.state = json.load(open('dictionary.json'))


class SimpleRulePolicy(Policy):
    def __init__(self):
        Policy.__init__(self)
        self.db = json.load(open('product_db.json'))

    def predict(self, state):
        self.results = []
        system_action = defaultdict(list)
        user_action = defaultdict(list)
        system_acts = []
        for intent, domain, slot, value in state['user_act']:
            user_action[(domain.lower(), intent.lower())].append((slot.lower(), value))
        for user_act in user_action:
            self.update_system_action(user_act, user_action, state, system_action)
        system_acts = [[intent, domain, slot, value] for (domain, intent), slots in system_action.items() for slot, value in slots]
        state['system_act'] = system_acts
        return system_acts

    def update_system_action(self, user_act, user_action, state, system_action):
        domain, intent = user_act
        constraints = [(slot, value) for slot, value in state['belief_state'][domain.lower()].items() if value != '']
        self.results = self.db['database'][domain]

        # Reguła 1
        if intent == 'request':
            if len(self.results) == 0:
                system_action[(domain, 'NoOffer')] = []
            else:
                for slot in user_action[user_act]:
                    if self.results and slot[0] in self.results[0]:
                        system_action[(domain, 'Inform')].append([slot[0], self.results[0].get(slot[0], 'unknown')])

        # Reguła 2
        elif intent == 'inform':
            if len(self.results) == 0:
                system_action[(domain, 'NoOffer')] = []
            else:
                system_action[(domain, 'Inform')].append(['Choice', str(len(self.results))])
                for product in self.results:
                    if all(product.get(slot, '').lower() == value.lower() for slot, value in constraints):
                        system_action[(domain, 'Recommend')].append(['Name', product['name']])
                        break


def nlg(system_act):
    domain, intent, slot, value = system_act

    if intent == 'Affirm':
        r = random.randint(1, 3)

        if r == 1:
            return 'Tak'
        elif r == 2:
            return 'Zgadza się'
        else:
            return 'Potwierdzam'
    
    if intent == 'Deny':
        r = random.randint(1, 3)

        if r == 1:
            return 'Nie'
        elif r == 2:
            return 'Nie zgadza się'
        else:
            return 'Nie potwierdzam'
        
    if intent == 'Canthelp':
        r = random.randint(1, 3)

        if r == 1:
            return 'Przepraszam, ale obawiam się, że nie mogę tego zrobić'
        elif r == 2:
            return 'Wystąpił błąd, proszę się skontaktować z obsługą'
        else:
            return 'ERR://23¤Y%/'
        
    if intent == 'Hellomsg':
        r = random.randint(1, 3)

        if r == 1:
            return 'Witaj'
        elif r == 2:
            return 'Cześć'
        else:
            return 'Dzień dobry'
        
    if intent == 'Bye':
        r = random.randint(1, 3)

        if r == 1:
            return 'Do zobaczenia'
        elif r == 2:
            return 'Żegnaj'
        else:
            return 'Buk zapłać'
        
    if domain == 'Product':
        if intent == 'Inform':
            if slot == 'Quantity':
                if value == 0:
                    return f'Nie znalazłem produktów spełniających podane kryteria.'
                elif value == 1:
                    return f'Znalazłem jeden produkt spełniający podane kryteria.'
                elif value <= 4:
                    return f'Znalazłem {value} produkty spełniające podane kryteria.'
                elif value <= 9:
                    return f'Znalazłem {value} produktów spełniających podane kryteria.'
                else:
                    return f'Znalazłem wiele produktów spełniających podane kryteria.'
            elif slot == 'Quality':
                return f'Znalazłem produkt(y) jakości {value}'
            elif slot == 'Price_range':
                return f'Znalazłem produkt(y) w przedziale cenowym {value}'
            elif slot == 'Type':
                return f'Znalazłem produkt(y) typu {value}'
            elif slot == 'Brand':
                return f'Znalazłem produkt(y) marki {value}'
            elif slot == 'Price':
                return f'Znalazlem produkt(y) w cenie {value}'
        if intent == 'Request':
            if slot == 'CreditCardNo':
                return 'Podaj nuber karty płatniczej'
            if slot == 'Quantity':
                return 'Podaj liczbę artykułów'
            if slot == 'Type':
                return 'Podaj typ produktu'
        if intent == 'Recommend':
            if slot == "Name":
                r = random.randint(1, 3)

                if r == 1:
                    return f'Kochany użytkowniku, z całego serduszka polecam Ci {value}'
                elif r == 2:
                    return f'Polecam {value}'
                else:
                    return f'Mogę polecić {value}'

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



dst = DST()
policy = SimpleRulePolicy()

utterance = input("Podaj wypowiedź użytkownika: ")

dialog_act = predict(utterance)
state = dst.update(dialog_act)
system_act = policy.predict(state)

for act in system_act:
    response = nlg(act)
    print("Odpowiedź systemu:", response)
