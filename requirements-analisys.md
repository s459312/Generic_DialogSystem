## Wymagania do systemu:

* rozpoczęcie zakupów,
* informowanie o promocjach/sugerowanie dostępnych promocji,
* finalizacja zakupów,
* anulowanie złożonego zamówienia,
* dodawanie i usuwanie przedmiotów do koszyka,
* proponowanie podobnych produktów (jeśli nie ma danego produktu w ofercie),
* obsługa bonów/karty rabatowej,
* zapisywanie listy zakupów na później,
* wczytywanie listy zakupów,
* zwrot produktu.

## Zadanie 1: Rozpoczęcie zakupów.

> **system:** Witamy w systemie zakupów sieci sklepów spożywczych *"Galaktyczny Skład"*, co chcesz dzisiaj zamówić? \
**user:** Chciałbym zamówić parówki z serem *"Jupiterki"*, makaron świderki, oraz czteropak piwa *"Galaktatra"*. \
**system:** Do koszyka zostały dodane: parówki z serem, makaron świderki oraz 4-pak piwa *"Tatra"*. Czy chcesz coś dodać jeszcze? ***W promocji mamy czipsy "Lejs" o smaku SURIMI***. \
**user:** To będzie wszystko. \
**system:** Dziękujemy, złożone zamówienie zostało przyjęte do realizacji.

## Zadanie 2: Informowanie o promocjach/sugerowanie dostępnych promocji.

> **user:** Dodaj do koszyka masło 82% *"Galaktyczna dolina"*. \
**system:** Do koszyka dodano: masło 82% *"Galaktyczna dolina"*. ***Obecnie mamy promocje 3+1 dla masła 82% "Galaktylos", czy chciałbyś/chciałabyś skorzystać z promocji?*** \
**user:** Ile bejmów na to wydam? \
**system:** ***Przy zakupie masła "Galaktylos" w promocji 3+1 zapłacisz 20 cebulionów! TANIO JAK W 2021 ROKU!*** Czy chcesz wymienić produkt masło 82% *"Galaktyczna dolina"* na masło *"Galaktylos"* w promocji 3+1? \
**user:** Nie. \
**system:** Dobrze, czy chcesz kupić coś jeszcze? \
**...**

## Zadanie 3: Finalizacja zakupów.

> **...** \
**user:** To będzie wszystko. \
**system:** Chcesz przejśc do płatności? \
**user:** Tak. \
**system:** Koszyk, zapisany, czy chcesz abym przeczytał wszystkie artykuły w koszyku? \
**user:** Nie. \
**system:** Suma płatności - 420 cebulionów już ze zniżką *"0 VAT"* od partii rządzącej! Chwała wielkiej partii! Czy posiadasz kartę klienta? \
**user:** Tak. \
**system:** Poprosze numer karty lub numer telefonu, jeśli był podany przy rejestracji. \
**user:** 420-213-769. \
**system:** Dodatkowe zniżki zostały naliczone. Suma zniżek: 0 cebulionów. Suma płatności ze zniżkami - 420 cebulionów. Czy chcesz zakończyć zakupy? \
**user:** Tak. \
**system:** Dobrze, zamówienie zostało przyjęte ro realizacji, z twojego konta zostanie pobrane 420 cebulionów. \
**system(optional):** Łaczenie z bankiem. \
**system(optional):** Autoryzacja płatności. \
**system:** Zakupy zostały opłacone, dziękujemy za korzystanie z usług sklepu *"Galaktyczny Skład"*.

## Zadanie 4: Anulowanie złożonego zamówienia.

> **user:** Chciałbym anulować ostatnie zamówienie. \
**system:** Podaj numer karty klienta lub numer telefonu. \
**user:** 420-213-769. \
**system:** Chcesz anulować zamówienie numer 1, 2 czy 3. \
**user:** Zamówienie numer 2. \
**system:** Czy potwierdzasz anulowanie zamówienia numer 2? \
**user:** Tak, anuluj zamówienie. \
**system:** Zamówienie anulowano. \
 \
***lub*** \
 \
**system:** Chcesz anulować zamówienie numer 1, 2 czy 3? \
**user:** Zamówienie numer 1. \
**system:** Zamówienie numer 1 jest już w realizacji. Za anulowanie tego zamówienia nie otrzymasz zwrotu gotówki. Czy potwierdzasz anulowanie zamówienia numer 1? \
**user:** Nie. \
**system:** Zamówienie nie zostało anulowane. Czy coś jeszcze mogę dla Ciebie zrobić?

## Zadanie 5: Dodawanie przedmiotów do koszyka oraz ich usuwanie.

> **user:** Prosze dodać parówki *"Jupiterki"*. \
**system:** Parówki *"Jupiterki"*: Classic" zostały dodane do twojego koszyka. Kontynuować? \
**user:** Dodaj do tego wódkę *"Marsówka"*. \
**system:** Wódka *"Marsówka"* została dodana to twojego koszyka. \
**user:** Co mam w koszyku? \
**system:** Zawartość koszyka:
* napój gazowany *"Cosmic Coke"*,
* awokado,
* zamrożona pizza *"Hawajska: Dla wszyskich"* marki *"Kosmiczna Flota"*,
* ciasto w kostce *"Czarna dziura"*,
* parówki *"Jupiterki: Classic"*,
* wódka *"Marsówka"*.
> **user:** Proszę usunąć awokado. \
**system:** Awokado zostało usunięte. \
**user:** A może nie, niech awokado zostanie. \
**system:** Awokado zostało przywrócone do twojego koszyka. Chcesz kontynuować zakupy? \
**user:** Nie. \
**system:** Chcesz przejść do płatności? \
**user:** Tak. \
**system:** Suma zakupów łącznie wyniesie 2137 cebulionów. \
**user:** Proszę jednak usunąć awokado. \
**system:** Wracam do trybu edycji koszyka. Awokado zostało usunięte. Czy chcesz kontynuować zakupy? \
**user:** Nie, chcę zapłacić. \
**system:** Suma zakupów łącznie wyniesie 69 cebulionów. \
**...**

## Zadanie 6: Proponowanie podobnych produktów w przypadku braku oczekiwanego.

> **user:** Proszę dodać do koszyka batonik *"Mars"*. \
**system:** Aktualnie batonik *"Mars"* jest niedostępny, proponuję batoniki: *"Bounty"*, *"Twix"*, *"Lion"*. \
**user:** Dobrze, poproszę *"Lion"*. \
**system:** Batonik *"Lion"* został dodany do koszyka. \
**...** 

## Zadanie 7: Obsługa bonów/karty rabatowej.

> **system:** Czy posiadasz bon lub kartę rabatową? \
**user:** Tak. \
**system:** Proszę o podanie numeru bonu lub karty. \
**user:** JB21C3C7. \
**system:** Dziękuję. Twój rabat został naliczony. \
**...** \
 \
***lub*** \
 \
**system:** Czy posiadasz bon lub kartę rabatową? \
**user:** Nie. \
**...**

## Zadanie 8: Zapisywanie listy zakupów na później/wczytywanie listy zakupów.

> **user:** Prosze dodać parówki *"Jupiterki"*. \
**system:** Parówki *"Jupiterki: Classic"* zostały dodane do twojego koszyka. Kontynuować? \
**user:** Dodaj do tego wódkę *"Marsówka"*. \
**system:** Wódka *"Marsówka"* została dodana to twojego koszyka. \
**user:** Co mam w koszyku? \
**system:** Zawartość koszyka: 
* napój gazowany *"Cosmic Coke"*,
* awokado,
* zamrożona pizza *"Hawajska: Dla wszyskich"* marki *"Kosmiczna Flota"*,
* ciasto w kostce *"Czarna dziura"*,
* parówki *"Jupiterki: Classic"*,
* wódka *"Marsówka"*.
> **user:** Proszę usunąć awokado. \
**system:** Awokado zostało usunięte. \
**user:** A może nie, niech awokado zostanie. \
**system:** Awokado zostało przywrócone do twojego koszyka. Chcesz kontynuować zakupy? \
**user:** Nie. \
**system:** Chcesz przejść do płatności? \
**user:** Nie. zapisz mój koszyk. \
**system:** Do konta o numerze 420-213-769 zapisuje zawartość koszyka z numerem 5: 
* napój gazowany *"Cosmic Coke"*,
* awokado,
* zamrożona pizza *"Hawajska: Dla wszyskich"* marki *"Kosmiczna Flota"*,
* ciasto w kostce *"Czarna dziura"*,
* parówki *"Jupiterki: Classic"*,
* wódka *"Marsówka"*.
> **user:** To pa. \
**...** \
**user:** Chce zreazlizować zapisany koszyk. \
**system:** Podaj numer konta lub numer telefonu. \
**user:** 420-213-769. \
**system:** Dla tego konta mam zapisane trzy koszyki: 5, 7, 11. który koszyk chcesz zrealizować? \
**user:** Ten z avokado. \
**system:** Avokado znajduje się w 5 i 11 koszyku. Który koszyk chcesz zrealizować? \
**user:** Co znajduje się w koszyku 5? \
**system:** 
* napój gazowany *"Cosmic Coke"*,
* awokado,
* zamrożona pizza *"Hawajska: Dla wszyskich"* marki *"Kosmiczna Flota"*,
* ciasto w kostce *"Czarna dziura"*,
* parówki *"Jupiterki: Classic"*,
* wódka *"Marsówka"*.
> **user:** Chce zrealizować ten koszyk. \
**system:** Przechodzę do płatności za koszyk numer 5. \
**...**

## Zadanie 9: Zwrot produktu.

> **user:** Dzień dobry, ser *"Gouda"*, który niedawno zakupiłem u Państwa w sklepie okazał się spleśniały. \
**system:** Dzień dobry, w takiej sytuacji możliwy jest zwrot pieniędzy lub wybór innego produktu w podobnej cenie. \
**user:** Dobrze, poproszę o wymiane produktu na ser *"Cheddar"* lub ser *"Edamski"*. \
**system:** Dostępne są oba sery, proszę o wybór jednego. \
**user:** Niech będzie ser *"Cheddar"*. \
**system:** Proszę o podanie numeru zamówienia (**optional:** oraz dowodu wadliwego produktu, który zostanie sprawdzony przez pracownika sklepu/innego bota). \
**user:** XYZ (**optional:** gouda.jpg). \
**...** \
**system:** Reklamacja została przyjęta. \
**...**







