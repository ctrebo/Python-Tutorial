<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
</div>

<h1 align="center">Förderwochenkurs Python <img src = "https://media2.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif?cid=ecf05e47a0n3gi1bfqntqmob8g9aid1oyj2wr3ds3mg700bl&rid=giphy.gif" width = 32px></h1>

  
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Kapitel</summary>
  <a href="#about-the-project">Über das Projekt</a>
  <ol>     
    <li><a href="#dt">Data Types</a></li>
    <li><a href="#print">Print</a></li>
    <li><a href="#operanden">Operanden</a></li>
    <li><a href="#if-else">If-Else</a></li>
    <li><a href="#random">Random</a></li>
    <li><a href="#while-for">While For</a></li>
    <li><a href="#ds">Listen</a></li>
    <li><a href="#fstrings">f'Strings</a></li>
    <li><a href="#funktionen">Funktionen</a></li>
  </ol>
  <li><a href="#projects">Mini Projects</a></li>
</details>
    
    
<!-- ABOUT THE PROJECT -->

<h2 id="about-the-project">Über das Projekt</h2>
Dieser Kurs wurde im Rahmen der Förderwoche in der TFO Bruneck im Jahr 2022 erstellt. 


<!-- Data Type -->

<h2 id="dt">Data Types</h2>

In Python gibt es folgende Datentypen:

* String --> "Hallo" (Wichtig: Alles zwischen zwei Anführungszeichen ist ein String, also auch "4" oder "4.0"
* Int --> 4
* Float --> 4.0
* Bool --> True/False

Hinweis: Mit der `type()` Funktion kann der Datentyp auch manuell herausgefunden werden<br>

```python
print(type("Hallo"))

```

<pre><'class string'></pre>

<!-- Print -->
<h2 id="print">Print</h2>
Mit der <code>print()</code> Funktion kann man in Python Werte im Terminal ausgeben lassen. <br>
Die Print-Funktion akzeptiert jeden Datentyp, jedoch dürfen verschiedene Datentypen nicht einfach so gemischt werden. Lösungen für dieses Problem sind entweder die String-Addition oder sogenannte <a href="#fstrings">f-Strings</a>, auf welche wir später eingehen werden.
`
<!-- Operanden -->
<h2 id="operanden">Operanden</h2>
Die gängigsten Operatoren in Python sind:
<img src="images/Operatoren.png" alt="Logo">
<figcaption class="caption">Quelle: W3Schools</figcaption>
<h3>String-Addition</h3>
Auch Strings können mit dem <code>+</code> Operator zusammengefügt werden.<br>
Addiert man jedoch zwei verschiedene Datentypen miteinander(z.B "Hallo" + 4), wird ein Fehler angezeigt.<br>
Um diesen Fehler zu beheben muss man die Zahl in einen String-Wert umwandeln. Dies geht mit der <code>str()</code> Funktion.<br>
<code>str(4)</code> --> <code>"4"</code>

<!-- If-else -->
<h2 id="if-else">If-Else</h2>
<p>Mit sogenannten "if-statements" kann man in Python eine Bedingung an die Ausführung eines Codes knüpfen.<br>
Dafür stehen einen folgende Vergleichsoperatoren zur verfügung: </p>

* Gleichheit: <code>a == b</code>
* Ungleichheit: <code>a != b</code>
* Größer als: <code>a > b</code>
* Größer-Gleich: <code>a >= b</code>
* Kleiner als: <code>a < b</code>
* Kleiner-Gleich: <code>a <= b</code>

**Syntax**: Bei if-statements wird die Bedingung, beendet mit einem <code>:</code>, normal angeschrieben.<br>
Der Teil, welcher nur unter der Bedingung ausgeführt werden soll, wird eingerückt.


```python
if a == b:
    print("a und b sind gleich")
```
<h3>elif</h3>

Elif-Statements sagen dem Programm, dass wenn die Bedingung darüber nicht eintrifft, es diese Bedingung überprüfen soll.

```python
if a == b:
    print("a und b sind gleich")
elif a != b:
    print("a und b sind ungleich")
```

<h3>else</h3>

Else-Statement bewirken, dass falls keine der übergeordneten Bedingungen eintrifft, etwas bestimmtes ausgeführt werden soll. 

```python
if a > b:
    print("a ist größer als b")
elif a < b:
    print("a ist kleiner als b")
else:
    print("a und b sind gleich groß")
```
<!-- Random -->
<h2 id="random">Random</h2>
Die Random-Bibliothek ist eine recht häufig verwendete Bibliothek in Python. <br>
Anwendungsbeispiele sind z.B das Generieren einer Zufallszahl oder das zufällige auswählen eines Elements einer Liste. <br>
Hier sind einige der wichtigsten Befehle der Bibliothek aufgelistet:

* <code>random.randrange(start, stop)</code>
* <code>random.choice(seq)</code>

<!-- While For -->
<h2 id="while-for">While-Schleife und For-Schleife</h2>
In Python gibt es 2 primäre Schleifen:

* <code>while</code>-Schleifen
* <code>for</code>-Schleifen

<h3>While-Schleife</h3>
Mit der While-Schleife kann eine Reihe von Statements so lange ausgeführt werden, wie sie Bedingung wahr ist.

```python
# Gib i so lange aus solange es kleiner als 5 ist.
# Bedingung ist in diesem Fall i < 5
i = 1
while i < 5:
  print(i)
  i += 1
```

<h3>For-Schleife</h3>
Mit einer For-Schleife kann man über eine Reihe von Zahlen oder eine Datenstruktur iterieren.

```python
# Gib die Zahlen von 0 bis 5 aus(6 ist ausgeschlossen).
for i in range(6):
    print(i)
```

<!-- Listen -->

<h2 id="lists">Listen</h2>
Listen erlauben es mehrere Elemente in einer Variable zu speichern.

```python
# Deklarieren einer Liste
list_ = [1, 2, 3]
```
Mit dem subscript Operator <code>[ ]</code> kann man auf die Element der Liste zugreifen. Dabei ist wichtig zu wissen, dass der erste Index der Liste 0 ist.

```python
# Greife auf das 1. Element einer Liste zu
list_ = [1, 2, 3]
list_[0] = 5
print(list_[0])
```
Hinweis: Schreibt man [-1] wird auf das letzte Element der Liste zugegriffen.
Elemente können mit 

```python
# Füge Zahl 4 in die Liste ein
list_.append(4)
```
in die Liste eingefügt und mit

```python
# Entferne erstes Element der Liste 
list_.pop(0)
```
entfernt werden.

<h2 id="fstrings">f'Strings</h2>
F-Strings sind eine großartige Methode um Strings zu formatieren.
Vor f-Strings haben wir normalerweise ein '+' benutzt um z.B. Zahlen und Strings zu verbinden

```python
alter = 21
name = "Ivan"
print("Hallo, ich bin " + name + " und ich bin " + str(alter) + " Jaher alt")
```
Mit f-Strings geht es aber um eingies einfacher und übersichtlicher!
```python
alter = 21
name = "Ivan"
print(f"Hallo, ich bin {name} und ich bin {alter} Jaher alt")
```

<h2 id="funktionen">Funktionen</h2>
Wenn die Programme länger und komplexer werden, verwendet man oft Funktionen. <br>
Dabei wird ein gewisser teil des Programmes in eine Funktion geschrieben, und kann unendlich oft im Programm aufgerufen werden.<br>

Eine Funktion wird folgendermaßen definiert und aufgerufen:
```python
def NameDerFuktion():
    ...
    ...


NameDerFunktion()
```
In die Klammern kann auch noch eine Variable geschrieben werden, welche NUR innerhalb der Funktion verarbeitet wird. Beim Aufrufen einer solchen Funktion müssen so viele Werte in die Klammer geschrieben werden, wie bei der Definition angegeben wurden.

```python
def NameDerFuktion(a, b):
    result = a + b
    print(result)
    
NameDerFunktion(2, 3)    
```

<p>Output:</p>
<pre>5</pre>

<img width= "240" src= "https://pa1.narvii.com/6580/8098c6e9207376889eeb0532d9f5a0723c4d73f5_hq.gif"/>

