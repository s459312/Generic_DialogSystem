import spacy

nlp = spacy.load("pl_core_news_md")

product_type_rules = {
    "pieczywo": ["chleb", "bułka", "rogalik", "bagietka"],
    "owoce": ["jabłko", "banan", "gruszka", "pomarańcza"],
    "warzywa": ["marchew", "ziemniak", "cebula", "pomidor"],
    "mięso": ["kurczak", "wołowina", "wieprzowina", "indyk"],
    "produkty mrożone": ["lody", "frytki", "pierogi mrożone", "nuggetsy"],
    "słodycze": ["czekolada", "ciastko", "lizak", "guma do żucia"],
    "przyprawy": ["sól", "pieprz", "oregano", "cynamon"],
    "napoje": ["woda", "sok", "herbata", "kawa"],
    "napoje alkoholowe": ["piwo", "wino", "wódka", "whisky"],
    "higiena": ["pasta do zębów", "mydło", "szampon", "papier toaletowy"],
    "chemia gospodarcza": ["płyn do naczyń", "proszek do prania", "odświeżacz powietrza"],
    "inne": ["długopis", "baterie", "śrubokręt", "nożyczki"],
    "nabiał": ["mleko"]
}

class DialogAct:
    def __init__(self, act_type, slots=None):
        self.act_type = act_type
        self.slots = slots if slots else {}

def extract_acts_and_slots(text):
    doc = nlp(text)
    acts = []

    for token in doc:
        if token.lower_ == "cześć":
            acts.append(DialogAct("hello"))
        elif token.lower_ == "do widzenia":
            acts.append(DialogAct("bye"))
        elif token.lower_ == "dziękuję":
            acts.append(DialogAct("thankyou"))
        elif token.lower_ == "proszę":
            acts.append(DialogAct("request"))
        elif token.lower_ == "powtórz":
            acts.append(DialogAct("repeat"))
        elif token.lower_ == "reset":
            acts.append(DialogAct("restart"))
        elif token.lower_ in ["tak", "oczywiście"]:
            acts.append(DialogAct("affirm"))
        elif token.lower_ in ["nie", "nie chcę"]:
            acts.append(DialogAct("deny"))
        elif token.pos_ == "NOUN":
            product_type, product = find_product_type(token.lemma_)
            if product_type and product:
                act = DialogAct("inform", {"product type": product_type, "product": product})
                acts.append(act)

    return acts

def find_product_type(product):
    for product_type, products in product_type_rules.items():
        if product in products:
            return product_type, product

    return None, None

text = "Cześć, chciałbym kupić mleko, sok oraz chleb"
acts = extract_acts_and_slots(text)
for act in acts:
    print(f"Type: {act.act_type}")
    print(f"Slots: {act.slots}")
    print()
