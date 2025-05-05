import markdown_blocks
import copy_static
import generate_pages

def main():
   copy_static.public_to_static()
   generate_pages.generate_page("content/index.md", "template.html", "public/index.html")



if __name__ == "__main__":
    main()
