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
  <a href="#about-the-project">About The Project</a>
  <ol>     
    <li><a href="#dt">Data Types</a></li>
    <li><a href="#print">Print</a></li>
    <li><a href="#operanden">Operanden</a></li>
    <li><a href="#if-else">If-Else</a></li>
    <li><a href="#random">Random</a></li>
    <li><a href="#while-for">While For</a></li>
    <li><a href="#ds">Data Structures</a></li>
    <li><a href="#fstrings">f'Strings</a></li>
    <li><a href="#funktionen">Funktionen</a></li>
  </ol>
  <li><a href="#projects">Mini Projects</a></li>
</details>
    
    
<!-- ABOUT THE PROJECT -->

<h2 id="about-the-project">About The Project</h2>
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
print(type("Hallo))

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

<!-- Data Structures -->

<h2 id="ds">Data Structures</h2>
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

<h2 id="fstrings">f'Strings</h2>
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

<h2 id="funktionen">Funktionen</h2>
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

<img align="right" width="240" src= "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/5eeea355389655.59822ff824b72.gif"/>
<img align="center" width="240" src="https://i.pinimg.com/originals/6e/a8/c6/6ea8c68dfa924bc2e6a9abe3e473087a.gif"/>
<img width= "240" src= "https://pa1.narvii.com/6580/8098c6e9207376889eeb0532d9f5a0723c4d73f5_hq.gif"/>

