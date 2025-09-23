<a name="ds-genericmetadatajson"> </a>

# Generic Glottography dataset derived from Rantanen et al. 2021 "Geographical database of the Uralic languages"

**CLDF Metadata**: [Generic-metadata.json](./Generic-metadata.json)

**Sources**: [sources.bib](./sources.bib)

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Rantanen, T., Vesakoski, O., Ylikoski, J., & Tolvanen, H. (2021). Geographical database of the Uralic languages (v1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4784188
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Generic](http://cldf.clld.org/v1.0/terms.rdf#Generic)
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/4.0/
[dc:spatial](http://purl.org/dc/terms/spatial) | westlimit=9.5; southlimit=52.1; eastlimit=113.5; northlimit=75.7
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/Glottography/rantanen2021uralic
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/Glottography/rantanen2021uralic/tree/d9f9e15">Glottography/rantanen2021uralic d9f9e15</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v5.2">Glottolog v5.2</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.12.3</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | rantanen2021uralic
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-mediacsv"></a>Table [media.csv](./media.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF MediaTable](http://cldf.clld.org/v1.0/terms.rdf#MediaTable)
[dc:extent](http://purl.org/dc/terms/extent) | 3


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Media_Type](http://cldf.clld.org/v1.0/terms.rdf#mediaType) | `string`<br>Regex: `[^/]+/.+` | 
[Download_URL](http://cldf.clld.org/v1.0/terms.rdf#downloadUrl) | `anyURI` | 
[Path_In_Zip](http://cldf.clld.org/v1.0/terms.rdf#pathInZip) | `string` | 

## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 42


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal`<br>&ge; -90<br>&le; 90 | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal`<br>&ge; -180<br>&le; 180 | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string`<br>Regex: `[a-z0-9]{4}[1-9][0-9]{3}` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string`<br>Regex: `[a-z]{3}` | 
[Feature_IDs](http://cldf.clld.org/v1.0/terms.rdf#contributionReference) | list of `string` (separated by ` `) | List of identifiers of features that were aggregated to create the feature referenced by Speaker_Area.<br>References [contributions.csv::ID](#table-contributionscsv)
`Glottolog_Languoid_Level` | `string`<br>Valid choices:<br> `dialect` `language` `family` | https://glottolog.org/meta/glossary#Languoid
`Family` | `string` | Name of the top-level family for the languoid in the Glottolog classification. A null value in this column marks 1) top-level families in case Glottolog_Languoid_Level is 'family' and 2) isolates in case Glottolog_Languoid_Level is 'language'.
[Speaker_Area](http://cldf.clld.org/v1.0/terms.rdf#speakerArea) | `string` | References [media.csv::ID](#table-mediacsv)

## <a name="table-contributionscsv"></a>Table [contributions.csv](./contributions.csv)

We list the individual features from the source dataset as contributions in order to preserve the original metadata and a point of reference for the aggregated shapes.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ContributionTable](http://cldf.clld.org/v1.0/terms.rdf#ContributionTable)
[dc:extent](http://purl.org/dc/terms/extent) | 382


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Contributor](http://cldf.clld.org/v1.0/terms.rdf#contributor) | `string` | 
[Citation](http://cldf.clld.org/v1.0/terms.rdf#citation) | `string` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string`<br>Regex: `[a-z0-9]{4}[1-9][0-9]{3}` | References a Glottolog languoid most closely matching the linguistic entity described by the feature.
[Year](http://purl.org/dc/terms/temporal) | `string`<br>Regex: `[0-9]{3,4}|traditional` | The time period to which the feature relates, specified as year AD or with the keyword 'traditional', meaning either the time of contact with European maritime powers or period when an ancient language was spoken.
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)
[Media_IDs](http://cldf.clld.org/v1.0/terms.rdf#mediaReference) | list of `string` (separated by ` `) | Contributions of type 'feature' are linked to GeoJSON files that store the geo data.  can be related to various kinds of media. Contributions of type 'map' are linked to the corresponding scans of maps and geo-data derived from these.<br>References [media.csv::ID](#table-mediacsv)
`Type` | `string`<br>Valid choices:<br> `map` `feature` | There are two types of contributions: Individual geo-features as depicted in the source and images of maps.
[Map_IDs](http://cldf.clld.org/v1.0/terms.rdf#contributionReference) | list of `string` (separated by ` `) | Contributions of type 'feature' link to the maps on which they appear.<br>References [contributions.csv::ID](#table-contributionscsv)

