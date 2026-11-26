# Manga Reader

Offline-fähiger Manga-/Webtoon-Reader für das Handy (PWA). Eine HTML-Datei, keine Abhängigkeiten, keine Server-Anbindung.

- Öffnet **CBZ**, **ZIP**, **PDF** und einzelne Bilder (JPG, PNG, WebP, GIF, AVIF)
- **Bücherregal** mit Covern, Fortschrittsbalken und „Weiterlesen“-Karte; sortierbar (zuletzt gelesen, Titel, hinzugefügt); alles bleibt lokal im Browser des Geräts
- Merkt sich pro Buch Seite, Position auf der Seite, Modus, Leserichtung und Passung (Pinch-Zoom wird nicht gespeichert)
- Seitenmodus (R→L oder L→R, Passend/Breite) und Scroll-Modus für Webtoons
- Tippen oder Wischen zum Blättern, Slider, Vollbild

## Installieren (Android)
1. Seite in Chrome öffnen: `https://gronkh68-rgb.github.io/Manga-Reader/`
2. Menü → „App installieren“ bzw. „Zum Startbildschirm hinzufügen“

## Hosting
GitHub → Settings → Pages → Branch `main`, Ordner `/ (root)`.

## Version und Updates
Oben neben dem Titel steht die Version (z. B. `v6`). Ein Tipp darauf sucht nach Updates. Sobald eine neue Version bereitsteht, erscheint unten „Neue Version verfügbar“ mit Knopf „Aktualisieren“. Die Prüfung läuft beim Öffnen der App und alle 30 Minuten.

## Einzeldatei
`python3 build-einzeldatei.py` erzeugt `mangareader.html`: eine Datei mit eingebettetem pdf.js, läuft per Doppelklick ohne Webadresse. Sie hat keine automatischen Updates.

## Aktualisieren
Bei jedem Release in `sw.js` die Konstante `CACHE` hochzählen (`manga-reader-v7` …) und in `index.html` `APP_VERSION` sowie die Anzeige `v6` im Header (`#ver`) anpassen. Das hochgezählte `sw.js` löst bei den Handys den „Neue Version verfügbar“-Hinweis aus. In `build-einzeldatei.py` die Dateiversion mitziehen.

Nicht unterstützt: CBR/RAR, ZIP64 (Archive über 4 GB), Doppelseiten nebeneinander.

## Drittanbieter
PDF-Seiten rendert [pdf.js](https://github.com/mozilla/pdf.js) 4.10.38 (Apache-2.0, Lizenz in `pdfjs-LICENSE.txt`). Es wird erst beim ersten PDF geladen. PDFs mit Passwort werden nicht unterstützt.
