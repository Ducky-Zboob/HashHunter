# HashHunter

## How to use it ?

To use `HashHunter`, you have to install the required `Python modules` with this command :

``` bash
pip3 install -r requirements.txt
```

After that, you can **execute the script** with the command :
``` bash
./HashHunter.py
```

or with this command :

``` bash
python3 HashHunter.py
```

You can now **see the command help menu**.

----

## Command Help `Documentation`

-h, --help              : **show this help message and exit**

-H [hashstring], --hashstring [hashstring]
                        : **define the hash string which you want to crack**

-W [wordlist], --wordlist [wordlist]
                        : **define the wordlist's path**

-R [range], --range [range]
                        : **define the range of the attack ({min/max} letters range)**

-C [charset], --charset [charset]
                        : **define a charset for the attack**

-P [pattern], --pattern [pattern]
                        : **define a pattern for the attack. use @ to specify the character which will be bruteforce**

----

## `Attack examples`

### `Wordlist` attack

``` bash
./HashHunter.py -H (the hashstring) -W (wordlist path)
```

* -H define the hashstring which you want to crack

* -W define the path of your wordlist

### `Range` attack

``` bash
./HashHunter.py -H (the hashstring) -R 1/3 (-C your charset)
```
* -H define the hashstring which you want to crack

* -R define the range of the word generation (in this exemple, the generation will generate all words posibilities of 1 to 3 characters)

* -C define the charset (it's not required)

### `Pattern` attack

``` bash
./HashHunter.py -H (the hashstring) -P @ey! (-C your charset)
```

* -H define the hashstring which you want to crack

* -P define your pattern, for exemple I want to crack a word which is ending with { ey! } and have 1 character which I don't know

* -C define the charset (it's not required)