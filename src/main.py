from data_stuff import copye, generate_pages_recursive
import sys

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    src, dest = "static", "docs"
    copye(src, dest)
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()