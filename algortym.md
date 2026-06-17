# Algorytm podziału subwencji AGH – WTK

## KROK 1 — Zbieramy dane źródłowe

Algorytm potrzebuje 4 grup danych.

---

# A. Studenci

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

# B. Kadra

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

# C. Badania

### Źródło danych

* POL-on
* Ewaluacja działalności naukowej

### Tabela wejściowa

| Dyscyplina            |  N | Kategoria |
| --------------------- | -: | --------- |
| Technologie kosmiczne | 35 | A         |

---

# D. Projekty

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

gdzie:

| Parametr | Znaczenie                |
| -------- | ------------------------ |
| Uri      | udział studenta          |
| Wk       | kosztochłonność kierunku |
| Wz       | współczynnik zagraniczny |

---

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

Wtedy:

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

---

## Kadra zagraniczna

| Stanowisko       | Waga |
| ---------------- | ---: |
| Profesor         |  3.0 |
| Profesor uczelni |  2.4 |
| Adiunkt          |  1.8 |
| Pozostali        |  1.5 |

---

## Przykład WTK

6 profesorów

5 profesorów uczelni

28 adiunktów

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

Wtedy:

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

Wzór:

```text
B* = N × KS × Kn
```

gdzie:

| Parametr | Znaczenie                  |
| -------- | -------------------------- |
| N        | liczba N                   |
| KS       | kosztochłonność dyscypliny |
| Kn       | współczynnik kategorii     |

---

## WTK

```text
N = 35
KS = 3.25
Kn = 1.0 (kategoria A)
```

Obliczenie:

```text
35 × 3.25 × 1.0
=
113.75
```

Otrzymujemy:

```text
B* = 113.75
```

---

Zakładamy:

```text
ΣB = 7000
```

Wtedy:

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

Zakładamy:

```text
AGH:
300 000 000 zł
```

Wtedy:

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

## Wagi algorytmu

| Składnik | Waga |
| -------- | ---: |
| Studenci | 0.33 |
| Kadra    | 0.33 |
| Badania  | 0.29 |
| Projekty | 0.05 |

---

Wzór:

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

Najważniejszy element algorytmu.

```text
D_i

=
0.5 × D_hist
+
0.5 × D_alg
```

---

## Dla standardowego wydziału

```text
50% poprzedni rok

50% nowy algorytm
```

---

## WTK jest wyjątkiem

WTK powstał:

```text
01.04.2025
```

Nie posiadał własnej historii subwencji.

Dlatego bardzo prawdopodobne jest, że:

```text
5 mln zł

=
finansowanie startowe
+
algorytm
```

a nie wyłącznie wynik wzorów.

---

# Jakie tabele powinien mieć WTK Strategic Planner?

## STUDENCI

| Kierunek | Rok | PL | Zagr |
| -------- | --- | -: | ---: |

---

## KADRA

| Typ | Polska | Zagranica |
| --- | -----: | --------: |

---

## BADANIA

| Dyscyplina |  N | KS | Kategoria |
| ---------- | -: | -: | --------- |

---

## PROJEKTY

| Program | Kwota |
| ------- | ----: |

---

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
