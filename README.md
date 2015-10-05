**Dies ist nur ein temporärer Klon für die Angebote der Ophase. Updates am 
Kneipenplan selbst (Kneipe zu, Daten falsch, etc.) sollten entweder im Branch 
"upstream-master" gemacht und in den master branch gemergt werden; dadurch 
können sie leicht in die Live-Version überführt werden.

Das Live-Repo sollte als remote hinzugefügt werden: ```git remote add upstream 
git@github.com:codeforpb/Kneipenplan.git```.**

# OPhase

## Quickstart

 * [Jekyll](http://jekyllrb.com/docs/installation/) installieren
 * Projekt clonen
 * ```jekyll serve -w``` im geklonten Projekt ausführen
 * Der Webserver sollte nun starten

Ein aktueller Stand der Anfragen ist anschließend unter zu finden http://127.0.0.1:4000/Kneipenplan/ophase/

## Lokalen Klon aktualisieren

```cd $PROJECT_DIR; git pull```

## Anfrage einpflegen

Mit einem Text-Editor die Datei zur Kneipe unter ```bars/_posts/``` öffnen. 
Anschließend die Felder ```student``` und ```teamer``` ergänzen.

Beispiel: 
```
---
name: "Zum Ölberg"
lat: 51.72087618818835 
lon: 8.759397268295288
streetAndNr: "An den Kapuzinern 20"
plz: "33098"
link: "http://www.zumölberg.de"
tel: "05251 7097671"
student: "Bier: 0.3l 1.80€, 0.5l 2.80€; 
Weizen 0.5l 2.80€; 
Cola/Fanta/Sprite: 0.3l 1.90€, 0.5l  2.90€; 
Cocktails 3.60€;
Jägermeister 1.40€;
Ölberger 1.30€"
teamer: "Ölberger oder 0.3l Bier"
---
Mitwochs Weizen 0,5 für 2,40€, Donnerstag 2 Cocktails für 1 ab 19 Uhr
```

> Die Felder dürfen Zeilenumbrüche zur besseren Lesbarkeit enthalten; diese werden
> in der Ausgabe ignoriert.

## Kneipenplan-Handout drucken

 * Starten wie Quickstart
 * Ein Druck-Befehl auf http://127.0.0.1:4000/Kneipenplan/ophase/ erzeugt dank 
   HTML & CSS ein fertiges Handout.

> Falls zu viele Kneipen oder zu viele Angebote existieren, können einzelne 
> Kneipen durch Löschen auf bars/_posts/ entfernt werden.

# Paderborner Kneipenplan

Basierend auf dem Kneipenplan der Fachschaft Mathematik/Informatik mit
deren freundlicher Genehmigung. Die Live-Version ist unter 
http://codeforpb.github.io/Kneipenplan/ zu finden.

Die erste bekannte Version des Kneipenplans wurde für die Tagung der 
deutschsprachigen Mathematikfachschaften im Herbst 1990 erstellt. Die Teilnehmer 
dieser Tagung wurden mit einem Verzeichnis der Paderborner Kneipen begrüßt. Der 
ursprüngliche Plan kann auf den Seiten der Fachschaft heruntergeladen werden: 
https://fsmi.uni-paderborn.de/service/essen-und-trinken/kneipenplan/version-10/


# Zur Entwicklung
## Kneipenplan updaten
Öffne entweder einen Issue mit Änderungen oder Vorschlägen, oder sende eine 
Email an ljan@mail.upb.de - es wird jedoch an einer besseren Methode gearbeitet 
;)

Alternativ kannst du auch das Projekt klonen und einen Pull-Request erstellen.

### Neue Lokalität hinzufügen
    rake bar name="Pub" [lat="51.708407964756205"] [lon="8.771488666534424"] [date="2015-05-05"]
    # Oder...
    rake food name="Grill|Cafe" [lat="51.708407964756205"] [lon="8.771488666534424"] [date="2015-05-05"]
Erzeugen eine neue Datei für die Bar oder den Imbiss, die eckigen Klammern 
symbolisieren die Optionalität der Koordinaten und des Datums. Danach sollte die 
Datei geöffnet werden und ein `special: "GibtsNurHierBier 0,5l für 42 €`", sowie 
ein Text am Ende der Datei eingetragen werden.

## Projekt starten

 * [Jekyll](http://jekyllrb.com/docs/installation/) installieren
 * Projekt clonen
 * ```jekyll serve -w``` im geklonten Projekt ausführen

Anschließend wird eine URL angezeigt, auf der eine lokale Kopie der Seite 
erreichbar ist. Dort können alle Änderungen ausprobiert werden.