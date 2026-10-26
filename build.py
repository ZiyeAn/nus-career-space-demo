from pathlib import Path
root = Path(__file__).resolve().parent
html = (root / 'index.html').read_text()
html = html.replace('<link rel="stylesheet" href="styles.css?v=20261026c">', '<style>' + (root / 'styles.css').read_text() + '</style>')
html = html.replace('<script src="app.js?v=20261026c"></script>', '<script>' + (root / 'app.js').read_text() + '</script>')
(root / 'NUS Career Space.html').write_text(html)
