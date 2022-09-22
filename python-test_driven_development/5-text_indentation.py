#!/usr/bin/python3
"""text_indentation Module"""


def text_indentation(text):
    """Write a function that prints a text with 2 new \
        lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    bool = False
    for i in range(0, len(text)):
        if bool:
            bool = False
            continue
        if text[i] == "." or text[i] == ":" or text[i] == "?":
            print(f"{text[i]}")
            print("")
            if text[i] != text[-1] and text[i+1] == " ":
                bool = True
        else:
            print(f"{text[i]}", end="")
