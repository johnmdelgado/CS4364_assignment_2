# CS4364 Assignment 2: Pre-processing

# Project

Given a text file (input.txt), write a program (in your language of choice) to pre-process the file. The program should
a. Tokenize the lines of the file based on white-spaces.
b. Case-fold each token to lowercase.
c. Identify the stop-words. Use the stop words from the stop_words.txt file.
d. Remove all punctuation.
e. Use Porter stemmer to stem the tokens.
f. Write each token on a separate line in the output file.
g. Write the type of token - for all non-empty token, next to the token, in the same line of the output file, write ‘article’ if the token is an article (i.e., a, an, the), ‘stop word’ if the token is a stop word, otherwise, write the stemmed version of the token.
Sample input file: The less there is to justify a traditional custom, the harder it is to get rid of it.

Sample output file:
the - article
less - less
there - stop word
is - stop word
to - stop word
justify - justifi
a - article
traditional - tradit
custom - custom  
 the - article
harder - harder
it - stop word
is - stop word
to - stop word
get - get
rid - rid
of - stop word
it - stop word

Deliverables: 2 files

1. The source code of the program. The name of the file should be lastname_firstname.xyz (replace xyz with proper extension).
2. The output txt file. The filename should be lastname_firstname.txt \*https://tartarus.org/martin/PorterStemmer/

## Built with

[Python 3.9.0](https://www.python.org/downloads/release/python-390/)

## Prerequisites

### Python Version 3.9.0

    sudo apt-get update
    sudo apt-get install python3.9.0

### Python yaml package

    pip3 install pyyaml

## Installation

1. clone repo from: https://github.com/johnmdelgado/CS4364Assignment2

## Configuration

Under the configs folder is the config.yaml file with configuration settings. These are the default values but can be updated as needed or as requirements change.

```
filepaths:
  input_file_filepath: "data/input.txt"
  stop_word_filepath: "data/stop_words.txt"

output_settings:
  output_to_terminal: true
  output_to_file: true
  output_dir: "/output/"
```

## Example Usage

- Included in this package under the data folder is a input.txt that will be used by default if there isn't a txt file specifed.

```
        cat test_file.txt | python3 ./delgado_john.py
```

- you can also run without sending a file and it will attempt to load the default values

```
        python3 ./delgado_john.py
```

## Output

If the configuration values are set to true in the config file. It will output either to the terminal or
if `output_to_file` is set to true, it will output a file to the output directory in the root directory
with the naming convention of `Output_Data_29102021T160108.txt` with the datetime being dynamically generated
at output time.

## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## References/Tools

- https://regex101.com/

## License

Distributed under the MIT License. See `LICENSE` for more information.
