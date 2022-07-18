'''
    "Encrypt Strings"

    Write a function called encrypt_strings that takes in three strings
    and returns one string consisting of the three strings concatenated and encrypted.

    The encryption technique works as follows:
      - Turn any lowercase vowels into an "x"
        - If the string is less than two characters STOP after the first step
        - Otherwise do the following steps
      - Add the last two characters to the front of the string
      - Add a space between the third and fourth character
      
      Example encryptions:
        - "Hello" -> "Hxllx" -> "lxHxllx" -> "lxH xllx"
        - "world!" -> "wxrld!" -> "d!wxrld!" -> "d!w xrld!"
        - "ca" -> "cx" -> "cxcx" -> "cxc x"
        - "e" -> "x"
      
    HINT: Try using a helper function!

    Examples:
        encrypt_strings("Hello", "new", "world!") --> "lxH xllxxwn xwd!w xrld!"
        encrypt_strings("ab", "cc", "e") --> "xbx bccc cx"
        encrypt_strings("aaa", "", "476") --> "xxx xx764 76"
'''

#Write your function under here