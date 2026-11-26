# Manga Reader

Offline-fähiger Manga-/Webtoon-Reader für das Handy (PWA). Eine HTML-Datei, keine Abhängigkeiten, keine Server-Anbindung.

- Öffnet **CBZ**, **ZIP**, **PDF** und einzelne Bilder (JPG, PNG, WebP, GIF, AVIF)
- Bibliothek mit Cover und Lesefortschritt, alles bleibt lokal im Browser des Geräts
- Seitenmodus (R→L oder L→R, Passend/Breite) und Scroll-Modus für Webtoons
- Tippen oder Wischen zum Blättern, Slider, Vollbild

## Installieren (Android)
1. Seite in Chrome öffnen: `https://gronkh68-rgb.github.io/Manga-Reader/`
2. Menü → „App installieren“ bzw. „Zum Startbildschirm hinzufügen“

## Hosting
GitHub → Settings → Pages → Branch `main`, Ordner `/ (root)`.

## Aktualisieren
Nach Änderungen an `index.html` in `sw.js` die Konstante `CACHE` hochzählen (`manga-reader-v3` …), sonst liefert der Offline-Cache die alte Version.

Nicht unterstützt: CBR/RAR, ZIP64 (Archive über 4 GB), Doppelseiten nebeneinander.

## Drittanbieter
PDF-Seiten rendert [pdf.js](https://github.com/mozilla/pdf.js) 4.10.38 (Apache-2.0, Lizenz in `pdfjs-LICENSE.txt`). Es wird erst beim ersten PDF geladen. PDFs mit Passwort werden nicht unterstützt.
