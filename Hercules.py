from DontEdit import *
from HelpLogo import *

try:
    ERROR = open("ERROR.log", "a")

    ProgramName = "Hercules"

    OS='Darwin'

    #this is for the user to understand what the program does
    if len(sys.argv) == 2 and sys.argv[1] == "--help" or len(sys.argv) == 2 and sys.argv[1] == "-h":
        HelpFile = open("HELP.txt", "w")

        #This is for the user to know what programs are used in this program
        ProgramsUsed = "+++++++++++++++Programs used+++++++++++++++"
        ProgramsUsedInfo = "This program will help you crack passwords \nIt has two programs inside it, one is Hydra and the other is Nmap"

        #this is for the user to understand what the program does
        HowToUse = "\n+++++++++++++++How to use++++++++++++++++++"
        HowToUseInfo01 = f"To use the program you have to tell the computer what port you want to scan."
        HowToUseInfo02 = f"\nIt will then scan the port that you asked for on the network and see if any ports that you asked are open."
        HowToUseInfo03 = f"\nIf there are any ports that are open, it will ask for a username and hostname"
        HowToUseInfo04 = f"\nWhen you give the program the username and hostname, it will try to crack that given parameters you gave it."
        HowToUseInfo05 = f"\nIf you want to use the program locally, you can type 'sudo python3 {ProgramName} --local'"
        
        # holds the information about how the program works in a array so it can grab them more easily
        info = (HowToUseInfo01 +
                HowToUseInfo02 + 
                HowToUseInfo03 + 
                HowToUseInfo04 +
                HowToUseInfo05)
        
        subprocess.run(["figlet", "? HELP ?"])

        print(text_art, file=HelpFile)
        print()
        #inputs the program used logo in a help file
        print(ProgramsUsed, file=HelpFile)

        #puts the info about the program inside the help file
        print(ProgramsUsedInfo, file=HelpFile)
        print(ProgramsUsed)
        print(ProgramsUsedInfo)
        print()

        #Puts the info logo in the help file
        print(HowToUse, file=HelpFile)

        #puts the info about how to use the program inside the help file
        print(info, file=HelpFile)
        #puts the info about how to use the program on the screen
        
        print(HowToUse)
        print(info)
        print()

    # puts the script in local mode
    elif len(sys.argv) == 2 and sys.argv[1] == "--local":
        # gets the current time and formats it HH:MM:SS
        current_time = datetime.datetime.now().time()

        formatted_time = current_time.strftime("%I:%M:%S %p")

        # Get the current date
        current_date = datetime.datetime.now().strftime("%m/%d/%Y")

        # easy way to read the root user function
        ROOT = 0

        def connect(url="https://google.com"):
            try:
                urllib.request.urlopen(url)  # Try to open a connection to the host
                return True  # If successful, return True
            except:
                return False  # If unsuccessful, return False

        # Makes sure that the user is connected to the internet    

        if platform.system() == OS:
            #checks if the user is running as root
            if os.geteuid() == ROOT:
                #makes the loading bar visible
                def print_loading_bar(iterations, delay=0.1, width=40):
                    """
                    Prints a loading bar with green dots to visualize progress.
                    
                    Args:
                        iterations (int): Total number of iterations.
                        delay (float, optional): Delay between updates in seconds. Default is 0.1 seconds.
                        width (int, optional): Width of the loading bar. Default is 40 characters.
                    """
                    for loadingBar in range(iterations + 1):
                        progress = loadingBar / iterations  # Calculate the progress ratio
                        bar_length = int(progress * width)  # Calculate the number of dots for the current progress
                        bar = GREEN + '•' * bar_length + RESET + ' ' * (width - bar_length)  # Construct the loading bar string
                        percentage = int(progress * 100)  # Calculate the percentage of completion
                        
                        # Print the loading bar and percentage, replacing the line each iteration
                        print(f'\rLoading {ProgramName} [{bar}] {percentage} % ', end='', flush=False)
                        
                        time.sleep(delay)  # Pause to control the update rate
                print_loading_bar(50)
                os.system("bash localScript.sh")  # the script to run after loading
            
            else:    
                # makes a pop up dialog to tell the user that the user is not root
                print(f"TIME:{formatted_time} Please run as ROOT. DATE:{current_date}")
                print(f"ERROR:TIME:{formatted_time} Please run as ROOT. DATE:{current_date}", file=ERROR)
        else:
            # makes a pop up dialog to tell the user that the OS is not correct
            # makes a pop up dialog to tell the user that the OS is not correct
            print(f"TIME:{formatted_time} Wrong OS. Please use the correct OS. DATE:{current_date}")
            print(f"WARNING:TIME:{formatted_time} Wrong OS. Please use the correct OS. DATE:{current_date}",file=ERROR)
    
    # puts the program in global mode
    else:
        # gets the current time and formats it HH:MM:SS
        current_time = datetime.datetime.now().time()

        formatted_time = current_time.strftime("%I:%M:%S %p")

        # Get the current date
        current_date = datetime.datetime.now().strftime("%m/%d/%Y")

        # easy way to read the root user function
        ROOT = 0

        def connect(host="google.com"):
            try:
                urllib.request.urlopen("http://" + host)  # Try to open a connection to the host
                return True  # If successful, return True
            except:
                return False  # If unsuccessful, return False

        # Makes sure that the user is connected to the internet    
        if connect() == True:
            #checks if the user is on Mac OS
            if platform.system() == OS:
                #checks if the user is running as root
                if os.geteuid() == ROOT:
                    #makes the loading bar visible
                    def print_loading_bar(iterations, delay=0.1, width=40):
                        """
                        Prints a loading bar with green dots to visualize progress.
                        
                        Args:
                            iterations (int): Total number of iterations.
                            delay (float, optional): Delay between updates in seconds. Default is 0.1 seconds.
                            width (int, optional): Width of the loading bar. Default is 40 characters.
                        """
                        for loadingBar in range(iterations + 1):
                            progress = loadingBar / iterations  # Calculate the progress ratio
                            bar_length = int(progress * width)  # Calculate the number of dots for the current progress
                            bar = GREEN + '•' * bar_length + RESET + ' ' * (width - bar_length)  # Construct the loading bar string
                            percentage = int(progress * 100)  # Calculate the percentage of completion
                            
                            # Print the loading bar and percentage, replacing the line each iteration
                            print(f'\rLoading {ProgramName} [{bar}] {percentage} % ', end='', flush=False)
                            
                            time.sleep(delay)  # Pause to control the update rate
                    print_loading_bar(50)
                    os.system("bash start.sh")  # the script to run after loading
                
                else:    
                    # makes a pop up dialog to tell the user that the user is not root
                    print(f"TIME:{formatted_time} Please run as ROOT. DATE:{current_date}")
                    print(f"ERROR:TIME:{formatted_time} Please run as ROOT. DATE:{current_date}", file=ERROR)
            else:
                # makes a pop up dialog to tell the user that the OS is not correct
                print(f"TIME:{formatted_time} Wrong OS. Please use the correct OS. DATE:{current_date}")
                print(f"WARNING:TIME:{formatted_time} Wrong OS. Please use the correct OS. DATE:{current_date}",file=ERROR)

        else:
            print(f"TIME:{formatted_time} Please connect to the internet. DATE:{current_date}")
            print(f"ERROR:TIME:{formatted_time} Please connect to the internet. DATE:{current_date}",file=ERROR)

# if the user uses control-c, the program will exit
except KeyboardInterrupt:
    print("\n[-]Exiting...")