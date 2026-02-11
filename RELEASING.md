# Releasing the dataset

## Recreate the data extracted from the source

```shell
cldfbench download cldfbench_rantanen2021uralic.py
```

## Recreate the CLDF dataset

```shell
cldfbench makecldf cldfbench_rantanen2021uralic.py --glottolog-version v5.2
cldfbench cldfreadme cldfbench_rantanen2021uralic.py
cldfbench zenodo --communities glottography cldfbench_rantanen2021uralic.py
cldfbench readme cldfbench_rantanen2021uralic.py
```


## Validation

```shell
cldf validate cldf
```

```shell
cldfbench geojson.validate cldf
109     valid features
50      valid speaker areas
```

```shell
cldfbench geojson.glottolog_distance cldf --glottolog-version v5.2 --format tsv | csvformat -t | csvgrep -c Distance -r"^0\.?" -i | csvsort -c Distance | csvcut -c ID,Distance | csvformat -E | termgraph
```

```
komi1277: ▇ 1.03
```