# Data Science Project Template

A solution to [Google's scrambled words problem](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/0000000000051004).

Note, this repo uses boilerplate code from this [template](https://github.com/mark-curran/data-science-project-template).

## Running the Code

### Creating Solution File

To run the code, run this command.

```bash
.src/scrmabled_strings.py --dictionary [PATH TO DICTIONARY FILE] --input [PATH TO INPUT FILE]
```

### Creating Sample Data

You can create a sample dictionary as follows.

```bash
python ./src/generate_data.py --dict-output [PATH TO DICTIONARY FILE]
```

You can create a sample input file as follows.

```bash
python ./src/generate_data.py --input-output [PATH TO INPUT FILE]
```

### Running Tests

To run tests, run this command.

```bash
pytest ...
```

## Local Development

Instructions on setting up a local dev environment.

TODO: Add section on logging levels, i.e., `export SCRAMBLED_WORDS_DEBUG_MODE=1` to set debug as the logging level.
