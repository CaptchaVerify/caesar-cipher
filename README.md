# Caesar Cipher

A command-line encryption tool built in Python that implements the Caesar cipher algorithm.

## Features
- Encrypt a message with a shift number between 1-25
- Decrypt a message if you know the shift number
- Brute force mode - tries all 25 possible shifts to crack an unknown cipher
- Saves output to a timestamped .txt file automatically
- Runs in a loop so you can process multiple messages without restarting

## How to run
```bash
python cipher.py
```

## What I learned
- How the Caesar cipher works using ASCII values and the ord/chr functions
- Using the modulo operator to wrap the alphabet correctly
- File handling in Python - writing and saving output to .txt files
- Building a full interactive command-line tool with loops and input validation
