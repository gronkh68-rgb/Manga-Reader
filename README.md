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

## Aktualisieren
Die App holt Seiten zuerst aus dem Netz, Updates kommen also beim nächsten Start. Wenn sich pdf.js ändert, in `sw.js` die Konstante `CACHE` hochzählen (`manga-reader-v6` …), sonst liefert der Offline-Cache die alte Version.

Nicht unterstützt: CBR/RAR, ZIP64 (Archive über 4 GB), Doppelseiten nebeneinander.

## Drittanbieter
PDF-Seiten rendert [pdf.js](https://github.com/mozilla/pdf.js) 4.10.38 (Apache-2.0, Lizenz in `pdfjs-LICENSE.txt`). Es wird erst beim ersten PDF geladen. PDFs mit Passwort werden nicht unterstützt.
