## A Python Tool to Extract Page Records from Wikimedia SQL Data Dumps

**Author**: Bill Thompson (biltho@mpi.nl)


#### Summary
A Simple python script to extract a record of all pages in a given wikipedia from [Wikimedia](https://dumps.wikimedia.org) sql dumps. Writes out a csv with ("page_id", "page_namespace", "page_title", and "page_len") columns.

Usage:

```python main.py -f avwiki-latest-page.sql.gz```

The latest dumps for the English wikipedia, for example, can be found [here](https://dumps.wikimedia.org/enwiki/latest/). This script works on the sql version of the page table dump (e.g.: [link](dumps.wikimedia.org/enwiki/latest/enwiki-latest-page.sql.gz)). This repository contains an example dump (```avwiki-latest-page.sql.gz```) and an example of the parsed result (```avwiki-latest-page-parsed.csv```). The latest dumps in other languages can be found at:

dumps.wikimedia.org/LANGUAGEwiki/latest/LANGUAGEwiki-latest-page.sql.gz

where LANGUAGE is replaced by the language iso (e.g. en, ab, es, pt, fr, etc...).



