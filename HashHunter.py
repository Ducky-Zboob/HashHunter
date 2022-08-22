#!/bin/python3

# =====Imports=====

import argparse
import string
from colorama import Fore, Style
import os
import hashlib
from Cryptodome.Hash import keccak, SHA3_224, SHA3_256
from Cryptodome.Hash import SHA3_384, SHA3_512, MD2, MD4
import wordlist as wordGen

# =====Args-Manager=====

ArgsParser = argparse.ArgumentParser()

ArgsParser.add_argument(
    '-H',
    '--hashstring',
    help='define the hash string which you want to crack'
)

ArgsParser.add_argument(
    '-W',
    '--wordlist',
    help="define the wordlist's path"
)

ArgsParser.add_argument(
    '-R',
    '--range',
    help='define the range of the attack ({min/max} letters range)'
)

ArgsParser.add_argument(
    '-C',
    '--charset',
    help='define a charset for the attack'
)

ArgsParser.add_argument(
    '-P',
    '--pattern',
    help=''.join([
        'define a pattern for the attack. use @ to specify the character ',
        'which will be bruteforce'
        ])
)

FinalArgs = ArgsParser.parse_args()

# =====Variables=====

hashhunter_title = """
  ___ ___               .__        ___ ___               __                
 /   |   \_____    _____|  |__    /   |   \ __ __  _____/  |_  ___________ 
/    ~    \__  \  /  ___/  |  \  /    ~    \  |  \/    \   __\/ __ \_  __ \\
\    Y    // __ \_\___ \|   Y  \ \    Y    /  |  /   |  \  | \  ___/|  | \/
 \___|_  /(____  /____  >___|  /  \___|_  /|____/|___|  /__|  \___  >__|   
       \/      \/     \/     \/         \/            \/          \/     
""" # noqa

# =====Functions=====


def bruteforce():

    try_number = 0

    hashstring = FinalArgs.hashstring

    if FinalArgs.wordlist:
        wordlist = open(
            os.path.realpath(FinalArgs.wordlist),
            'r'
        )
        words_list = wordlist.readlines()
        wordlist.close()
        real_words_list = []
        for word in words_list:
            if word[-1] == '\n':
                real_words_list.append(word[0:-1])
            else:
                real_words_list.append(word)

        print(
            Fore.CYAN +
            Style.BRIGHT +
            '\n[*] ' +
            Fore.WHITE +
            Style.NORMAL +
            "Starting wordlist bruteforce attack."
        )
        print(
            Fore.CYAN +
            Style.BRIGHT +
            '[*] ' +
            Fore.WHITE +
            Style.NORMAL +
            f"On hash [ {hashstring} ]."
        )
        print(
            Fore.CYAN +
            Style.BRIGHT +
            '[*] ' +
            Fore.WHITE +
            Style.NORMAL +
            f"With wordlist [ {FinalArgs.wordlist} ]."
        )

        for word in real_words_list:

            md2Hashed = MD2.new()
            md2Hashed.update(str(word).encode())
            md2Hashed = md2Hashed.hexdigest()

            md4Hashed = MD4.new()
            md4Hashed.update(str(word).encode())
            md4Hashed = md4Hashed.hexdigest()

            md5Hashed = hashlib.md5()
            md5Hashed.update(str(word).encode())
            md5Hashed = md5Hashed.hexdigest()

            sha1Hashed = hashlib.sha1()
            sha1Hashed.update(str(word).encode())
            sha1Hashed = sha1Hashed.hexdigest()

            sha224Hashed = hashlib.sha224()
            sha224Hashed.update(str(word).encode())
            sha224Hashed = sha224Hashed.hexdigest()

            sha256Hashed = hashlib.sha256()
            sha256Hashed.update(str(word).encode())
            sha256Hashed = sha256Hashed.hexdigest()

            sha384Hashed = hashlib.sha384()
            sha384Hashed.update(str(word).encode())
            sha384Hashed = sha384Hashed.hexdigest()

            sha512Hashed = hashlib.sha512()
            sha512Hashed.update(str(word).encode())
            sha512Hashed = sha512Hashed.hexdigest()

            sha3224Hashed = SHA3_224.new()
            sha3224Hashed.update(str(word).encode())
            sha3224Hashed = sha3224Hashed.hexdigest()

            sha3256Hashed = SHA3_256.new()
            sha3256Hashed.update(str(word).encode())
            sha3256Hashed = sha3256Hashed.hexdigest()

            sha3384Hashed = SHA3_384.new()
            sha3384Hashed.update(str(word).encode())
            sha3384Hashed = sha3384Hashed.hexdigest()

            sha3512Hashed = SHA3_512.new()
            sha3512Hashed.update(str(word).encode())
            sha3512Hashed = sha3512Hashed.hexdigest()

            keccak224Hashed = keccak.new(digest_bits=224)
            keccak224Hashed.update(str(word).encode())
            keccak224Hashed = keccak224Hashed.hexdigest()

            keccak256Hashed = keccak.new(digest_bits=256)
            keccak256Hashed.update(str(word).encode())
            keccak256Hashed = keccak256Hashed.hexdigest()

            keccak384Hashed = keccak.new(digest_bits=384)
            keccak384Hashed.update(str(word).encode())
            keccak384Hashed = keccak384Hashed.hexdigest()

            keccak512Hashed = keccak.new(digest_bits=512)
            keccak512Hashed.update(str(word).encode())
            keccak512Hashed = keccak512Hashed.hexdigest()

            try_number += 1

            if md2Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in MD2.\n"
                )
                exit()

            elif md4Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in MD4.\n"
                )
                exit()

            elif md5Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in MD5.\n"
                )
                exit()

            elif sha1Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA1.\n"
                )
                exit()

            elif sha224Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA224.\n"
                )
                exit()

            elif sha256Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA256.\n"
                )
                exit()

            elif sha384Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA384.\n"
                )
                exit()

            elif sha512Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA512.\n"
                )
                exit()

            elif sha3224Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA3 224.\n"
                )
                exit()

            elif sha3256Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA3 256.\n"
                )
                exit()

            elif sha3384Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA3 384.\n"
                )
                exit()

            elif sha3512Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA3 512.\n"
                )
                exit()

            elif keccak224Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in Keccak 224.\n"
                )
                exit()

            elif keccak256Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in Keccak 256.\n"
                )
                exit()

            elif keccak384Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in Keccak 384.\n"
                )
                exit()

            elif keccak512Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in Keccak 512.\n"
                )
                exit()

    if FinalArgs.pattern:

        pattern = FinalArgs.pattern

        print(
            Fore.CYAN +
            Style.BRIGHT +
            '\n[*] ' +
            Fore.WHITE +
            Style.NORMAL +
            "Starting pattern bruteforce attack."
        )
        print(
            Fore.CYAN +
            Style.BRIGHT +
            '[*] ' +
            Fore.WHITE +
            Style.NORMAL +
            f"On hash [ {hashstring} ]."
        )
        print(
            Fore.CYAN +
            Style.BRIGHT +
            '[*] ' +
            Fore.WHITE +
            Style.NORMAL +
            f"With the pattern {pattern}."
        )

        if FinalArgs.charset:

            print(
                Fore.CYAN +
                Style.BRIGHT +
                '[*] ' +
                Fore.WHITE +
                Style.NORMAL +
                f"With charset [ {FinalArgs.charset} ]."
            )

            charset = FinalArgs.charset

        else:

            charset = string.ascii_letters + string.digits + string.punctuation

        word_generator = wordGen.Generator(charset=charset)

        for word in word_generator.generate_with_pattern(pattern=pattern):

            md2Hashed = MD2.new()
            md2Hashed.update(str(word).encode())
            md2Hashed = md2Hashed.hexdigest()

            md4Hashed = MD4.new()
            md4Hashed.update(str(word).encode())
            md4Hashed = md4Hashed.hexdigest()

            md5Hashed = hashlib.md5()
            md5Hashed.update(str(word).encode())
            md5Hashed = md5Hashed.hexdigest()

            sha1Hashed = hashlib.sha1()
            sha1Hashed.update(str(word).encode())
            sha1Hashed = sha1Hashed.hexdigest()

            sha224Hashed = hashlib.sha224()
            sha224Hashed.update(str(word).encode())
            sha224Hashed = sha224Hashed.hexdigest()

            sha256Hashed = hashlib.sha256()
            sha256Hashed.update(str(word).encode())
            sha256Hashed = sha256Hashed.hexdigest()

            sha384Hashed = hashlib.sha384()
            sha384Hashed.update(str(word).encode())
            sha384Hashed = sha384Hashed.hexdigest()

            sha512Hashed = hashlib.sha512()
            sha512Hashed.update(str(word).encode())
            sha512Hashed = sha512Hashed.hexdigest()

            sha3224Hashed = SHA3_224.new()
            sha3224Hashed.update(str(word).encode())
            sha3224Hashed = sha3224Hashed.hexdigest()

            sha3256Hashed = SHA3_256.new()
            sha3256Hashed.update(str(word).encode())
            sha3256Hashed = sha3256Hashed.hexdigest()

            sha3384Hashed = SHA3_384.new()
            sha3384Hashed.update(str(word).encode())
            sha3384Hashed = sha3384Hashed.hexdigest()

            sha3512Hashed = SHA3_512.new()
            sha3512Hashed.update(str(word).encode())
            sha3512Hashed = sha3512Hashed.hexdigest()

            keccak224Hashed = keccak.new(digest_bits=224)
            keccak224Hashed.update(str(word).encode())
            keccak224Hashed = keccak224Hashed.hexdigest()

            keccak256Hashed = keccak.new(digest_bits=256)
            keccak256Hashed.update(str(word).encode())
            keccak256Hashed = keccak256Hashed.hexdigest()

            keccak384Hashed = keccak.new(digest_bits=384)
            keccak384Hashed.update(str(word).encode())
            keccak384Hashed = keccak384Hashed.hexdigest()

            keccak512Hashed = keccak.new(digest_bits=512)
            keccak512Hashed.update(str(word).encode())
            keccak512Hashed = keccak512Hashed.hexdigest()

            try_number += 1

            if md2Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in MD2.\n"
                )
                exit()

            elif md4Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in MD4.\n"
                )
                exit()

            elif md5Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in MD5.\n"
                )
                exit()

            elif sha1Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA1.\n"
                )
                exit()

            elif sha224Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA224.\n"
                )
                exit()

            elif sha256Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA256.\n"
                )
                exit()

            elif sha384Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA384.\n"
                )
                exit()

            elif sha512Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA512.\n"
                )
                exit()

            elif sha3224Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA3 224.\n"
                )
                exit()

            elif sha3256Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA3 256.\n"
                )
                exit()

            elif sha3384Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA3 384.\n"
                )
                exit()

            elif sha3512Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in SHA3 512.\n"
                )
                exit()

            elif keccak224Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in Keccak 224.\n"
                )
                exit()

            elif keccak256Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in Keccak 256.\n"
                )
                exit()

            elif keccak384Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in Keccak 384.\n"
                )
                exit()

            elif keccak512Hashed == hashstring:

                print(
                    Fore.GREEN +
                    Style.BRIGHT +
                    "\n[+]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" String found ! [ {word} ]"
                )
                print(
                    Fore.CYAN +
                    Style.BRIGHT +
                    "[*]" +
                    Fore.WHITE +
                    Style.NORMAL +
                    f" Found in {try_number} try. | Encrypted in Keccak 512.\n"
                )
                exit()


def research_error():
    error_code = 0

    if (
        not FinalArgs.hashstring and
        not FinalArgs.wordlist and
        not FinalArgs.range and
        not FinalArgs.pattern and
        not FinalArgs.charset
    ):
        print(Fore.WHITE + Style.NORMAL)
        print('-h, --help               show this message and exit')
        print('-H, --hashstring         define the hashstring which you want to crack')
        print("-W, --wordlist           define your wordlist's path")
        print("-R, --range              define the range of your Range attack (the words lenght)")
        print("-P, --pattern            define the pattern of your Pattern attack")
        print("-C, --charset            define the charset for your Range or Pattern attack")
        print("\nExecute the script with the option '--help' for more informations.\n")
        exit()

    if not FinalArgs.hashstring:
        print(
            Fore.RED +
            Style.BRIGHT +
            '\n[-] ' +
            Fore.WHITE +
            Style.NORMAL +
            "'hashstring' argument not defined."
        )
        error_code += 1
    if (not FinalArgs.wordlist and not FinalArgs.range and
       not FinalArgs.pattern):

        if error_code != 0:
            print(
                Fore.RED +
                Style.BRIGHT +
                '[-] ' +
                Fore.WHITE +
                Style.NORMAL +
                "'wordlist', 'range' or 'pattern' argument not defined."
            )
        else:
            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[-] ' +
                Fore.WHITE +
                Style.NORMAL +
                "'wordlist' or 'range' argument not defined."
            )
        print(
            Fore.RED +
            Style.BRIGHT +
            '[-] ' +
            Fore.WHITE +
            Style.NORMAL +
            "Unrecognize attack type."
        )
        error_code += 1
    if FinalArgs.wordlist and FinalArgs.range:
        if error_code != 0:
            print(
                Fore.RED +
                Style.BRIGHT +
                '[-] ' +
                Fore.WHITE +
                Style.NORMAL +
                "'wordlist' and 'range' arguments defined and make conflicts."
            )
        else:
            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[-] ' +
                Fore.WHITE +
                Style.NORMAL +
                "'wordlist' and 'range' arguments defined and make conflicts."
            )
        print(
            Fore.RED +
            Style.BRIGHT +
            '[-] ' +
            Fore.WHITE +
            Style.NORMAL +
            "Unrecognize attack type."
        )
        error_code += 1

    if FinalArgs.wordlist and FinalArgs.charset:
        if error_code != 0:
            print(
                Fore.RED +
                Style.BRIGHT +
                '[-] ' +
                Fore.WHITE +
                Style.NORMAL +
                "'wordlist' and 'charset' arguments defined and make conflicts."
            )
        else:
            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[-] ' +
                Fore.WHITE +
                Style.NORMAL +
                "'wordlist' and 'charset' arguments defined and make conflicts."
            )
        print(
            Fore.RED +
            Style.BRIGHT +
            '[-] ' +
            Fore.WHITE +
            Style.NORMAL +
            "Unrecognize attack type."
        )
        error_code += 1


    if FinalArgs.range and FinalArgs.pattern:
        if error_code != 0:
            print(
                Fore.RED +
                Style.BRIGHT +
                '[-] ' +
                Fore.WHITE +
                Style.NORMAL +
                "'range' and 'pattern' arguments defined and make conflicts."
            )
        else:
            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[-] ' +
                Fore.WHITE +
                Style.NORMAL +
                "'range' and 'pattern' arguments defined and make conflicts."
            )
        print(
            Fore.RED +
            Style.BRIGHT +
            '[-] ' +
            Fore.WHITE +
            Style.NORMAL +
            "pattern attack type don't need 'range' argument."
        )
        print(
            Fore.RED +
            Style.BRIGHT +
            '[-] ' +
            Fore.WHITE +
            Style.NORMAL +
            "Unrecognize attack type."
        )
        error_code += 1

    if FinalArgs.wordlist and FinalArgs.pattern:
        if error_code != 0:
            print(
                Fore.RED +
                Style.BRIGHT +
                '[-] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'wordlist' and 'pattern' arguments ",
                    "defined and make conflicts."
                ])
            )
        else:
            print(
                Fore.RED +
                Style.BRIGHT +
                '\n[-] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'wordlist' and 'pattern' arguments ",
                    "defined and make conflicts."
                ])
            )
        print(
            Fore.RED +
            Style.BRIGHT +
            '[-] ' +
            Fore.WHITE +
            Style.NORMAL +
            "pattern attack type don't need 'wordlist' argument."
        )
        print(
            Fore.RED +
            Style.BRIGHT +
            '[-] ' +
            Fore.WHITE +
            Style.NORMAL +
            "Unrecognize attack type."
        )
        error_code += 1

    if error_code != 0:
        exit()

    second_error_code = 0

    if FinalArgs.wordlist:
        if not os.path.isfile(FinalArgs.wordlist):
            print(
                Fore.RED +
                Style.BRIGHT +
                '[-] ' +
                Fore.WHITE +
                Style.NORMAL +
                "'wordlist' argument incorrect. Wordlist not found."
            )
            second_error_code += 1

    if FinalArgs.range:
        split_range_arg = FinalArgs.range.split('/')
        if len(split_range_arg) >= 3 or len(split_range_arg) <= 1:
            print(
                Fore.RED +
                Style.BRIGHT +
                '[-] ' +
                Fore.WHITE +
                Style.NORMAL +
                "".join([
                    "'range' argument invalid syntax. ",
                    "It must be {Arg1/Arg2} (Arg1:Min and Arg2:Max)."
                ])
            )
            second_error_code += 1
        else:
            try:
                int(split_range_arg[0])
                int(split_range_arg[1])
                if int(split_range_arg[0] > split_range_arg[1]):
                    print(
                        Fore.RED +
                        Style.BRIGHT +
                        '[-] ' +
                        Fore.WHITE +
                        Style.NORMAL +
                        "".join([
                            "'range' argument syntax error. ",
                            "Minimal value highter than maximal value."
                        ])
                    )
                    second_error_code += 1
            except: # noqa
                print(
                    Fore.RED +
                    Style.BRIGHT +
                    '[-] ' +
                    Fore.WHITE +
                    Style.NORMAL +
                    "'range' argument syntax error. Argument aren't integer."
                )
                second_error_code += 1

    if second_error_code != 0:
        exit()

    bruteforce()


# =====Program-Starting=====

if __name__ == '__main__':
    print(Fore.CYAN + Style.BRIGHT + hashhunter_title)
    research_error()
