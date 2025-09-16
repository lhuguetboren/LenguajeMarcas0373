# XPath & XSLT

**XPath** selecciona nodos en XML; **XSLT** los transforma (p. ej., a HTML).

## XPath (ejemplos)
```xpath
/catalogo/curso
/catalogo/curso[@id='ASIX1']
//modulo[@horas>130]
/catalogo/curso[nombre='ASIX 2']
//modulo[contains(., 'Sistemas')]
```

## XSLT de ejemplo
```xsl
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" version="5" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/">
    <html lang="es">
      <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title>Catálogo de cursos</title>
      </head>
      <body>
        <h1>Catálogo de cursos</h1>
        <xsl:for-each select="catalogo/curso">
          <h2><xsl:value-of select="nombre"/></h2>
          <table border="1" cellpadding="4" cellspacing="0">
            <thead>
              <tr>
                <th>Código</th>
                <th>Horas</th>
                <th>Nombre</th>
              </tr>
            </thead>
            <tbody>
              <xsl:for-each select="modulos/modulo">
                <tr>
                  <td><xsl:value-of select="@codigo"/></td>
                  <td><xsl:value-of select="@horas"/></td>
                  <td><xsl:value-of select="."/></td>
                </tr>
              </xsl:for-each>
            </tbody>
          </table>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>

```

!!! exercise "Actividad"
    Ordena los módulos por `@horas` (mayor a menor) y añade una fila de totales.
