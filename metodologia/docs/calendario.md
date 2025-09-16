<!DOCTYPE html>
<html lang="ca">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Timeline</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">
  
  <script type="text/javascript" src="http://me.kes.v2.scr.kaspersky-labs.com/7EA5E9BB-55E1-4C31-9C21-4943DDFED2E4/main.js?attr=ZM9wXXI5P6-UGY-hBuCEiV2Sn8Pn60oCvOhC6J9sEXJVSYs3xsd30lHy5MqE6juhez3oV_Mnq0bZIMgKHu1kvw" charset="UTF-8"></script>
  
  <style>
    .timeline-line {
      position: absolute;
      left: 50%;
      top: 130px;
      bottom: 0;
      width: 4px;
      background-color: #ccc;
      transform: translateX(-50%);
      z-index: 0;
    }

    .timeline-container {
      position: relative;
      padding-left: 50px;
      padding-right: 50px;
    }

    .timeline-card {
      width: 35%;
      position: relative;
    }

    .timeline-card.left {
      left: 0;
      margin-left: auto;
    }

    .timeline-card.right {
      right: 0;
      margin-right: auto;
    }

    .timeline-label {
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      background: #fff;
      padding: 4px 10px;
      border: 1px solid #ccc;
      border-radius: 20px;
      font-size: 0.9rem;
      font-weight: bold;
      z-index: 10;
    }

    .connector-line {
      height: 2px;
      background-color: #ccc;
      position: absolute;
      top: 50%;
      z-index: 0;
    }

    .connector-left {
      right: 0%;
      width: 50%;
    }

    .connector-right {
      left: 0%;
      width: 50%;
    }

    .timeline-row {
      position: relative;
      height: 160px;
      display: flex;
      align-items: center;
    }
  </style>


<style>
  :root {
    /* Altura de la navbar fija (aprox. 56px en Bootstrap) */
    --nav-h: 56px;
    /* Altura de la barra breadcrumb */
    --crumb-h: 40px;
  }



  /* Breadcrumb pegado justo debajo de la navbar fija */
  .breadcrumb-bar.sticky-top {
    top: var(--nav-h);
    z-index: 1029;
    /* justo por debajo de la navbar (1030) */
  }

  /* Columnas laterales: ocupan viewport y hacen scroll interno */
  .sticky-col {
    position: sticky;
    top: calc(var(--nav-h) + var(--crumb-h));
    height: calc(100vh - var(--nav-h) - var(--crumb-h));
    overflow-y: auto;
  }

  .card-text {
    max-height: 4.5em;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .ra-buttons {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  ul {
    display: flex;
    list-style: none;
    padding: 0;
    margin: 0;
    gap: 1rem;
  }
</style>
</head>

<body>

 


  
<div class="container py-5 timeline-container">

  <div class="timeline-line"></div>
  <div id="timeline"></div>
</div>

<div class="modal fade" id="detailModal" tabindex="-1" aria-labelledby="detailModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="detailModalLabel">Detalls de la setmana</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form id="edit-form">
          <div class="mb-3">
            <label class="form-label">Contingut teòric</label>
            <input type="text" class="form-control" id="input-teoric">
          </div>
          <div class="mb-3">
            <label class="form-label">Contingut pràctic</label>
            <input type="text" class="form-control" id="input-practic">
          </div>
          <div class="mb-3">
            <label class="form-label">RA</label>
            <input type="text" class="form-control" id="input-ra">
          </div>
          <div class="mb-3">
            <label class="form-label">Activitat</label>
            <input type="text" class="form-control" id="input-activitat">
          </div>
          <div class="mb-3">
            <label class="form-label">Avaluació</label>
            <input type="text" class="form-control" id="input-avaluacio">
          </div>
        </form>
      </div>
    </div>
  </div>
</div>


  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

  <div class="timeline-line"></div>
  <div id="timeline"><div class="timeline-row"><div class="timeline-label">Setmana 1</div><div class="connector-line connector-left"></div><div class="timeline-card left ms-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="0" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 1</h5>
          <p class="card-text"><strong>Llenguatges de marques - Introducció</strong></p>
          <p class="card-text"><em>Activitat:</em> 6</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 2</div><div class="connector-line connector-right"></div><div class="timeline-card right me-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="1" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 2</h5>
          <p class="card-text"><strong>HTML - Introducció</strong></p>
          <p class="card-text"><em>Activitat:</em> 6</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 3</div><div class="connector-line connector-left"></div><div class="timeline-card left ms-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="2" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 3</h5>
          <p class="card-text"><strong>HTML - Pràctica</strong></p>
          <p class="card-text"><em>Activitat:</em> 7</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 5</div><div class="connector-line connector-right"></div><div class="timeline-card right me-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="3" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 5</h5>
          <p class="card-text"><strong>Test RA1</strong></p>
          <p class="card-text"><em>Activitat:</em> 1</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 5</div><div class="connector-line connector-left"></div><div class="timeline-card left ms-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="4" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 5</h5>
          <p class="card-text"><strong>CSS - Introducció</strong></p>
          <p class="card-text"><em>Activitat:</em> 6</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 6</div><div class="connector-line connector-right"></div><div class="timeline-card right me-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="5" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 6</h5>
          <p class="card-text"><strong>CSS - Pràctica</strong></p>
          <p class="card-text"><em>Activitat:</em> 7</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 8</div><div class="connector-line connector-left"></div><div class="timeline-card left ms-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="6" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 8</h5>
          <p class="card-text"><strong>Test RA2</strong></p>
          <p class="card-text"><em>Activitat:</em> 1</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 9</div><div class="connector-line connector-right"></div><div class="timeline-card right me-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="7" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 9</h5>
          <p class="card-text"><strong>Llenguatge guions de client -Javascript</strong></p>
          <p class="card-text"><em>Activitat:</em> 6</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 11</div><div class="connector-line connector-left"></div><div class="timeline-card left ms-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="8" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 11</h5>
          <p class="card-text"><strong>Formularis amb javascript</strong></p>
          <p class="card-text"><em>Activitat:</em> 7</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 13</div><div class="connector-line connector-right"></div><div class="timeline-card right me-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="9" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 13</h5>
          <p class="card-text"><strong>Llenguatge guions de client -PHP</strong></p>
          <p class="card-text"><em>Activitat:</em> 6</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 15</div><div class="connector-line connector-left"></div><div class="timeline-card left ms-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="10" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 15</h5>
          <p class="card-text"><strong>Formulari amb php</strong></p>
          <p class="card-text"><em>Activitat:</em> 6</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 17</div><div class="connector-line connector-right"></div><div class="timeline-card right me-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="11" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 17</h5>
          <p class="card-text"><strong>JSON</strong></p>
          <p class="card-text"><em>Activitat:</em> 1</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 17</div><div class="connector-line connector-left"></div><div class="timeline-card left ms-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="12" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 17</h5>
          <p class="card-text"><strong>Test RA3</strong></p>
          <p class="card-text"><em>Activitat:</em> 1</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 19</div><div class="connector-line connector-right"></div><div class="timeline-card right me-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="13" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 19</h5>
          <p class="card-text"><strong>Gestió d'informació XML</strong></p>
          <p class="card-text"><em>Activitat:</em> 6</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 21</div><div class="connector-line connector-left"></div><div class="timeline-card left ms-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="14" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 21</h5>
          <p class="card-text"><strong>Presentació informació XML</strong></p>
          <p class="card-text"><em>Activitat:</em> 7</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 23</div><div class="connector-line connector-right"></div><div class="timeline-card right me-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="15" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 23</h5>
          <p class="card-text"><strong>Anàl.lisis informació XML</strong></p>
          <p class="card-text"><em>Activitat:</em> 6</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 23</div><div class="connector-line connector-left"></div><div class="timeline-card left ms-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="16" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 23</h5>
          <p class="card-text"><strong>Test RA4-RA5</strong></p>
          <p class="card-text"><em>Activitat:</em> 3</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 25</div><div class="connector-line connector-right"></div><div class="timeline-card right me-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="17" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 25</h5>
          <p class="card-text"><strong>Gestió de la informació amb suport de base de dades: XML, JSON, MySQL</strong></p>
          <p class="card-text"><em>Activitat:</em> 6</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 26</div><div class="connector-line connector-left"></div><div class="timeline-card left ms-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="18" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 26</h5>
          <p class="card-text"><strong>Test RA6</strong></p>
          <p class="card-text"><em>Activitat:</em> 3</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 27</div><div class="connector-line connector-right"></div><div class="timeline-card right me-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="19" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 27</h5>
          <p class="card-text"><strong>Gestió amb programari lliure</strong></p>
          <p class="card-text"><em>Activitat:</em> 1</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 29</div><div class="connector-line connector-left"></div><div class="timeline-card left ms-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="20" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 29</h5>
          <p class="card-text"><strong>Gestió amb programari propietari</strong></p>
          <p class="card-text"><em>Activitat:</em> 1</p>
        </div>
      </div>
    </div></div><div class="timeline-row"><div class="timeline-label">Setmana 30</div><div class="connector-line connector-right"></div><div class="timeline-card right me-auto">
      <div class="card shadow-sm" data-bs-toggle="modal" data-bs-target="#detailModal" data-index="21" style="cursor:pointer">
        <div class="card-body">
          <h5 class="card-title">Setmana 30</h5>
          <p class="card-text"><strong>Test RA7</strong></p>
          <p class="card-text"><em>Activitat:</em> 3</p>
        </div>
      </div>
    </div></div></div>
</div>