from datetime import datetime
#import datetime module
def create_file(filepath):
    try:    
        current_date=datetime.now()
        with open(filepath,"w") as file:   
            file.write(str(current_date))#file contains date and time in it
            print("File Created at",filepath)
    except IOError as e:
        print("Error",e)

filepath="C:\\Users\\Pabitha\\Downloads\\file1.txt"
create_file(filepath)#creating function to create a text file with date and time
