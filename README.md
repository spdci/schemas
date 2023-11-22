# SPDCI Interoperability Schemas

## Enhancing Interoperability Between CRVS and Social Protection Systems with JSON-LD

JSON-LD (JavaScript Object Notation for Linking Data) is a pivotal component in facilitating the interoperability between systems. This repository contains schema definitions using JSON-LD, designed to ensure seamless data integration and communication across diverse platforms and systems.

### Why JSON-LD for SPDCI?
JSON-LD extends the standard JSON format to include linked data, allowing for more expressive and interconnected data representations. This feature is particularly beneficial in complex environments like CRVS and social protection systems, where data consistency and universal understanding are paramount.

### Example: JSON-LD in Action
Below is a practical example of how our JSON-LD schema represents a CRVS entity. This schema encapsulates key identifiers, personal information, and relational data in a structured, web-scale interoperable format:

```json
{
    "@context": {
      "@vocab": "http://spdci.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "schema": "http://schema.org/",
      "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
      "owl": "http://www.w3.org/2002/07/owl#"
    },
    "@id": "spdci:CRVS_Person_2",
    "@type": "spdci:CRVS_Person",
    "identifier": "UIN:789456",
    "name": {
        "@type": "spdci:Name",
        "given_name": "Sudarat",
        "sur_name": "Phumchai"
    },
    "phone_number": "+66 891 234567",
    "email": "sudarat.phumchai@example.com",
    "sex": "spdci:Female",
    "birthdate": "1985-06-10T00:00:00",
    "birthplace": "Phumchai_Village_Clinic",
    "address": {
        "@type": "spdci:Place",
        "address": "45, Rural Road, Phumchai Village",
        "geo": {
            "@type": "spdci:GeoCoordinates",
            "latitude": "18.775632",
            "longitude": "98.985524"
        },
        "containedInPlace": "Place_2",
    },
    "marital_status": "spdci:Married",
    "marriagedate": "2010-04-20T00:00:00"
}
```

### Dive Deeper
- For an in-depth understanding of how these schemas work, visit our [documentation page](https://standards.spdci.org/standards/standards/1.-crvs/6.5-data-standards).
- To see these schemas in action, try out our interactive examples in the [JSON-LD Playground](https://json-ld.org/playground/).

### Community and Contributions
We welcome contributions, ideas, and feedback from the community. To contribute or report issues, please follow our [contribution guidelines](https://github.com/spdci).
