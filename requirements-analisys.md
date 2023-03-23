


Wymagania do systemu:
*rozpoczęcie zakupów
*informowanie o promocjach/sugerowanie dostępnych promocji
*finalizacja zakupów
*anulowanie złożonego zamówienia
*dodawanie & usuwanie przedmiotów do koszyka
*proponowanie podobnych produktów (jeśli nie ma danego produktu w ofercie)
*obsługa bonów/karty rabatowej
*zapisywanie listy zakupów na później
*wczytywanie listy zakupów
*zwrot produktu



Zadanie 1: rozpoczęcie zakupów

system: Witamy w systemie zakupów sieci sklepów spożywczych "Galaktyczny Skład", co chcesz dzisiaj zamówić?
user: chciałbym zamówić parówki z serem "Jupiterki", makaron świderki, oraz czteropak piwa "Galaktatra"
system: do koszyka zostały dodane: parówki z serem, makaron świderki oraz 4-pak piwa "Tatra". Czy chcesz coś dodać jeszcze? *W promocji mamy czipsy Lejs o smaku SURIMI* 
user: to będzie wszystko
system: Dziękujemy, złożone zamówienie zostało przyjęte do realizacji. 

Zadanie 2: informowanie o promocjach/sugerowanie dostępnych promocji

user: dodaj do koszyka masło 82% "Galaktyczna dolina"
system: do koszyka dodano: masło 82% "Galaktyczna dolina. *Obecnie mamy promocje 3+1 dla masła 82% "Galaktylos", czy chciałbyś/chciałabyś skorzystać z promocji?*
user: ile bejmów na to wydam?
system: *przy zakupie masła "Galaktylos" w promocji 3+1 zapłacisz 20 cebulionów! TANIO JAK W 2021 ROKU!* Czy chcesz wymienić produkt masło 82% "Galaktyczna dolina" na masło "Galaktylos" w promocji 3+1?
user: nie
system: dobrze, czy chcesz kupić coś jeszcze?
...

Zadanie 3: finalizacja zakupów

...
user: to będzie wszystko
system: chcesz przejśc do płatności?
user: tak
system: koszyk, zapisany, czy chcesz abym przeczytał wszystkie artykuły w koszyku?
user: nie
system: suma płatności - 420 cebulionów już ze zniżką "0 VAT" od partii rządzącej! Chwała wielkiej partii!
Czy posiadasz kartę klienta?
user: tak 
system: poprosze numer karty lub numer telefonu, jeśli był podany przy rejestracji
user: 420-213-769
system: dodatkowe zniżki zostały naliczone. Suma zniżek: 0 cebulionów. Suma płatności ze zniżkami - 420 cebulionów. Czy chcesz zakończyć zakupy?
user: tak
system: Dobrze, zamówienie zostało przyjęte ro realizacji, z twojego konta zostanie pobrane 420 cebulionów
system(optional): Łaczenie z bankiem
system(optional): Autoryzacja płatności
system: zakupy zostały opłacone, dziekujemy za korzystanie z usług sklepu "Galaktyczny Skład"


Zadanie 4: Anulowanie złożonego zamówienia
user: chciałbym anulować ostatnie zamówienie
system: podaj numer karty klienta lub numer telefonu
user: 420-213-769
system: chcesz anulować zamówienie numer 1, 2 czy 3
user: zamówienie numer 2
system: czy potwierdzasz anulowanie zamównienia nr 2?
user: tak, anuluj zamówienie
system: zamówienie anulowano

lub:
system: chcesz anulować zamówienie numer 1, 2 czy 3
user: zamówienie numer 1
system: zamówienie numer 1 jest już w realizacji. Za anulowanie tego zamówienia nie otrzymasz zwrotu gotówki. Czy potwierdzasz anulowanie zamówienia numer 1?
user: nie
system: zamówienie nie zostało anulowane. Czy coś jeszcze mogę dla Ciebie zrobić?


Zadanie 5: Dodawanie przedmiotów do koszyka oraz ich usuwanie

user: prosze dodać parówki "Jupiterki"
system: parówki "Jupiterki: Classic" zostały dodane do twojego koszyka. Kontynuować?
user: dodaj do tego wódkę "Marsówka"
system: wódka "Marsówka" została dodana to twojego koszyka
user: co mam w koszyku
system: zawartość koszyka:
        - napój gazowany "Cosmic Coke"
        - awokado
        - zamrożona pizza "Hawajska: Dla wszyskich" marki "Kosmiczna Flota"
        - ciasto w kostce "Czarna dziura"
        - parówki "Jupiterki: Classic"
        - wódka "Marsówka"

user: proszę usunąć awokado
system: awokado zostało usunięte
user: a może nie, niech awokado zostanie
system: awokado zostało przywrócone do twojego koszyka. Chcesz kontynuować zakupy?
user: nie
system: chcesz przejść do płatności?
user: tak
system: suma zakupów łącznie wyniesie 2137 cebulionów 
user: proszę jednak usunąć awokado
system: wracam do trybu edycji koszyka. Awokado zostało usunięte. Czy chcesz kontynuować zakupy?
user: nie, chcę zapłacić
system: suma zakupów łącznie wyniesie 69 cebulionów
....

Zadanie 6: Proponowanie podobnych produktów w przypadku braku oczekiwanego

user: proszę dodać do koszyka batonik "Mars"
system: Aktualnie batonik "Mars" jest niedostępny, proponuję batoniki: "Bounty", "Twix", "Lion"
user: dobrze, poproszę "Lion"
system: Batonik "Lion" został dodany do koszyka
.... 

Zadanie 7: obsługa bonów/karty rabatowej




Zadanie 8:zapisywanie listy zakupów na później/wczytywanie listy zakupów

user: prosze dodać parówki "Jupiterki"
system: parówki "Jupiterki: Classic" zostały dodane do twojego koszyka. Kontynuować?
user: dodaj do tego wódkę "Marsówka"
system: wódka "Marsówka" została dodana to twojego koszyka
user: co mam w koszyku
system: zawartość koszyka:
        - napój gazowany "Cosmic Coke"
        - awokado
        - zamrożona pizza "Hawajska: Dla wszyskich" marki "Kosmiczna Flota"
        - ciasto w kostce "Czarna dziura"
        - parówki "Jupiterki: Classic"
        - wódka "Marsówka"

user: proszę usunąć awokado
system: awokado zostało usunięte
user: a może nie, niech awokado zostanie
system: awokado zostało przywrócone do twojego koszyka. Chcesz kontynuować zakupy?
user: nie
system: chcesz przejść do płatności?
user: nie. zapisz mój koszyk
system: do konta o numerze 420-213-769 zapisuje zawartość koszyka z numerem 5:
        - napój gazowany "Cosmic Coke"
        - awokado
        - zamrożona pizza "Hawajska: Dla wszyskich" marki "Kosmiczna Flota"
        - ciasto w kostce "Czarna dziura"
        - parówki "Jupiterki: Classic"
        - wódka "Marsówka"
user: to pa
....
user: chce zreazlizować zapisany koszyk
system: podaj numer konta lub numer telefonu
user: 420-213-769
system: dla tego konta mam zapisane trzy koszyki: 5,7, 11. który koszyk chcesz zrealizować?
user: ten z avokado
system: avokado znajduje się w 5 i 11 koszyku. Który koszyk chcesz zrealizować?
user: co znajduje się w koszyku 5?
system: - napój gazowany "Cosmic Coke"
        - awokado
        - zamrożona pizza "Hawajska: Dla wszyskich" marki "Kosmiczna Flota"
        - ciasto w kostce "Czarna dziura"
        - parówki "Jupiterki: Classic"
        - wódka "Marsówka"
user: chce zrealizować ten koszyk
system: przechodzę do płatności za koszyk numer 5
...

Zadanie 9: Zwrot produktu 

user: dzień dobry, ser "Gouda", który niedawno zakupiłem u Państwa w sklepie okazał się spleśniały
system: Dzień dobry, w takiej sytuacji możliwy jest zwrot pieniędzy lub wybór innego produktu w podobnej cenie
user: dobrze, poproszę o wymiane produktu na ser "Cheddar" lub ser "Edamski"
system: Dostępne są oba sery, proszę o wybór jednego
user: niech będzie ser "Cheddar"
system: Proszę o podanie numeru zamówienia (optional: oraz dowodu wadliwego produktu, który zostanie sprawdzony przez pracownika sklepu/innego bota) 
user: XYZ (optional: gouda.jpg)
...
system: reklamacja została przyjęta
...







