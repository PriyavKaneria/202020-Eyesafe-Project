1. first check whether you linux distro has python3 installed or not. if not installed follow step 2 otherwise proceed with step 3 ( to check for python3 run the command "python3 --version" or "which python3" and you must see an output not an error)

2. to install python3
    i. ubuntu based distros -: run command "sudo apt install python3" in the terminal 
    ii. red-hat based distros -: run command "sudo yum install python3" in the terminal
    iii. for suse and opensuse -: run command "sudo zypper install python3" in the terminal
    iv. for arch based distros -: run command "sudo pacman -s python3" in the terminal

3. place the file "20-20-20-Eyesafe-project.py" anywhere in you home directory.

4. copy the location of directory in which "20-20-20-Eyesafe-project.py" file is placed

5. open terminal and run command "sudo nano ~/.bashrc"

6. a document inside nano editor must have opened after line 5 command, at the end of that document write "export eyesafe="path/to/directory/which/you/copied"

7. press (control + s) then press (control + x) and then run the command "source ~/.bashrc"

8. now whenever you want to run the service just write the commad "cd $eyesafe && python3 20-20-20-Eyesafe-project.py"


ENJOY~~~~!!!!!!~
