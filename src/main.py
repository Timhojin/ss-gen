from data_stuff import copye, generate_pages_recursive

def main():
    src, dest = "static", "public"
    copye(src, dest)
    generate_pages_recursive("content", "template.html", "public")

main()