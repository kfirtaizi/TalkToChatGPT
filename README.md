# TalkToChatGPT
A python project to remotely ask ChatGPT questions (Wake it up with a wakeword) and make ChatGPT speak the answer out loud, with no user interaction.

# Prerequisite
* Windows Operating system (Tested on Windows 10)
* Have python installed (Tested on Python 3.10)

# Installation
After downloading the project and extracting it (Press on Code -> Download ZIP),  
navigate to the path of the project (where `start_gui.py` resides), and create a virtual environment for the project by:  
- `python -m venv venv`  
Let it finish.  
- `venv\Scripts\activate`  
- `pip install -r requirements.txt`  
Let the packages install completely.  

# Running and configuring
**IMPORTANT NOTE**: You can configure your wakeword in the GUI, but it will always start with `OK`. So if I want my wakeword to be Google and I configure `(OK) Google`, to wake it up I will have to say `OK Google`.  

In the main directory of the project simply run:  
- (If not already running the virtual environment) `venv\Scripts\activate`
- `python start_gui.py`  
This GUI should pop up:  
![image](https://user-images.githubusercontent.com/44837286/211014433-14d82242-5fb4-4d86-a6e9-8c354447de18.png)

Configure it to your liking, press Start, and at the first run a new login for ChatGPT will pop up which will require you to login just one time.
I don't recommend usign your main email with your main password (In any third party program) - use an alt instead if you wish.

* Profile Name is the chrome profile that will be created for you the first time you're running this program. It is there to start with the cookies of this profile for you to not need to login everytime to ChatGPT. I recommend just keeping it `TalkToChatGPT` as it will automatically create a new profile with this name for you. If you want to use your existing profile change the name to the name of your profile as it shows (as a folder) in: `C:\Users\<username>\AppData\Local\Google\Chrome\User Data`

From now on you can leave this program running in the background, lay in bed, talk to it and hear the answers.

**NOTE**: The program is pretty buggy at the moment because I didn't feel like fixing all the details (Maybe in the future if there will be demand), but it should work good if you just press Start and let it do its thing.
