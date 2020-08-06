# CaesarCipherCracker
Caesar Cipher Cracker implemented in Python.

The `words.txt` data file comes from this [Github repository](https://github.com/dwyl/english-words).

The program works by generating every possible offset with a Caesar cipher, and
then testing each word in the generated text by scanning for it in a dictionary
file. The program then generates a "score" for each offset, and the lowest score
is the offset with the most accurate decoding.

To run the program, follow this format:

```
python ccc.py
Enter your encoded text here.
<Enter text>
Ideal offset is <offset>
Decodeded output was "<output>."
```
