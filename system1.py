
class NaturalLanguageUnderstanding:
    def __init__(self):
        pass

    def understand(self, text):
        user_act = {}
        user_act["type"] = []

        if any(substring in text.lower() for substring in ("cześć", "witaj", "siema", "elo", "hej", "czesc", "czesć", "cześc")):
            user_act["type"].append("hello()")
        if any(substring in text.lower() for substring in ("jak sie nazywasz",
                                                             "jak się nazywasz",
                                                             "jak masz na imie",
                                                             "jak masz na imię")):
            user_act["type"].append("request(name)")
        if text.lower() in ("rock and stone!", "rock and stone to the bone!", "by the beard!", "for karl!", "if you don't rock and stone, you ain't coming home!", "rock and stone yeeaaah!", "rock and stone - it never gets old!", "stone!"):
            user_act["type"].append("inform(rock_n_stone = True)")
        if not user_act["type"]:
            user_act["type"].append("null()")

        return user_act


class DialogueStateTracker:
    def __init__(self):
        self.state = "unknown"

    def update(self, user_act):
        if any(item == "hello()" in user_act["type"] for item in user_act["type"]):
            self.state = "say_hello"
        if any(item == "request(name)" in user_act["type"] for item in user_act["type"]):
            self.state = "told_name"
        if any(item == "inform(rock_n_stone = True)" in user_act["type"] for item in user_act["type"]):
            self.state = "rock_n_stone"
        if any(item == "null()" in user_act["type"] for item in user_act["type"]):
            self.state = "unknown"
        
        return self.state
        


class DialoguePolicy:
    def __init__(self):
        pass

    def respond(self, state):

        sys_act = {}
        sys_act["type"] = []


        if state == "say_hello":
            sys_act["type"].append("welcomemsg()")
        if state == "told_name":
            sys_act["type"].append("inform(name = NAME)")
        if state == "rock_n_stone":
            sys_act["type"].append("inform(rock_n_stone = True)")          
        if not sys_act["type"]:
            sys_act["type"].append("canthear()")
        
        return sys_act


class NaturalLanguageGeneration:
    def generate(self, sys_act):
        if any(item == "welcomemsg()" in sys_act["type"] for item in sys_act["type"]):
            return "Cześć."
        elif any(item == "inform(name = NAME)" in sys_act["type"] for item in sys_act["type"]):
            return "Cześć, mam na imię Ropuchomor."
        elif any(item == "inform(rock_n_stone = True)" in sys_act["type"] for item in sys_act["type"]):
            return "Rock and Stone!"
        else:
            return "Przepraszam ale nie rozumiem."


nlu = NaturalLanguageUnderstanding()
dst = DialogueStateTracker()
dpol = DialoguePolicy()
nlg = NaturalLanguageGeneration()

while True:
    user_utterance = input("User: ")
    user_act = nlu.understand(user_utterance)
    dialog_state = dst.update(user_act)
    sys_act = dpol.respond(dialog_state)
    sys_utterance = nlg.generate(sys_act)
    print("System: " + sys_utterance)