# Paderborner Kneipenplan

Basierend auf dem Kneipenplan der Fachschaft Mathematik/Informatik mit
deren freundlicher Genehmigung. Die Live-Version ist unter http://codeforpb.github.io/Kneipenplan/
zu finden.

Die erste bekannte Version des Kneipenplans wurde für die Tagung der 
deutschsprachigen Mathematikfachschaften im Herbst 1990 erstellt. Die Teilnehmer 
dieser Tagung wurden mit einem Verzeichnis der Paderborner Kneipen begrüßt. Der 
ursprüngliche Plan kann auf den Seiten der Fachschaft heruntergeladen werden: 
https://fsmi.uni-paderborn.de/service/essen-und-trinken/kneipenplan/version-10/


# Zur Entwicklung
## Kneipenplan updaten
Öffne entweder einen Issue mit Änderungen oder Vorschlägen, oder sende eine Email an ljan@mail.upb.de - es wird jedoch an einer besseren Methode gearbeitet ;)

Alternativ kannst du auch das Projekt klonen und einen Pull-Request erstellen.

### Neue Lokalität hinzufügen
    rake bar name="Pub" [lat="51.708407964756205"] [lon="8.771488666534424"] [date="2015-05-05"]
    # Oder...
    rake food name="Grill|Cafe" [lat="51.708407964756205"] [lon="8.771488666534424"] [date="2015-05-05"]
Erzeugen eine neue Datei für die Bar oder den Imbiss, die eckigen Klammern symbolisieren die Optionalität der Koordinaten und des Datums. Danach sollte die Datei geöffnet werden und ein `special: "GibtsNurHierBier 0,5l für 42 €`", sowie ein Text am Ende der Datei eingetragen werden.

## Projekt starten

 * [Jekyll](http://jekyllrb.com/docs/installation/) installieren
 * Projekt clonen
 * ```jekyll serve -w``` im geklonten Projekt ausführen

Anschließend wird eine URL angezeigt, auf der eine lokale Kopie der Seite erreichbar ist. Dort können alle Änderungen ausprobiert werden.
