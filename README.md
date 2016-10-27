# Urbanlookup

Wrapper for urbandictionary.com. Supports random words with the -r flag.

## Usage

```
# urbanlookup -h
usage: main.py [-h] [-n NUM] [-r] [-a] [word]

positional arguments:
  word               Word used in query

optional arguments:
  -h, --help         show this help message and exit
  -n NUM, --num NUM  Specifies the number of results to return
  -r, --random       Return random result
  -a, --all          Return all results
```

## Example

```
# urbanlookup api

==================================

Word:

        API

Author:

        Nathanmx

Definition:

API = application programming interface    An API is a series of
        functions that programs can use to make the operating system do their
        dirty work. Using Windows APIs, for example, a program can open
        windows, files, and message boxes--as well as perform more
        complicated tasks--by passing a single instruction. Windows has
        several classes of APIs that deal with telephony, messaging, and
        other issues.

Example:

        Windows uses an api called the Win32 API.  You can access many command
        via the command prompt. Start >> Run >> Type in "command" or "cmd"

Rating: 239

==================================


```
