# RSS (2.0)

Ejemplo de **feed RSS 2.0** para sindicación de contenidos del aula.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Aula ASIX — Novedades</title>
    <link>https://example.com/</link>
    <description>Noticias y avisos del aula</description>
    <language>es-es</language>
    <lastBuildDate>Sun, 14 Sep 2025 14:04:26 +0200</lastBuildDate>
    <item>
      <title>Bienvenida y primeros pasos</title>
      <link>https://example.com/bienvenida</link>
      <description>Consulta el README del proyecto y entrega tu primer HTML validado.</description>
      <pubDate>Sun, 14 Sep 2025 14:04:26 +0200</pubDate>
      <guid isPermaLink="false">asix-20250914140426-1</guid>
    </item>
    <item>
      <title>Práctica XML + DTD + XSD</title>
      <link>https://example.com/practica-xml</link>
      <description>Valida el catálogo con DTD y XSD y genera HTML con XSLT.</description>
      <pubDate>Sun, 14 Sep 2025 14:04:26 +0200</pubDate>
      <guid isPermaLink="false">asix-20250914140426-2</guid>
    </item>
  </channel>
</rss>

```

!!! tip "Valida tu feed"
    Usa un validador de feeds para comprobar estructura y fechas.
