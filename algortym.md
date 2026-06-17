# Algorytm podziału subwencji AGH – WTK

## Wprowadzenie

Niniejszy dokument przedstawia uproszczony opis algorytmu podziału subwencji stosowanego w AGH oraz sposób jego wykorzystania do planowania rozwoju Wydziału Technologii Kosmicznych (WTK).

Celem dokumentu nie jest odtworzenie wszystkich szczegółów formalnych uchwały, lecz pokazanie:

* jakie dane wpływają na wysokość subwencji,
* które parametry mają największe znaczenie,
* jak interpretować wyniki algorytmu,
* jakie działania mogą zwiększyć subwencję WTK w kolejnych latach.

Dla WTK szczególnie istotne są:

1. liczba studentów,
2. liczba studentów zagranicznych,
3. struktura kadry,
4. kategoria naukowa,
5. przychody projektowe.

---

# Główne równanie algorytmu

Najpierw wyliczana jest część algorytmiczna:

```text
D_alg
=
0.33 × Sp
+
0.33 × Na
+
0.29 × B
+
0.05 × P
```

gdzie:

* `Sp` – udział studencki,
* `Na` – udział kadrowy,
* `B` – udział badawczy,
* `P` – udział projektowy.

## Wagi algorytmu

| Składnik | Waga |
| -------- | ---: |
| Studenci |  33% |
| Kadra    |  33% |
| Badania  |  29% |
| Projekty |   5% |

---

# Mechanizm historyczny

Ostateczna subwencja nie zależy wyłącznie od aktualnych danych.

AGH stosuje mechanizm stabilizacyjny:

```text
D_i
=
0.5 × D_hist
+
0.5 × D_alg
```

gdzie:

* `D_hist` – udział jednostki w poprzednim roku,
* `D_alg` – udział wynikający z aktualnych parametrów.

Oznacza to, że:

```text
50% wyniku
=
poprzedni rok

50% wyniku
=
nowy algorytm
```

Dzięki temu nawet duże zmiany liczby studentów lub kadry nie przekładają się natychmiast na pełną zmianę subwencji.

---

# Specyfika WTK

Wydział Technologii Kosmicznych został utworzony 1 kwietnia 2025 roku.

WTK nie posiadał własnej historii subwencji porównywalnej z pozostałymi wydziałami AGH.

Dlatego bardzo prawdopodobne jest, że przy pierwszym podziale środków zastosowano dodatkowe mechanizmy związane z uruchomieniem nowej jednostki.

Można to uprościć do zależności:

```text
Subwencja WTK
≈
Finansowanie startowe
+
Wpływ algorytmu
```

Dlatego odtworzenie kwoty około 5 mln zł wyłącznie na podstawie wzorów może nie być możliwe bez danych historycznych i decyzji organizacyjnych podjętych przy tworzeniu wydziału.

---

# KROK 1 — Zbieramy dane źródłowe

Algorytm potrzebuje 4 grup danych.

## A. Studenci

### Źródło danych

* USOS
* stan na 31.12
* stan na ok. 23.03

### Dane wejściowe

| Pole                             | Przykład |
| -------------------------------- | -------: |
| Liczba studentów                 |      120 |
| Liczba studentów zagranicznych   |        3 |
| Współczynnik kosztochłonności Wk |    2.125 |

---

## B. Kadra

### Źródło danych

* SAP Kadry
* POL-on

### Tabela wejściowa

| Typ              | Liczba |
| ---------------- | -----: |
| Profesor         |      6 |
| Profesor uczelni |      5 |
| Adiunkt          |     28 |
| Pozostali        |      0 |

Dodatkowo osobno raportowana jest kadra zagraniczna.

---

## C. Badania

### Źródło danych

* POL-on
* Ewaluacja działalności naukowej

### Tabela wejściowa

| Dyscyplina            |  N | Kategoria |
| --------------------- | -: | --------- |
| Technologie kosmiczne | 35 | A         |

---

## D. Projekty

### Źródło danych

* SAP
* Dział Nauki AGH

### Tabela wejściowa

| Program        | Kwota |
| -------------- | ----: |
| ESA            |       |
| NCN            |       |
| NCBR           |       |
| Horizon Europe |       |
| Inne           |       |

---

# KROK 2 — Liczymy studentów ważonych

Dla każdego studenta:

```text
Student = Uri × Wk × Wz
```

| Parametr | Znaczenie                |
| -------- | ------------------------ |
| Uri      | udział studenta          |
| Wk       | kosztochłonność kierunku |
| Wz       | współczynnik zagraniczny |

## WTK – Space Technologies

```text
Wk = 2.125
```

### Student polski

```text
1 × 2.125 × 1
=
2.125
```

### Student zagraniczny

```text
1 × 2.125 × 7
=
14.875
```

### Przykład

117 studentów polskich

3 studentów zagranicznych

```text
117 × 2.125
+
3 × 14.875
=
293.25
```

Otrzymujemy:

```text
ESt = 293.25
```

---

# KROK 3 — Liczymy udział studencki

Zakładamy:

```text
ΣESt = 25 000
```

```text
Sp = ESt / ΣESt

Sp = 293.25 / 25 000

Sp = 0.01173
```

czyli:

```text
1.17%
```

udziału studenckiego AGH.

---

# KROK 4 — Liczymy kadrę

## Kadra krajowa

| Stanowisko       | Waga |
| ---------------- | ---: |
| Profesor         |  2.5 |
| Profesor uczelni |  2.0 |
| Adiunkt          |  1.5 |
| Pozostali        | 1.25 |

## Kadra zagraniczna

| Stanowisko       | Waga |
| ---------------- | ---: |
| Profesor         |  3.0 |
| Profesor uczelni |  2.4 |
| Adiunkt          |  1.8 |
| Pozostali        |  1.5 |

### Przykład WTK

```text
6 × 2.5
+
5 × 2.0
+
28 × 1.5
=
67
```

Otrzymujemy:

```text
Na* = 67
```

---

# KROK 5 — Liczymy udział kadrowy

Zakładamy:

```text
ΣNa* = 3500
```

```text
Na = 67 / 3500

Na = 0.0191
```

czyli:

```text
1.91%
```

udziału kadrowego AGH.

---

# KROK 6 — Liczymy badania

```text
B* = N × KS × Kn
```

### WTK

```text
N = 35
KS = 3.25
Kn = 1.0
```

```text
35 × 3.25 × 1.0
=
113.75
```

Otrzymujemy:

```text
B* = 113.75
```

Zakładamy:

```text
ΣB = 7000
```

```text
B = 113.75 / 7000

B = 0.0163
```

czyli:

```text
1.63%
```

udziału badawczego AGH.

---

# KROK 7 — Liczymy projekty

Przykład:

```text
WTK:
5 000 000 zł
```

```text
AGH:
300 000 000 zł
```

```text
P = 5 000 000 / 300 000 000

P = 0.0167
```

czyli:

```text
1.67%
```

udziału projektowego AGH.

---

# KROK 8 — Łączymy wszystkie składniki

```text
D_alg

=
0.33 × Sp
+
0.33 × Na
+
0.29 × B
+
0.05 × P
```

Przykład:

```text
0.33 × 1.17
+
0.33 × 1.91
+
0.29 × 1.63
+
0.05 × 1.67
```

Otrzymujemy udział WTK w nowej części algorytmu.

---

# KROK 9 — Składnik historyczny

```text
D_i

=
0.5 × D_hist
+
0.5 × D_alg
```

Dla standardowego wydziału:

```text
50% poprzedni rok

50% nowy algorytm
```

WTK jest wyjątkiem ze względu na utworzenie wydziału w 2025 roku.

---

# Dane wymagane przez WTK Strategic Planner

## STUDENCI

| Kierunek | Rok | PL | Zagr |
| -------- | --- | -: | ---: |

## KADRA

| Typ | Polska | Zagranica |
| --- | -----: | --------: |

## BADANIA

| Dyscyplina |  N | KS | Kategoria |
| ---------- | -: | -: | --------- |

## PROJEKTY

| Program | Kwota |
| ------- | ----: |

## AGH BASELINE

| Parametr | AGH |
| -------- | --: |
| ΣESt     |     |
| ΣNa*     |     |
| ΣB       |     |
| ΣP       |     |

---

# Wniosek

To jest minimalny zestaw danych wymagany do odtworzenia algorytmu podziału subwencji AGH dla WTK.

Bez tych pięciu tabel nie da się wiarygodnie policzyć:

* udziału wydziału,
* wpływu zmian organizacyjnych,
* prognoz subwencji,
* ROI działań rozwojowych.

Na tych danych powinien opierać się WTK Strategic Planner.
