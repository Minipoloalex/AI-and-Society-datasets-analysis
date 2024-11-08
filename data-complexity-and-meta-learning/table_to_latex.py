"""
First, you need to convert the .md table to latex using https://tableconvert.com/markdown-to-latex

Instead of running this script, you could also use the "Find and Replace" tool from VSCode.
"""

import re

text = None
ouptut_table_file = input_table_file = "output_latex_table.txt"

with open(input_table_file) as f:
    text = f.read()

new_text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)

with open(ouptut_table_file, "w") as f:
    f.write(new_text)
