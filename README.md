# postgres_explain_analyze_json_schema

a JSON schema for postgres ``EXPLAIN (ANALYZE, COSTS, VERBOSE, BUFFERS)` yaml or json.

## Methodology

Unfortunately, the schema is hand-maintained.

1. I generated many the output of many `EXPLAIN (ANALYZE, COSTS, VERBOSE, BUFFERS, FORMAT YAML)` queries in [`pg_inventory`](https://github.com/SKalt/pg_inventory)
1. an initial skeleton of the schema was generated with [the python `genson` package](https://github.com/wolverdude/GenSON/) using [`./scripts/generate_initial_schema.py`](./scripts/generate_initial_schema.py),
1. guessing which string types have constrained values, (i.e. any key ending in " Type:"), I used [`./scripts/collect_enums.sh`](./scripts/collect_enums.sh) to generate enumeration values and hand-defined the enumerations
1. I extracted a definition of a `Plan` object and used it to recursively define itself
1. I transformed the JSON into YAML <!-- TODO: enhance the YAML schema with documentation -->
1. Finally, I test the definition against the corpus of YAML I have.
