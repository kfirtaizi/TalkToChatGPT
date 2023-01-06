# TalkToChatGPT
A python project to remotely ask ChatGPT questions and make ChatGPT speak the answer out loud, with no user interaction.

# Prerequisite
* Windows Operating system (Tested on Windows 10)
* Have python installed (tested on Python 3.10)

# Installation
After downloading the project and extracting it (Press on Code -> Download ZIP: https://github.com/kfirtaizi/TalkToChatGPT/archive/refs/heads/main.zip),
navigate to the path of the project (where `start_gui.py` resides), and create a virtual environment for the project by:  
`python -m venv venv`  
Let it finish.  
`venv\Scripts\activate`  
`pip install -r requirements.txt`  
Let the packages install completely.  

# Running and configuring
In the main directory of the project simply run:  
`python start_gui.py`  
This GUI should pop up:  
![image](https://user-images.githubusercontent.com/44837286/211004450-92f3715f-4312-485a-acdf-0b40de5514f2.png)

Configure it to your liking, press Start, and at the first run a new login for ChatGPT will pop up which will require you to login just one time.
I don't recommend usign your main email with your main password (In any third party program) - use an alt instead if you wish.

From now on you can leave this program running in the background, lay in bed, talk to it and hear the answers.

NOTE: The program is pretty buggy at the moment because I didn't feel like fixing all the details (Maybe in the future if there will be demand), but it should work good if you just press Start and let it do its thing.
