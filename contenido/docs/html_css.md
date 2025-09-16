# HTML & CSS

Demostración con **pestañas** y **admoniciones** (Material).

=== "HTML"
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Proyecto LMSGI — Lenguajes de marcas</title>
    </head>
    <body>
      <header>
        <h1>Proyecto LMSGI — Lenguajes de marcas</h1>
        <nav aria-label="principal">
          <ul>
            <li><a href="#">Inicio</a></li>
            <li><a href="#">Catálogo</a></li>
            <li><a href="#">RSS</a></li>
            <li><a href="#">Logo SVG</a></li>
          </ul>
        </nav>
      </header>
      <main>
        <section>
          <h2>Qué incluye</h2>
          <ul>
            <li><strong>HTML5 + CSS</strong></li>
            <li><strong>XML</strong> con DTD/XSD y <strong>XSLT</strong></li>
            <li><strong>RSS 2.0</strong></li>
            <li><strong>SVG</strong></li>
            <li><strong>JSON</strong></li>
          </ul>
        </section>
      </main>
      <footer>
        <small>&copy; 2025 Aula ASIX — LMSGI</small>
      </footer>
    </body>
    </html>
    ```

=== "CSS"
    ```css
    /* Estilos mínimos para la plantilla LMSGI */
    :root { --maxw: 900px; }
    * { box-sizing: border-box; }
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, 'Helvetica Neue', Arial, 'Noto Sans'; line-height: 1.5; margin: 0; }
    main, header, footer { max-width: var(--maxw); margin: 0 auto; padding: 1rem; }
    header { background: #f5f5f5; border-bottom: 1px solid #ddd; }
    header h1 { margin: 0 0 .5rem; }
    nav ul { display: flex; gap: 1rem; list-style: none; padding: 0; margin: 0; flex-wrap: wrap; }
    nav a { text-decoration: none; }
    section { margin-block: 1.25rem; }
    code {{ background: #f0f0f0; padding: .1rem .3rem; border-radius: .25rem; }}
    table { width: 100%; border-collapse: collapse; }
    th, td { border: 1px solid #ddd; padding: .5rem; text-align: left; }
    th { background: #fafafa; }
    footer { border-top: 1px solid #ddd; background: #fafafa; }
    ```

!!! info "Validación rápida"
    - HTML → <https://validator.w3.org/>
    - CSS → <https://jigsaw.w3.org/css-validator/>
