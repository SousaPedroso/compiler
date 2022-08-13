<h1 align="center">Compiler of simple arithmetic operations</h1>

This repository contains the final project of Compilers II subject at UFMT proposed by the professor <a href="https://github.com/thesivis">Raphael</a>.

The valid tokens of the language can be seen according to the following automata.

<p align="center">
  <img alt="Automata of the language" src="./lexer/Lexer_LALG.svg" width=1000>
</p>

Using the ascendent syntatic, the automata which describes the rules for the <a href="https://github.com/SousaPedroso/compiler/blob/main/language">language </a> is demonstrated below, using a dictionary in python:

<p align="center">
  <img alt="Automata of the rules" src="./syntatic/Syntatic_Automata_LALG.svg">
</p>


None external package was used for this project, but for execute it you must install this repository as a package due to the directories organization, running the following command on the root of this repository:

```
python -m pip install .
```