""" Create a script that let the user type in a search term
and google browsers opens with that term.
"""

import webbrowser

query = input("Input your query: ")
webbrowser.open(f"https://google.com/search?q={query}")