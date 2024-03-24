def display_file_content(file_path):
    try:
        with open(file_path,"r") as file: #reads the file_path
            content=file.read()#display the file contents
            print(content)
    except IOError as e:
        print("Error",e)

file_path="C:\\Users\\Pabitha\\python prog\\file2.txt"
display_file_content(file_path)#calling function