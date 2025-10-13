# CSS – Pràctica (Activitat 4)

## Continuació del projecte: El diari digital

> Aquesta quarta activitat continua el projecte **“El Diari Digital”**, mantenint el fil conductor sobre com un mitjà digital pot estructurar, presentar i distribuir informació a la web.  
> En aquesta etapa ens centrarem en la **consolidació de CSS**, la **validació dels documents HTML i CSS**, i la **creació d’un sistema de sindicació (RSS)** que permet compartir notícies automàticament.

---

## Aplicació avançada de fulles d’estil (CSS)

Després d’aprendre els fonaments del CSS, ara aplicarem conceptes més avançats per donar al nostre diari un **disseny professional, net i adaptable**.

### Conceptes clau

- **Jerarquia visual:** utilitza colors, tipografies i espais per guiar la lectura.  
- **Reutilització d’estils:** mitjançant classes i fulls externs.  
- **Disseny modular:** separar estils per seccions (capçalera, cos, peu, etc.).  
- **Coherència cromàtica i tipogràfica:** manté la identitat visual del diari.  
- **Resposivitat:** adaptar el contingut a dispositius mòbils.

!!! tip "Exemples de jerarquía"
    - [UOC](https://design-toolkit.recursos.uoc.edu/jerarquia/) Ampliació de la jerarquia i altres temes relacionats


### Exemple pràctic

```css
/* styles.css */
body {
  font-family: 'Open Sans', sans-serif;
  background-color: #fafafa;
  margin: 0;
  color: #333;
}

header {
  background-color: #0a3d62;
  color: white;
  text-align: center;
  padding: 1rem;
}

nav ul {
  display: flex;
  justify-content: center;
  list-style: none;
  background: #3c6382;
  padding: 0;
}

nav ul li {
  margin: 0 1rem;
}

nav ul li a {
  color: white;
  text-decoration: none;
}

article {
  background: white;
  margin: 1rem auto;
  padding: 1rem;
  width: 80%;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

**Activitat 1:**

1. Crea una estructura HTML amb `<header>`, `<nav>`, `<main>` i `<footer>`.  
2. Aplica estils CSS per diferenciar visualment cada secció.  
3. Afegeix una llista de notícies amb classes `.principal` i `.secundaria` amb estils diferenciats.

---

## Validació d’HTML i CSS

La validació és un procés essencial per garantir que el codi del diari **segueixi els estàndards web** i sigui **accessible i interoperable**.

### Objectius de la validació

- **Detectar errors** de sintaxi o estructura.  
- **Millorar la compatibilitat** entre navegadors.  
- **Assegurar l’accessibilitat** per a tots els usuaris.  
- **Evitar problemes de SEO** relacionats amb HTML invàlid.

### Eines de validació

| Eina | Tipus | Ús principal |
|------|-------|---------------|
| [W3C Markup Validator](https://validator.w3.org/) | HTML | Comprovar estructura i tancament d’etiquetes |
| [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) | CSS | Comprovar propietats i sintaxi |
| [Wave Accessibility Tool](https://wave.webaim.org/) | Accessibilitat | Analitzar compatibilitat amb lectors de pantalla |
| **Inspectors del navegador** | HTML/CSS | Revisar errors visuals i regles aplicades |

**Activitat 2:**

1. Valida el teu `index.html` amb el [W3C Markup Validator](https://validator.w3.org/).  
2. Valida el teu `styles.css` amb el [CSS Validator](https://jigsaw.w3.org/css-validator/).  
3. Corregeix els errors detectats i documenta les modificacions.  
4. Revisa la compatibilitat visual en Chrome, Firefox i Edge.

---

## Llenguatges de marques per a la sindicació de continguts

Els **llenguatges de marques per a sindicació** permeten que altres llocs web o aplicacions **rebin automàticament les actualitzacions** del nostre diari. El més utilitzat és **RSS (Really Simple Syndication)**.

### Característiques principals

- Basat en **XML**.  
- Conté **elements estructurats** com `<channel>` i `<item>`.  
- Facilita la **distribució automàtica de notícies**.  
- Pot integrar-se en agregadors, aplicacions o altres webs.

### Exemple d’un feed RSS per al Diari Digital

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
  <channel>
    <title>El Diari Digital</title>
    <link>https://www.eldiari.cat</link>
    <description>Últimes notícies i articles d'opinió</description>
    <language>ca</language>

    <item>
      <title>Nova secció d’esports</title>
      <link>https://www.eldiari.cat/esports/nova-seccio</link>
      <description>El diari estrena avui una secció dedicada a l’esport català.</description>
      <pubDate>Tue, 15 Oct 2025 10:00:00 GMT</pubDate>
    </item>

  </channel>
</rss>
```

**Activitat 3:**  

1. Crea un fitxer `feed.xml` amb un mínim de **tres notícies** del teu diari.  
2. Inclou títol, descripció, enllaç i data de publicació per a cada notícia.  
3. Valida el teu fitxer XML en un validador en línia.  
4. Afegeix un enllaç al `feed.xml` des del peu de pàgina del teu `index.html`.

---

## Síntesi final

Aquesta activitat t’ha permès:

- Consolidar l’ús de **CSS avançat** per millorar la presentació del diari.  
- Validar la qualitat del teu codi HTML i CSS.  
- Crear un sistema de **sindicació RSS** per compartir continguts automàticament.  

Tot això reforça la idea que un **diari digital complet** necessita no només contingut i disseny, sinó també **estructura, compatibilitat i distribució eficient**.

---

!!! tip "Idea clau final"
    Un diari digital professional combina un codi validat, un disseny coherent i un sistema de difusió intel·ligent. L’ús correcte de CSS i RSS és essencial per a la seva visibilitat i manteniment en l’ecosistema web.

## Pràctica final  **CSS Grid Layout**

Abans de fer el disseny *responsive* del Diari Digital, és important entendre una de les eines més potents del CSS modern: **Grid Layout**.
El sistema **Grid** permet organitzar el contingut en files i columnes amb una flexibilitat molt més gran que `float`, `inline-block` o `flexbox` quan es tracta de dissenys de pàgina.

---

### 1. Què és un grid?

Un **grid** (graella) és un *contenidor* que divideix l’espai disponible en una sèrie de **files (rows)** i **columnes (columns)**.
Els elements dins del contenidor es col·loquen automàticament en aquestes cel·les o bé manualment amb coordenades (`grid-row`, `grid-column`).

```css
.container {
  display: grid;
  grid-template-columns: 200px 1fr 1fr;
  grid-template-rows: auto auto;
  gap: 1rem;
}
```

En aquest exemple:

* `display: grid` activa el mode graella.
* `grid-template-columns` defineix **tres columnes**: la primera fixa (200px) i dues flexibles (`1fr` cadascuna).
* `gap` estableix l’espai entre files i columnes.

---

### 2. Conceptes bàsics

| Termini            | Significat                                          |
| ------------------ | --------------------------------------------------- |
| **Grid container** | L’element pare que conté el grid (`display: grid;`) |
| **Grid items**     | Els elements fills directes del container           |
| **Grid lines**     | Línies numerades que delimiten les files i columnes |
| **Track**          | L’espai entre dues línies (una fila o una columna)  |
| **Cell**           | Una cel·la individual dins la graella               |
| **Area**           | Una zona que pot ocupar diverses cel·les contigües  |

---

### 3. Mesures útils

- **`fr`** (*fractional unit*): reparteix espai disponible de forma proporcional.
  Ex.: `grid-template-columns: 2fr 1fr;` → la primera columna ocupa el doble que la segona.
- **`auto`**: mida segons el contingut.
- **`minmax(min, max)`**: limita el creixement d’una cel·la.
  Ex.: `minmax(200px, 1fr)` → mai menys de 200px, però pot créixer fins a 1fr.

---

### 4. Distribucions habituals

**a) Dues columnes (principal + lateral):**

```css
.grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 1rem;
}
```

**b) Tres columnes iguals:**

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
```

**c) Distribució responsive automàtica:**

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}
```

Aquesta forma és molt útil per fer que els elements s’ajustin automàticament a la mida de la pantalla sense definir punts de tall concrets.

---

### 5. Col·locació manual d’elements

Cada element fill pot ocupar diverses files o columnes:

```css
.item1 {
  grid-column: 1 / 3;   /* ocupa de la línia 1 a la 3 → 2 columnes */
  grid-row: 1 / 2;
}
```

---

### 6. Grid vs Flexbox

| **Grid**                                                   | **Flexbox**                                           |
| ---------------------------------------------------------- | ----------------------------------------------------- |
| Pensat per **disposició bidimensional** (files + columnes) | Pensat per **una sola direcció** (fila **o** columna) |
| Ideal per al **layout global** de la pàgina                | Ideal per al **contingut intern** d’un bloc o secció  |
| Permet alineació en dues dimensions                        | Només alinea en una direcció principal                |

> En molts dissenys s’utilitzen **tots dos**: *Grid* per estructurar la pàgina i *Flexbox* per ordenar els elements dins de cada secció.

---

### 7. Exercici bàsic

Crea una petita maqueta de 6 targetes de notícies en 3 columnes:

```html
<section class="grid-demo">
  <article>Notícia 1</article>
  <article>Notícia 2</article>
  <article>Notícia 3</article>
  <article>Notícia 4</article>
  <article>Notícia 5</article>
  <article>Notícia 6</article>
</section>
```

```css
.grid-demo {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}
.grid-demo article {
  background: #f1f2f6;
  padding: 1rem;
  border-radius: .5rem;
}
```

📱 Prova d’afegir `auto-fit` o `minmax()` per veure com es reordenen en pantalles petites.

---

### 8. Objectius del bloc

- Comprendre la sintaxi i lògica de **Grid Layout**.
- Saber definir **files i columnes flexibles**.
- Utilitzar `fr`, `repeat()`, `auto-fit` i `minmax()`.
- Preparar la maqueta del *Diari Digital* per adaptar-la posteriorment amb **media queries**.

---

## Disseny responsive amb **Media Queries**

En aquest bloc aprendràs a adaptar el *Diari Digital* a diferents amplades de pantalla utilitzant **media queries**. Treballarem amb un enfoc **mobile-first** i definirem punts de tall per a mòbil, tablet i escriptori.

### Objectius

* Entendre la sintaxi de `@media` i el concepte de **mobile-first**.
* Dissenyar una **graella** que canviï de columnes segons la mida de pantalla.
* Fer que la **navegació** i els **articles** siguin llegibles i usables en dispositius petits.
* Assegurar que imatges, tipografia i espais s’adaptin fluidament.

### Punts de tall recomanats

* **Mòbil**: ≤ **767px**
* **Tablet**: **768–1023px**
* **Escriptori**: ≥ **1024px**

> Pots ajustar aquests valors si el teu disseny ho demana; l’important és que hi hagi coherència entre trencaments.

### Guia ràpida (mobile-first)

1. **Base (mòbil per defecte)** – Estils globals sense media queries.
2. **Tablet** – Afina distribució i tipografies a partir de 768px.
3. **Escriptori** – Amplia graelles i marges a partir de 1024px.

### Exemple de codi

```css
/* 1) Base: mòbil (mobile-first) */
:root{
  --space-1: .5rem;
  --space-2: 1rem;
  --space-3: 1.5rem;
  --maxw: 1200px;
}

/* Tipografia fluida */
html { font-size: clamp(15px, 2.2vw, 18px); }

body{
  font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
  margin: 0;
  color: #222;
  background: #fafafa;
}

header, footer{
  padding: var(--space-2);
  background: #0a3d62;
  color: #fff;
  text-align: center;
}

/* Navegació: pila vertical al mòbil */
nav ul{
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: var(--space-1);
}
nav a{
  display: block;
  padding: .6rem .8rem;
  background: #3c6382;
  color: #fff;
  text-decoration: none;
  border-radius: .5rem;
}

/* Contingut principal en una sola columna al mòbil */
main{
  width: min(92%, var(--maxw));
  margin: var(--space-2) auto;
}
.grid-noticies{
  display: grid;
  grid-template-columns: 1fr;         /* 1 col mòbil */
  gap: var(--space-2);
}
article{
  background: #fff;
  padding: var(--space-2);
  border-radius: .6rem;
  box-shadow: 0 1px 3px rgba(0,0,0,.08);
}
article img{
  max-width: 100%;
  height: auto;
  display: block;
  border-radius: .4rem;
  margin-block: .5rem;
}

/* 2) Tablet ≥768px */
@media (min-width: 768px){
  nav ul{
    grid-auto-flow: column;
    grid-auto-columns: 1fr;           /* menú en fila, botons fluids */
  }
  .grid-noticies{
    grid-template-columns: 1.2fr 1fr; /* 2 columnes: principal + lateral */
  }
  .llista-secundaries{
    display: grid;
    grid-template-columns: 1fr 1fr;   /* subgrid dins la columna lateral */
    gap: var(--space-2);
  }
}

/* 3) Escriptori ≥1024px */
@media (min-width: 1024px){
  main{ width: min(86%, var(--maxw)); }
  .grid-noticies{
    grid-template-columns: 2fr 1fr 1fr; /* 3 columnes: portada + dues secundàries */
  }
  nav ul{
    justify-content: center;
    gap: var(--space-2);
  }
  article{ padding: var(--space-3); }
}
```

### Estructura HTML orientativa

```html
<header>
  <h1>El Diari Digital</h1>
</header>

<nav>
  <ul>
    <li><a href="#">Portada</a></li>
    <li><a href="#">Actualitat</a></li>
    <li><a href="#">Esports</a></li>
    <li><a href="#">Cultura</a></li>
  </ul>
</nav>

<main>
  <section class="grid-noticies">
    <article class="principal">
      <h2>Títol principal</h2>
      <img src="img/portada.jpg" alt="Imatge notícia principal">
      <p>Resum de la notícia principal…</p>
    </article>

    <aside class="llista-secundaries">
      <article class="secundaria">
        <h3>Notícia 1</h3>
        <p>Extracte…</p>
      </article>
      <article class="secundaria">
        <h3>Notícia 2</h3>
        <p>Extracte…</p>
      </article>
      <article class="secundaria">
        <h3>Notícia 3</h3>
        <p>Extracte…</p>
      </article>
      <article class="secundaria">
        <h3>Notícia 4</h3>
        <p>Extracte…</p>
      </article>
    </aside>
  </section>
</main>

<footer>
  <small>&copy; 2025 El Diari Digital — <a href="feed.xml">RSS</a></small>
</footer>
```

---

### Activitat 4: *Responsive complet del Diari Digital*

1. **Mobile-first:** ajusta els estils base perquè el lloc es vegi perfecte a mòbil (una sola columna, navegació apilada, imatges fluides).
2. **Tablet (≥768px):** reestructura el *layout* a dues columnes i converteix el menú en fila.
3. **Escriptori (≥1024px):** crea una graella de tres columnes (portada + 2 secundàries).
4. **Tipografia fluida:** aplica `clamp()` per al `font-size` del `<html>` i revisa line-height i marges.
5. **Imatges i media:** assegura `max-width: 100%` i proves amb diferents proporcions.
6. **Accessibilitat i focus:** comprova contrastos i estats `:focus-visible` en enllaços del menú.
7. **Validació i proves:** valida HTML/CSS i comprova el resultat amb les *devtools* (mòbils populars).
8. **Documenta** els punts de tall triats i el perquè (2–4 frases).

**Entrega:**

* Codi HTML/CSS actualitzat.
* 3 captures (mòbil, tablet, escriptori) del mateix article de portada.
* Fitxer `README_responsive.md` breu amb decisions i punts de tall.

### (Opcional) Reptes extra

* **Sticky header** amb *scroll shadow* només a partir de 768px.
* **Cards equilibrades**: limita el nombre de línies del titular amb `line-clamp` (si ho prefereixes, amb una classe utilitària).
* **Dark mode** respectant `@media (prefers-color-scheme: dark)`.

### Rúbrica d’avaluació (10 punts)

* **Estructura responsive** (3p): canvis coherents entre punts de tall.
* **Llegibilitat** (2p): tipografia, espaiat, contrast.
* **Imatges/multimèdia fluids** (1.5p).
* **Navegació usable** (1.5p): focus, ordre, tacte en mòbil.
* **Validació i documentació** (2p): W3C ok i README clar.