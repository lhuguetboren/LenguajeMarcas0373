# XML + DTD + XSD

**Bien formado** vs **válido**, y definición de **esquema (XSD)**.

=== "XML"
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE catalogo SYSTEM "catalogo.dtd">
<catalogo xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:noNamespaceSchemaLocation="catalogo.xsd">
  <curso id="ASIX1">
    <nombre>ASIX 1</nombre>
    <modulos>
      <modulo codigo="LMSGI" horas="132">Lenguajes de marcas y sistemas de gestión de información</modulo>
      <modulo codigo="ISO" horas="132">Implantación de sistemas operativos</modulo>
      <modulo codigo="BD" horas="165">Bases de datos</modulo>
    </modulos>
  </curso>
  <curso id="ASIX2">
    <nombre>ASIX 2</nombre>
    <modulos>
      <modulo codigo="SR" horas="132">Servicios de red e Internet</modulo>
      <modulo codigo="ASO" horas="99">Administración de sistemas operativos</modulo>
      <modulo codigo="SAD" horas="132">Seguridad y alta disponibilidad</modulo>
    </modulos>
  </curso>
</catalogo>

    ```

=== "DTD"
    ```dtd
    <!ELEMENT catalogo (curso+)>
<!ELEMENT curso (nombre, modulos)>
<!ATTLIST curso id ID #REQUIRED>

<!ELEMENT nombre (#PCDATA)>
<!ELEMENT modulos (modulo+)>
<!ELEMENT modulo (#PCDATA)>
<!ATTLIST modulo
  codigo CDATA #REQUIRED
  horas CDATA #IMPLIED>

    ```

=== "XSD"
    ```xsd
    <?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">
  <xs:element name="catalogo">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="curso" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="nombre" type="xs:string"/>
              <xs:element name="modulos">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="modulo" maxOccurs="unbounded">
                      <xs:complexType mixed="true">
                        <xs:attribute name="codigo" type="xs:string" use="required"/>
                        <xs:attribute name="horas" type="xs:positiveInteger" use="optional"/>
                      </xs:complexType>
                    </xs:element>
                  </xs:sequence>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="required"/>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>

    ```

!!! exercise "Actividad"
    Introduce un nuevo `curso` y un `modulo` con atributos `codigo` y `horas`. Valida con DTD y XSD.
