import markdown_blocks
import copy_static
import generate_pages
import sys

def main():
<<<<<<< HEAD
   basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
   contentpath = generate_pages.extend_path_to_root("content")
   templatepath = generate_pages.extend_path_to_root("template.html")
   publicpath = generate_pages.extend_path_to_root("docs")
   copy_static.dir_to_static(publicpath)
=======
<<<<<<< HEAD
   basepath = sys.argv if len(sys.argv) > 1 else "/"
   
   contentpath = generate_pages.extend_path_to_root("content")
   templatepath = generate_pages.extend_path_to_root("template.html")
   publicpath = generate_pages.extend_path_to_root("docs")
   copy_static.public_to_static(publicpath)
=======
   basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
   contentpath = generate_pages.extend_path_to_root("content")
   templatepath = generate_pages.extend_path_to_root("template.html")
   publicpath = generate_pages.extend_path_to_root("docs")
   copy_static.dir_to_static(publicpath)
>>>>>>> 2de3777 (maybe fix?)
>>>>>>> 61c0c31 (maybe fix?)
   generate_pages.generate_pages_recursive(contentpath, templatepath, publicpath, basepath)



if __name__ == "__main__":
    main()
