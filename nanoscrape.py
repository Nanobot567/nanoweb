# nanoscrape 1.0
# by nanobot567
# started work on april 7, 2021


try:
    print("Importing assets...")
    import requests
    print("Done!\n")
except:
    print("Import failed, downloading required assets from pip...")
    try:
        try:
            from pip._internal import main as _pip_main
        except ImportError:
            from pip import main as _pip_main

        _pip_main(["install", "requests"])
    except:
        print("You do not have pip installed! Please download it before you run this program.")
        quit()



ans = ""

x = ""
x = input("Please paste the link here or type 'cancel' to cancel: ")
if "https://" or "http://" in x:
    
    url = x
    print("Please wait while I check if the link is valid... (this could take several minutes)")
    try:
        r = requests.get(url)
        m = input("What is the file extension (.zip, .exe, etc.)? ")
    
        if "." in m:
            ext = m
            l = input("Where would you like this to be stored (please put double backslashes like C:\\\\ if you are on windows)? ")
            path = l
            s = input("What is this file going to be called (without extension)? ")
            name = s
            print("Alright, downloading...")
            try:
                with open(f'{path}{name}{ext}', 'wb') as f:
                    f.write(r.content)

                print(f"status_code: {r.status_code}")
                print(f"type: {r.headers['content-type']}")
                print(f"encoding: {r.encoding}")
            except Exception as e:
                print(f"Something went wrong! Please try again. (Error: {str(e)})")

    except Exception as e:
        print(f"Something went wrong! Please try again. (Error: {str(e)})")
elif x == "cancel":
    pass
else:
    print("That is not a valid url! Please try again.")
        
    



