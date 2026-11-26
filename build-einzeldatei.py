#!/usr/bin/env python3
"""Baut aus index.html eine eigenständige Einzeldatei (mangareader.html) mit eingebettetem pdf.js.
Ohne Service Worker und Manifest, läuft per Doppelklick (file://). Aufruf: python3 build-einzeldatei.py"""
import base64, re

src = open('index.html', encoding='utf-8').read()

# pdf.js aus eingebetteten Blobs laden statt aus Dateien
a = src.index('let pdfjsP = null;')
b = src.index('async function pdfPages')
loader = '''let pdfjsP = null;
function b64Blob(id, type) {
  const bin = atob(document.getElementById(id).textContent.trim());
  const u8 = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) u8[i] = bin.charCodeAt(i);
  return new Blob([u8], { type: type });
}
function loadPdfjs() {
  if (!pdfjsP) pdfjsP = import(URL.createObjectURL(b64Blob('lib-pdf', 'text/javascript'))).then(m => {
    m.GlobalWorkerOptions.workerSrc = URL.createObjectURL(b64Blob('lib-worker', 'text/javascript'));
    return m;
  });
  return pdfjsP;
}

'''
src = src[:a] + loader + src[b:]

# PWA-Teile entfernen
for pat in (r'<link rel="manifest"[^\n]*\n', r'<link rel="icon"[^\n]*\n', r'<link rel="apple-touch-icon"[^\n]*\n'):
    src = re.sub(pat, '', src)
src = re.sub(r'/\*SW-BEGIN\*/.*?/\*SW-END\*/\n', "const APP_VERSION = 'v6 · Datei';\n$('#ver').textContent = APP_VERSION;\n$('#ver').style.textDecoration = 'none';\n", src, flags=re.S)
src = re.sub(r"const APP_VERSION = 'v6 · Datei';", lambda m: m.group(0), src)

enc = lambda f: base64.b64encode(open(f, 'rb').read()).decode()
libs = ('<script type="application/octet-stream" id="lib-pdf">' + enc('pdf.min.mjs') + '</script>\n'
        '<script type="application/octet-stream" id="lib-worker">' + enc('pdf.worker.min.mjs') + '</script>\n')
i = src.index("<script>\n'use strict';")
src = src[:i] + libs + src[i:]
assert 'serviceWorker' not in src and 'rel="manifest"' not in src
open('mangareader.html', 'w', encoding='utf-8').write(src)
print('mangareader.html', len(src) // 1024, 'KB')
