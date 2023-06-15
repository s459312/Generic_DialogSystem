import spacy

nlp = spacy.load("pl_core_news_md")

class DialogManager:
    def __init__(self, nlu_module, dst_module):
        self.nlu_module = nlu_module
        self.dst_module = dst_module

    def start_dialog(self):
        self.dst_module.update_state([])  # Zerowanie stanu dialogowego

        while True:
            user_input = input("Użytkownik: ")

            # Wykorzystanie modułu NLU do ekstrakcji aktywności i slotów
            acts = self.nlu_module.extract_acts_and_slots(user_input)

            # Aktualizacja stanu dialogowego za pomocą modułu DST
            self.dst_module.update_state(acts)
            dialog_state = self.dst_module.get_state()

            # Logika dialogu
            if not acts:
                response = "Przepraszam, nie rozumiem. Czym mogę Ci pomóc?"
            elif "hello" in acts[0].act_type:
                response = "Witaj! W czym mogę Ci pomóc?"
            elif "inform" in acts[0].act_type:
                response = self.generate_response(dialog_state)
            elif "bye" in acts[0].act_type:
                response = "Dziękuję za rozmowę. Miłego dnia!"
                break
            else:
                response = "Nie rozumiem. Czym mogę Ci pomóc?"

            print("Agent:", response)

    def generate_response(self, dialog_state):
        # Logika generowania odpowiedzi na podstawie stanu dialogowego
        # Możesz dostosować tę logikę do swoich potrzeb
        # Przykład: generowanie odpowiedzi na podstawie aktualnego stanu dialogowego
        response = "Rozumiem, potrzebujesz"

        if "product type" in dialog_state and "product" in dialog_state:
            product_type = dialog_state["product type"]
            product = dialog_state["product"]
            response += f" {product} z kategorii {product_type}"
        elif "product type" in dialog_state:
            product_type = dialog_state["product type"]
            response += f" produkty z kategorii {product_type}"
        else:
            response += " informacji o twoich potrzebach"

        response += ". Jak mogę Ci jeszcze pomóc?"

        return response

class DialogStateTracker:
    def __init__(self):
        self.dialog_state = {}

    def update_state(self, acts):
        for act in acts:
            if act.act_type == "hello":
                self.dialog_state = {}
            elif act.act_type == "bye":
                self.dialog_state = {}
            elif act.act_type == "inform":
                slots = act.slots
                for slot, value in slots.items():
                    self.dialog_state[slot] = value

    def get_state(self):
        return self.dialog_state
    




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

class NLU:
    def __init__(self):
        pass

    def extract_acts_and_slots(self, text):
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
                product_type, product = self.find_product_type(token.lemma_)
                if product_type and product:
                    act = DialogAct("inform", {"product type": product_type, "product": product})
                    acts.append(act)

        return acts

    def find_product_type(self, product):
        for product_type, products in product_type_rules.items():
            if product in products:
                return product_type, product

        return None, None

text = "Cześć, chciałbym kupić mleko, płatki oraz owoce"
nlu = NLU()
acts = nlu.extract_acts_and_slots(text)
for act in acts:
    print(f"Type: {act.act_type}")
    print(f"Slots: {act.slots}")
    print()


dst = DialogStateTracker()

text = "Cześć, chciałbym kupić mleko, płatki oraz owoce"
acts = nlu.extract_acts_and_slots(text)


dst.update_state(acts)


dialog_state = dst.get_state()

print("Dialog State:")
print(dialog_state)
dm = DialogManager(nlu ,dst)
dm.start_dialog()