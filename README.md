# Data Science Project Template

This repository contains a solution to [Google's scrambled words problem](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/0000000000051004).

## Problem Statement

Consider two files; the **input** and the **dictionary**. Each file is plain text, and on each line of each file is a string consisting of lowercase ascii letters without spaces.

_Definition: Let s1 and s2 be strings. We say s2 is a scrambled substring of s1 if there exists at least one substring s3 of s2, such that the following is true:_

* _The first letter of s2 equals the first letter of s3._
* _The last letter of s2 equals the last letter of s3._
* _The middle letters (i.e. excluding the first and last letters) of s2 are a permutation of the middle letters of s3._

Note, that the definition the scrambled substring implies that _s2_ and _s3_ have equal length.

_Problem: For each string in the input file, count how many strings in the dictionary are scrambled substrings of said string._

The solution in this repository formats the solution as a string printed to stdout. Each line of the string has the structure _Case #x: y_, where _x_ is the line number in the input file, and _y_ is the number of strings in the dictionary that are scrambled substrings of the string on line _x_ of the input file.

## Solution Methodolgy

The algorithm implemented in this repository has two steps.

### Check First and Last Letters

Given a string in the input file `input_str` and a string in the dictionary `dict_str`, we check the following conditions.

1. Record the length of `dict_str`, let's call it `length`. Also record the first/last letters of `dict_str`, i.e. `dict_str[0]` and `dict_str[-1]`.
2. Record the indices of all instances of `dict_str[0]` in `input_str`.
3. For each index `i` such that `input_str[i]=dict_str[0]`, check if `input_str[i+length]=dict_str[-1]`, and if so check if the middle letters of dict_str (i.e. `dict_str[1:-1]`) are a permutation of the middle letters of this section of the input string (i.e. `input_str[i+1:i+length]`).

Note that in these steps, if we do not find any letters in `input_str` fulfilling a certain condition, we do not need to proceed to the next step. The algorithm in this repository breaks prematurely if a step are not fulfilled.

### Check if Middle Letters are a Permutation

To check if two lowercase ascii strings are permutations of one another, it suffices to count the number of instances of each lowercase letter of the alphabet. In the code in this repository we save this information as lists of 26 non-negative integers.

As a further efficiency gain we create the 26-integer encoding of each of dictionary string before scanning the input strings, and save these encodings as an attribute of the class `StringWrapper`. 26-integer encodings of the middle letters of a substring of `input_str` (i.e. `input_str[i+1:i+length]`) are made only if the first and last letters match as described in the [previous subsection](#check-first-and-last-letters).

To further reduce the search time, we only check if `dict_str` is a scrambled substring of `input_str` if the length of the former is smaller than the length of the later.

## Running the Code

The following subsections described how to run the solution, tests or local development commands. All file paths are relative to the root of the repository.

There are two environment variables that can be set to control the logging level. To set the logging level to `DEBUG` first run the command

```bash
export SCRAMBLED_WORDS_DEBUG_MODE=1
```

If you want to supress `DEBUG` messages but want information about any scrambled substrings that are found to be printed to stdout, first run the command

```bash
export SCRAMBLED_WORDS_LOG_MATCHES=1
```

### Running the Solution

To run the solution, run this command.

```bash
python src/scrmabled_strings.py --dictionary [PATH TO DICTIONARY FILE] --input [PATH TO INPUT FILE]
```

This command should run if python 3.9.13 is installed. You can create this environment by building and running the code inside a docker container. To build and attach to a container with the required python environment run

```bash
docker-compose run -it scrambled-words /bin/bash
```

Then run the above commmand to execute the code.

### Creating Sample Data

The module `src/generate_data.py` contains two files for generating sample dictionaries and sample input files. Navigate to the [bottom of the file](https://github.com/mark-curran/scrambled-words/blob/27897a9ea569fbf4c552a914048b9a5a5a414731/src/generate_data.py#L86) to set the parameters you desire, then run the command

```bash
python ./src/generate_data.py
```

Note, that the file names `dict_file.txt` and `input_file.txt` are in the `.gitignore`. These might be convenient file names for the purposes of creating sample data.

### Running Tests

To run tests make sure pytest is installed. Alternatively, the [local development environment](#local-development) already has pytest installed.

To run the tests, run the command

```bash
pytest --verbose
```

## Local Development

Note, this repository uses boilerplate code from this [template](https://github.com/mark-curran/data-science-project-template). This repository also contains instructions for using the VSCode remote containers extension to get up and running with a local development environment.

If you are unfamiliar with the VSCode remote containers extension but are familiar with docker, you can build and attach to a local development container by running the command.

```bash
docker-compose -f .devcontainer/docker-compose-local.yml run -it local-dev /bin/bash
```
