import webbrowser as wb

html_prefix = "http://www.pythonchallenge.com/pc/def/"
key = str(2**38)
wb.open(html_prefix + key + '.html')
