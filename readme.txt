Autor: Wojciech Wolny
nr indeksu: 283786
Politechnika Warszawska
Wydział Elektroniki i Technik Infromacyjnych

Temat Projektu: "Podobieństwo cząstkowe ciągów"
Porgram powinien liczyć długość najdłuższego wspólnego prefiksu dla dwóch ciągów złożonych z "a" i innych losowych liter z ASCII.
Program otrzymuje na wejście ciąg znaków S i oblicza sumę podobieństw ciągu S do jego sufiksów.

Tryby wykonywania:
1. Podobieństwo cząstkowe ciągów dla gotowego pliku wejściowego:
    python aal.py -m1 <name of the file>.txt
    Tryb: m1
    Parametry:
        nazwa pliku z rozszerzeniem ".txt"
    Dane wejściowe:
        Plik .txt powinien składać się z jednego ciągu złożonego wyłącznie z liter "a" i innych losowych liter z ASCII w każdej linii
    Dane wyjściowe:
        suma podobieństwa cząstkowego ciągów dla każdego ciągu znaków w poprawnie wprowadzonym pliku
2. Podobieństwo cząstkowe ciągów z generowaniem wartości wejściowej:
    python aal.py -m2 -n<length of generated word> -d<ratio of a's in a word>
    Tryb: m2
    Parametry:
        -n -docelowa długość generowanego słowa
        -d -stosunek ilości "a" w generowanym słowie do jego całej długości - parametr opcjonalny
        -a  -wielkość alfabetu z założeniem, że -a jest większe równe 1 i z nałożeniem funkcji min(-a, 52) - parametr opcjonalny
    Dane wyjściowe:
        Ciąg znaków o długości -n ze stosunkiem ilości "a" do długości ciągu -d.
3. Test podobieństwa cząstkowego ciągów
python aal.py -m3 -n<length of generated word> -k<number of problems> -step<number of steps> -r<how many instances of each problem>
    Tryb: m3
    Parametry:
        -n      -długość najmniejszego słowa
        -k      -liczba problemów
        -step   -wielkość o którą zwiększamy długość słowa w kolejnym problemie
        -r      -liczba instancji dla każdego problemu
        -a  -wielkość alfabetu z założeniem, że -a jest większe równe 1 i z nałożeniem funkcji min(-a, 52) - parametr opcjonalny
    Dane wyjściowe:
        Tabela z wynikami przeprowadzonego testu. W kolumnach odpowiednio podane informacje o długości słowa w pojedyńczym problemie, średnim czasie wykonywania dla -r instancji oraz współczynnikiem zgodności oceny teoretycznej z pomiarem czasu.
4. Test podobieństwa cząstkowego ciągów z porównanie dla dwóch algorytmów. O złożonościach kwadratowej i liniowej.
python aal.py -m4 -n<length of generated word> -k<number of problems> -step<number of steps> -r<how many instances of each problem>
    Tryb: m4
    Parametry:
        -n      -długość najmniejszego słowa
        -k      -liczba problemów
        -step   -wielkość o którą zwiększamy długość słowa w kolejnym problemie
        -r      -liczba instancji dla każdego problemu
        -a  -wielkość alfabetu z założeniem, że -a jest większe równe 1 i z nałożeniem funkcji min(-a, 52) - parametr opcjonalny
    Dane wyjściowe:
        Dane w formacie "csv" z nagłówkiem. Kolumny są odzielone przecinkiem, a rzędy znakiem nowej lini.
        Dane posiadją informację o wielkości słowa w problemie, średnim wynikiem pomiaru czasu, współczynnikiem zgodnościoceny teoretycznej i sumie wartości funkcji dla wszystkich jego instancji dla algorytmu o złożoności kwadratowej oraz dla algorytmu o złożoności liniowej.

Dodatkowa funkcja pomocnicza do generowania pseudolosowych ciągów S znajduje się w pliku gen.py:
python gen.py -n<length of generated word> -d<ratio of a's to the word>
    Tryb: Generuj
    Parametry:
        -n  -docelowa długość generowanego słowa
        -d  -stosunek ilości "a" w generowanym słowie do jego całej długości - parametr opcjonalny
        -a  -wielkość alfabetu z założeniem, że -a jest większe równe 1 i z nałożeniem funkcji min(-a, 52) - parametr opcjonalny
    Dane wyjściowe:
        Ciąg znaków "a" i innych losowych znaków z zbioru liter z ASCII o długości -n ze stosunkiem ilości "a" do długości ciągu -d.

Metoda rozwiązania:
    W celu rozwiązania zadania wykorzystałem tablicę prefikso-prefiksową.
        Tablica ta podaje wartość najdłuzszego wspolnego słowa dla całego wyrazu oraz jego podsłowa zaczynającego się na pozycji j, gdzie j>0. Algorytm budujący tę tablice wykorzystuje informacje o budowie wyrazu na podstawie wcześniej policzonych wartości najdłuższych wspólnych prefiksów. Złożoność czasowa algorytmu jest równa O(N).
    Zastosowanie algorytmu:
        Algorytm został wykorzystany w celu policzenia sumy najdłuższych prefiksów całego słowa dla kolejnych sufiksów.
    Struktura danych:
        Dla każdego ciągu zostaje wytworzona tablice o długości ciągu.
        Złożoność pamięciowa algorytmu jest równa O(n).


Prgoram składa się z dwóch plików:
    aal.py:
        Opdowiada za przeliczanie 4 trybów pracy.
    W celu skorzystania z programu na potrzeby interfejsu graficznego można skorzystać z klasy PrefixSum, która posiada wszystkie potrzebne metody do korzystania ze wszystkich trybów pracy.
    gen.py:
        Odpowiada za generowanie pseudolosowych danych wejściowych.
        W celu skorzystania z programu na potrzeby interfejsu graficznego można skorzytsać z klasy Generate, z której następnie można generować słowa o dowolnej długości i o dowolnym stosunku liczby znaków "a" w całym słowie.

