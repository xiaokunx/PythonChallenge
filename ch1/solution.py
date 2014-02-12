import webbrowser as wb
html_prefix = "http://www.pythonchallenge.com/pc/def/"
html_suffix = ".html"

input = 'map'
alphabet_shift = 2
key = "".join(chr(ord(x) + alphabet_shift) for x in input)
wb.open(html_prefix + key + html_suffix)
