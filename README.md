password_gen - is simple script for generation password by using Python3 and his modules. There is just one python file. Let me explain how it works.


usage: pass_gen [-h] [--name NAME] [--length LENGTH]

Python password generate

optional arguments:
  -h, --help            show this help message and exit
  --name NAME, -n NAME  Line for input username
  --length LENGTH, -l LENGTH
                        Line for input password length




First of all we using 3 modules: 
  1. string
  2. random
  3. argparse
  
First two of them we use for generate password. We randomize subsequence of our password and length we will input by ourself. So it's very simple. String module contains ASCII is a character encoding standard for electronic communication. Below is the list of string constants you can use to get a different set of characters as a source for creating a random string. 

Constant                Description

ascii_lowercase	        Contain all lowercase letters

ascii_uppercase	        Contain all uppercase letters

ascii_letters	          Contain both lowercase and uppercase letters

digits	                Contain digits ‘0123456789’.

punctuation	            All special symbols !”#$%&'()*+,-./:;<=>?@[\]^_`{|}~.

whitespace	            Includes the characters space, tab, linefeed, return, formfeed, and vertical tab [^ \t\n\x0b\r\f]

printable	              characters that are considered printable. This is a combination of constants digits, letters, punctuation, and whitespace.




The argparse module makes it easy to write user-friendly command-line interfaces.

As you can see, we have 2 functions:
  - ppg
  - main

Our 'ppg' (python password generator) function is generation password and takes two parametrs (name - username, for which we generate password and length - for length of generated password).
Function 'main'uses argparse module. We create parser at first string of function, them ArgumentParse object will hold all the info necessary to paste command line into python data types. After that we adding arguments. Fillin an AP(ArgumentParser) with info about program arguments is done by making call to the add-argument() method. Generally AP calls tells AP how to take the strings on the command line and turn them into objects. Them parse_args() argument parcing info which was written into command line.

* For execute script from ant directory we should write path where python3 is located. For to do that:
  1. Write 'which python3' and copy path.
  2. At first string of file write:
      example     #!usr/local/bin
     them write in working directory this command for give permition to execute from any directory:
      sudo chmod +x parse.py
  3. Now we can write parse.py -h and it's works. But visually not beautiful write comand with '.py'. To solve this again find our parse.py in path which we use
  first string. And change filename to any you want. Write this command:
      sudo mv parse.py pass_gen
  4. Then try to write pass_gen (or you filename) and it will work.
