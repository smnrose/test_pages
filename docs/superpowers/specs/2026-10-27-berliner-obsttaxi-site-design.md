# Berliner Obsttaxi – Website-Entwurf

## Ziel

Eine erste, mobilfreundliche Website für eine Schnitzeljagd, die über eine Visitenkarte aufgerufen wird. Die Seite soll eine absurde, grelle „Berliner Obsttaxi“-Inszenierung bieten und beim Erkunden zu einem Kontakt-Platzhalter als nächstem Spielhinweis führen. Der Entwurf dient zugleich als einfacher Test für GitHub Pages.

## Gestalterische Richtung

- Ein überdrehtes, bewusst kitschiges Schaufenster mit Darknet-Anmutung als Gag.
- Grelle Farben, plakative WordArt-artige Überschriften und absurde Werbesprüche.
- Die Oberfläche darf visuell chaotisch wirken, Texte und Rätselhinweise müssen aber gut lesbar bleiben.
- Die Seite soll auf Smartphones funktionieren, da sie über eine Visitenkarte aufgerufen wird.

## Seitenaufbau

Eine einzelne Seite mit diesen Bereichen:

1. **Kopfbereich:** Großer „Berliner Obsttaxi“-Titel und eine übertriebene Werbezeile.
2. **Kategorien:** Navigation zu Themen-/Angebotsabschnitten per Sprungmarke innerhalb der Seite.
3. **Angebote:** Mehrere absurde Angebotskarten, in denen sich die Rätselhinweise verteilen.
4. **Video-Platzhalter:** Auffällige Posterfläche mit einem Hinweis, dass der Clip noch folgt. Motiv und tatsächliche Einbindung werden später festgelegt.
5. **Abschlussbereich:** Kontakt-Platzhalter und ein kurzer Hinweis, dass dies der nächste Schritt im Spiel ist.

## Rätselablauf

- Eine klare, leicht lösbare Haupträtselspur führt vom Werbebanner über ein auffälliges Detail in einer Kategorie zum Kontakt-Platzhalter.
- Optionale Easter Eggs können in weiteren Kategorien liegen, sind aber nicht nötig, um den nächsten Schritt zu finden.
- Die Hinweise sind spielerisch versteckt, nicht als geheime Daten geschützt; sie können im Seitenquelltext sichtbar sein.
- Der Kontakt bleibt im Entwurf ein Platzhalter und wird später durch einen eigens für das Spiel vorgesehenen Kontakt ersetzt.

## Technischer Rahmen

- Statische Website für GitHub Pages; keine Datenbank, kein Server und keine Konten.
- Kategorien verwenden interne Sprungmarken. HTML und CSS reichen für den beschriebenen Aufbau; JavaScript ist nur bei später ergänzter Interaktion nötig.
- Der Video-Platzhalter lässt sich später durch ein eingebettetes oder lokal bereitgestelltes Video ersetzen.
- Die Messenger-/Bot-Interaktion ist nicht Teil dieser Website-Spezifikation.

## Abnahmekriterien

- Die Seite lässt sich als statische Website über GitHub Pages bereitstellen.
- Kategorie-Navigation führt zu den passenden Abschnitten.
- Der Hauptpfad vom Kopfbereich über eine Angebotskarte zum Kontakt-Platzhalter ist ohne langes Suchen verständlich.
- Optionale Hinweise sind nicht erforderlich, um den Hauptpfad abzuschließen.
- Auf schmalen Smartphone-Displays bleiben Navigation, Hinweise und Platzhalter lesbar und bedienbar.
- Die Video-Fläche ist als Platzhalter erkennbar und kann später ausgetauscht werden.
