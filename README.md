# Berliner Obsttaxi

Eine grelle, übertriebene Einzelseite als Teil einer Schnitzeljagd. Die Seite ist statisch und für GitHub Pages gedacht.

## Lokal ansehen

Starte im Projektverzeichnis einen lokalen Webserver:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Öffne anschließend <http://127.0.0.1:8000/>.

## Auf GitHub Pages veröffentlichen

1. Öffne im GitHub-Repository **Settings → Pages**.
2. Wähle bei **Build and deployment** die Option **Deploy from a branch**.
3. Wähle den Branch `main` und den Ordner `/ (root)`, dann **Save**.
4. Warte, bis GitHub die Seite veröffentlicht hat. Beim ersten Mal kann das etwas dauern.

Die Projektseite ist anschließend unter `https://<owner>.github.io/test_pages/` erreichbar. Ersetze `<owner>` durch den GitHub-Benutzernamen oder die Organisation, der das Repository gehört.

## Inhalte anpassen

- `index.html` enthält die Texte, Kategorien, Hinweise und Platzhalter.
- `styles.css` enthält die Farben, WordArt-artigen Effekte und das responsive Layout.
- Der Kurierkontakt und das Video sind momentan Platzhalter und müssen vor dem Einsatz im Spiel ersetzt bzw. ausgearbeitet werden.
