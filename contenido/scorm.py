#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Convierte una web generada con MkDocs (carpeta 'site') en un paquete SCORM 1.2 sencillo.

Aproximación 1: solo contenido, se marca como COMPLETED al abrir el SCO.

CONFIGURACIÓN:
- Ajusta MKDOCS_SITE_DIR al directorio generado por `mkdocs build`
- Ajusta OUTPUT_ZIP al nombre del paquete SCORM resultante
- Rellena ENTRY_POINTS con los puntos de entrada al material
"""

import os
import shutil
import zipfile
from pathlib import Path

# === CONFIGURACIÓN BÁSICA ===

# Carpeta donde MkDocs genera el sitio estático
MKDOCS_SITE_DIR = "site"

# Nombre del ZIP SCORM de salida
OUTPUT_ZIP = "lenguajeMarcas.zip"

# Identificador y título del curso SCORM
COURSE_ID = "lenguajeMarcas"
COURSE_TITLE = "Lenguaje Marcas"

# Puntos de entrada al material (tú los rellenas)
# 'html' debe ser la ruta RELATIVA dentro de MKDOCS_SITE_DIR
ENTRY_POINTS = [
    {
        "id": "SCO1",
        "title": "html",
        "html": "html/index.html",  # por ejemplo: "index.html" o "tema1/index.html"
    },
    # Puedes añadir más:
    # {"id": "SCO2", "title": "Tema 1", "html": "tema1/index.html"},
]


# === TEMPLATES DE ARCHIVOS ===

SCORM_API_JS = r"""// scorm_api.js - Wrapper SCORM 1.2 muy sencillo

var ScormAPI = (function () {
    var api = null;
    var initialized = false;
    var finished = false;

    function findAPIInWindow(win) {
        var maxDepth = 10;
        var depth = 0;
        while (win && depth < maxDepth) {
            try {
                if (win.API) {
                    return win.API;
                }
            } catch (e) {}
            if (win.parent === win) {
                break;
            }
            win = win.parent;
            depth++;
        }
        return null;
    }

    function getAPIHandle() {
        if (api !== null) {
            return api;
        }
        api = findAPIInWindow(window);
        if (api === null && window.opener) {
            api = findAPIInWindow(window.opener);
        }
        return api;
    }

    function init() {
        if (initialized) return true;
        var theAPI = getAPIHandle();
        if (!theAPI || !theAPI.LMSInitialize) {
            console.warn("No se encontró API SCORM 1.2");
            return false;
        }
        var result = theAPI.LMSInitialize("");
        if (result === "true") {
            initialized = true;
            return true;
        } else {
            console.warn("LMSInitialize devolvió", result);
            return false;
        }
    }

    function finish() {
        if (!initialized || finished) return true;
        var theAPI = getAPIHandle();
        if (!theAPI || !theAPI.LMSFinish) return false;
        var result = theAPI.LMSFinish("");
        finished = (result === "true");
        return finished;
    }

    function setValue(element, value) {
        var theAPI = getAPIHandle();
        if (!theAPI || !theAPI.LMSSetValue) return false;
        var result = theAPI.LMSSetValue(element, value);
        return (result === "true");
    }

    function commit() {
        var theAPI = getAPIHandle();
        if (!theAPI || !theAPI.LMSCommit) return false;
        var result = theAPI.LMSCommit("");
        return (result === "true");
    }

    return {
        init: init,
        finish: finish,
        set: setValue,
        commit: commit
    };
})();
"""

LAUNCH_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="scorm_api.js"></script>
    <style>
        html, body {{
            margin: 0;
            padding: 0;
            height: 100%;
        }}
        .container {{
            box-sizing: border-box;
            height: 100%;
            width: 100%;
        }}
        .header {{
            font-family: sans-serif;
            font-size: 14px;
            padding: 6px 10px;
            background: #f2f2f2;
            border-bottom: 1px solid #ccc;
        }}
        .content {{
            width: 100%;
            height: calc(100% - 32px);
        }}
        iframe {{
            width: 100%;
            height: 100%;
            border: none;
        }}
    </style>
    <script>
        // Inicializa SCORM y marca COMPLETED al cargar la página
        window.onload = function () {{
            var ok = ScormAPI.init();
            if (ok) {{
                // Marcamos el SCO como completado
                ScormAPI.set("cmi.core.lesson_status", "completed");
                ScormAPI.commit();
            }}
        }};

        // Finaliza la sesión SCORM al salir
        window.onbeforeunload = window.onunload = function () {{
            ScormAPI.finish();
        }};
    </script>
</head>
<body>
    <div class="container">
        <div class="header">
            {title} (SCORM)
        </div>
        <div class="content">
            <iframe src="{content_src}" title="{title}"></iframe>
        </div>
    </div>
</body>
</html>
"""

def generate_manifest(build_root: Path, course_id: str, course_title: str, sco_defs):
    """
    Crea imsmanifest.xml en build_root.
    sco_defs: lista de dicts con keys:
        - item_id
        - resource_id
        - launch_href
        - title
    """
    manifest_path = build_root / "imsmanifest.xml"

    org_items_xml = []
    resources_xml = []

    org_id = "ORG-1"

    for sco in sco_defs:
        org_items_xml.append(f"""      <item identifier="{sco['item_id']}" identifierref="{sco['resource_id']}" isvisible="true">
        <title>{sco['title']}</title>
      </item>""")

        resources_xml.append(f"""    <resource identifier="{sco['resource_id']}" type="webcontent" adlcp:scormtype="sco" href="{sco['launch_href']}">
      <file href="{sco['launch_href']}"/>
    </resource>""")

    org_items_str = "\n".join(org_items_xml)
    resources_str = "\n".join(resources_xml)

    manifest_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{course_id}" version="1.0"
  xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd
    http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">

  <organizations default="{org_id}">
    <organization identifier="{org_id}">
      <title>{course_title}</title>
{org_items_str}
    </organization>
  </organizations>

  <resources>
{resources_str}
  </resources>
</manifest>
"""
    manifest_path.write_text(manifest_xml, encoding="utf-8")
    print(f"[OK] imsmanifest.xml generado en {manifest_path}")


def zip_dir(folder: Path, zip_filename: Path):
    """Comprime folder en zip_filename (paths relativos)."""
    if zip_filename.exists():
        zip_filename.unlink()
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(folder):
            root_path = Path(root)
            for fname in files:
                fpath = root_path / fname
                relpath = fpath.relative_to(folder)
                zf.write(fpath, relpath)
    print(f"[OK] Paquete SCORM creado: {zip_filename}")


def main():
    mkdocs_site = Path(MKDOCS_SITE_DIR).resolve()
    if not mkdocs_site.exists():
        raise SystemExit(f"No se encuentra la carpeta MkDocs '{mkdocs_site}'")

    build_root = Path("scorm_build").resolve()

    # Limpiamos build_root si existe
    if build_root.exists():
        shutil.rmtree(build_root)
    build_root.mkdir(parents=True, exist_ok=True)

    # 1) Copiar el sitio MkDocs dentro de build_root/site
    target_site = build_root / "site"
    shutil.copytree(mkdocs_site, target_site)
    print(f"[OK] Sitio MkDocs copiado a {target_site}")

    # 2) Escribir scorm_api.js en la raíz
    (build_root / "scorm_api.js").write_text(SCORM_API_JS, encoding="utf-8")
    print(f"[OK] scorm_api.js creado en {build_root}")

    # 3) Crear páginas de lanzamiento (wrappers) para cada punto de entrada
    sco_defs = []
    for idx, ep in enumerate(ENTRY_POINTS, start=1):
        item_id = f"ITEM-{ep['id']}"
        resource_id = f"RES-{ep['id']}"
        launch_name = f"launch_{ep['id'].lower()}.html"

        launch_path = build_root / launch_name

        # Ruta al HTML de MkDocs desde el root del paquete SCORM
        # (hemos copiado el sitio en build_root/site)
        content_src = f"site/{ep['html']}"

        html = LAUNCH_TEMPLATE.format(
            title=ep["title"],
            content_src=content_src
        )
        launch_path.write_text(html, encoding="utf-8")
        print(f"[OK] Página de lanzamiento creada: {launch_path} -> {content_src}")

        sco_defs.append({
            "item_id": item_id,
            "resource_id": resource_id,
            "launch_href": launch_name,
            "title": ep["title"],
        })

    # 4) Generar imsmanifest.xml
    generate_manifest(build_root, COURSE_ID, COURSE_TITLE, sco_defs)

    # 5) Comprimir todo en un ZIP SCORM
    zip_path = Path(OUTPUT_ZIP).resolve()
    zip_dir(build_root, zip_path)


if __name__ == "__main__":
    main()
