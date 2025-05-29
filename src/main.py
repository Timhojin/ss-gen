from data_stuff import copye, generate_pages_recursive
import sys

def main():
    basepath = "/"
    if sys.argv[0]:
        if sys.argv[0][-1] != "/":
            basepath = sys.argv[0] + "/"
        else:
            basepath = sys.argv[0]

    src, dest = "static", "docs"
    copye(src, dest)
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()