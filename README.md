# Uczenie maszynowe 2023

Witaj w swoim projekcie dla przedmiotu *Uczenie maszynowe*. Jest on przypisany do Twojej osoby. To tutaj powinnaś/powinieneś umieszczać efekty swojej pracy, czyli rozwiązania dla poszczególnych ćwiczeń laboratoryjnych.

Każdy *commit* na gałęzi `main` powoduje wyzwolenie *pipeline* [CI/CD](https://docs.gitlab.com/ee/ci/). Skrypt przejrzy zmodyfikowane pliki i uruchomi Twój program, pod dwoma warunkami:

* nie minął termin przekazywania rozwiązań – domyślnie jest to 1 tydzień od dnia, w którym odbyły się zajęcia laboratoryjne,
* nie została przekroczona określona w treści ćwiczenia liczba prób – możliwych sprawdzeń przekazanego zadania[^1].

Liczba prób określana jest poprzez zliczenie *commitów* dla danego pliku na gałęzi `main`. Dlatego zatwierdzaj *commit* na tej gałęzi tylko wtedy, gdy chcesz, aby Twój program został sprawdzony.

Proces sprawdzania możesz podejrzeć wybierając po lewej stronie opcję *CI/CD > Pipelines* i klikając odpowiednią pozycję, a następnie, w jej szczegółach, zaokrąglony przycisk odpowiedniego etapu (dla zadań laboratoryjnych będzie to jeden etap o nazwie `check`).

Wyniki sprawdzania zostaną dodane, w postaci pliku JSON, do katalogu z plikiem zadania. Nie usuwaj tych plików, ponieważ z nich pobierane są informacje służące do wyliczania oceny. Do oceny końcowej będą brane pod uwagę ostatnie wykonane próby danego zadania. 

W repozytorium znajdziesz też pliki z rozszerzeniem `.hmac`. Są to [kody uwierzytelniające](https://pl.wikipedia.org/wiki/HMAC), które potwierdzają autentyczność danego pliku. Ich również nie usuwaj.
