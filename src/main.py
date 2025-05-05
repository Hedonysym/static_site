import markdown_blocks
import copy_static
import generate_pages

def main():
   copy_static.public_to_static()
   contentpath = generate_pages.extend_path_to_root("content")
   templatepath = generate_pages.extend_path_to_root("template.html")
   publicpath = generate_pages.extend_path_to_root("public")
   generate_pages.generate_pages_recursive(contentpath, templatepath, publicpath)



if __name__ == "__main__":
    main()
