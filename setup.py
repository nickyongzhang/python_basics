from cx_Freeze import setup, Executable

setup(name = "website_parsing" ,
      version = "0.1" ,
      description = "Parse contents in a website" ,
      executables = [Executable("website_parsing.py")])