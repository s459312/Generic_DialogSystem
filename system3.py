import spacy
import random

nlp = spacy.load("pl_core_news_md")

class DialogManager:
    def __init__(self, nlu_module, dst_module):
        self.nlu_module = nlu_module
        self.dst_module = dst_module

    def promotion(self):
        r = random.randint(1, 4)
        if r == 1:
            promotion = "Mamy dzisiaj w promocji ser!"
        elif r == 2:
            promotion = "Aktualnie w promocji mamy jabłka!"
        elif r == 2:
            promotion = "Mleko w super cenie! Tylko dzisiaj!"
        elif r == 2:
            promotion = "Chipsy na imprezę w promocji!"
        return promotion

    def start_dialog(self):
        self.dst_module.update_state([])  # Zerowanie stanu dialogowego

        i = 0

        while True:
            user_input = input("Użytkownik: ")

            # Wykorzystanie modułu NLU do ekstrakcji aktywności i slotów
            acts = self.nlu_module.extract_acts_and_slots(user_input)

            # Aktualizacja stanu dialogowego za pomocą modułu DST
            self.dst_module.update_state(acts)
            dialog_state = self.dst_module.get_state()

            # Logika dialogu
            if not acts:
                r = random.randint(1, 4)
                if r == 1:
                    response = "Przepraszam, nie rozumiem. W czym mogę Ci pomóc?"
                elif r == 2:
                    response = "Czy mógłbyś powtórzyć?"
                elif r == 3:
                    response = "Nie rozumiem. Mógłbyś powtórzyć?"
                elif r == 4:
                    response = "Nie umiem na to odpowiedzieć."
            elif "hello" in acts[0].act_type:
                r = random.randint(1, 4)
                if r == 1:
                    response = "Witaj! W czym mogę Ci pomóc?"
                elif r == 2:
                    response = "Dzień dobry! W czym mogę Ci pomóc?"
                elif r == 3:
                    response = "Witaj! W czym mogę służyć?"
                elif r == 4:
                    response = "Dzień dobry! Czego potrzebujesz?"
            elif "inform" in acts[0].act_type:
                response = self.generate_response(dialog_state)
            elif "bye" in acts[0].act_type:
                r = random.randint(1, 4)
                if r == 1:
                    response = "Dziękuję za rozmowę. Miłego dnia!"
                elif r == 2:
                    response = "Dziękuję. Miłego dnia!"
                elif r == 3:
                    response = "Miłego dnia i do zobaczenia!"
                elif r == 4:
                    response = "Dziękuję i do zobaczenia!"
                print("Agent:", response)
                break
            else:
                response = "Nie rozumiem. Czym mogę Ci pomóc?"

            print("Agent:", response)
            i += 1
            if i % 5 == 0:
                print("Agent:", self.promotion())

    def generate_response(self, dialog_state):
        # Logika generowania odpowiedzi na podstawie stanu dialogowego
        # Możesz dostosować tę logikę do swoich potrzeb
        # Przykład: generowanie odpowiedzi na podstawie aktualnego stanu dialogowego
        r = random.randint(1, 4)
        if r == 1:
            response = "Rozumiem, potrzebujesz"
        elif r == 2:
            response = "Znalazłem produkt"
        elif r == 3:
            response = "Posiadamy"
        elif r == 4:
            response = "Wybieram"

        if "product type" in dialog_state and "product" in dialog_state:
            product_type = dialog_state["product type"]
            product = dialog_state["product"]
            response += f" {product} z kategorii {product_type}"
        elif "product type" in dialog_state:
            product_type = dialog_state["product type"]
            response += f" produkty z kategorii {product_type}"
        else:
            response += " informacji o twoich potrzebach"

        r = random.randint(1, 4)
        if r == 1:
            response += ". Jak mogę Ci jeszcze pomóc?"
        elif r == 2:
            response += ". Co mogę jeszcze dla Ciebie zrobić?"
        elif r == 3:
            response += ". W czym mogę jeszcze pomóc?"
        elif r == 4:
            response += ". Czy potrzebujesz czegoś jeszcze?"

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
    "pieczywo": ["chleb", "bułka", "bulka",  "bułki", "bulki", "rogaliki", "rogalika", "bagietka", "bagietkę", "bagietke", "bagietki"],
    "owoce": ["jabłko", "jablko", "banana", "gruszkę", "gruszke", "pomarańczę","pomarancze"],
    "warzywa": ["marchewkę", "marchewke", "ziemniak", "cebulę", "cebule", "pomidory", "pomidora"],
    "mięso": ["kurczaka", "wołowinę", "wolowine", "wieprzowinę", "wieprzowine", "indyka"],
    "produkty mrożone": ["lody", "frytki", "pierogi", "nuggetsy"],
    "słodycze": ["czekoladę", "czekolade","czekolady", "ciastko", "lizaka", "gumę do żucia", "gume do zucia", "chipsy"],
    "przyprawy": ["sól", "sol", "pieprz", "oregano", "cynamon"],
    "napoje": ["wodę", "wode", "sok", "herbatę", "herbate", "kawę", "kawe", "energetyka"],
    "napoje alkoholowe": ["piwo", "wino", "wódkę","wodke", "whisky"],
    "higiena": ["pastę do zębów", "paste do zebow", "mydło", "mydlo", "szampon", "papier toaletowy"],
    "chemia gospodarcza": ["płyn do naczyń", "plyn do naczyn", "proszek do prania", "odświeżacz powietrza", "odswiezacz powietrza"],
    "inne": ["długopis", "baterie", "śrubokręt", "nożyczki"],
    "nabiał": ["mleko", "ser", "śmietanę","smietane"]
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
            if token.lower_ == "cześć" or token.lower_ == "witaj":
                acts.append(DialogAct("hello"))
            elif token.lower_ == "widzenia" or token.lower_ == "żegnaj":
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
                print(token.lemma_)
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

nlu = NLU()

dst = DialogStateTracker()

dm = DialogManager(nlu ,dst)
dm.start_dialog()