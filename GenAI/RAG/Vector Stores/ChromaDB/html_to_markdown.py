import os
import markdownify as m
import rich as r
from bs4 import BeautifulSoup

parentDir = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(os.path.join(parentDir, "markdowns")):
    os.mkdir(os.path.join(parentDir, "markdowns"))

with open(os.path.join(parentDir, r"html_pages/python_gil.html"), mode="r", encoding="utf-8") as f:
    content = f.read()
    content = BeautifulSoup(content, "lxml")


# for data in content(['script', 'img', 'a', 'figure', "form"]):
#         # Remove tags
#         data.decompose()

print(content)

# markdown = m.markdownify(str(content.prettify()))
markdown = m.markdownify(str(content))
with open(os.path.join(parentDir, r"markdowns/python_gil.md"), mode="w", encoding="utf-8") as f:
    f.write(markdown)
