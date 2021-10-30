# Hangman

This is a simple version of the Hangman game written in Python for the CLI (Command Line Interface).

## Set-up

If you to manually set up the program, you'll need a few things first. It'll depend on your OS, so follow the guide for yours below. If you just want the .exe file, go here to download the latest one. 

### Linux

1. You'll first need to install Python 3. If you already have Python 3.8 or above, this step can be skipped. Run `sudo apt install python3` in a terminal to install this.
2. Next, install Git. If you've already installed it, skip this step. Run `sudo apt-get install git` to install it.
3. Now, run this set of commands to finish the setup.
```bash
$ cd ~
$ git clone https://github.com/C-ffeeStain/Hangman.git
$ cd hangman
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
4. You're done! Now you can open the Hangman directory that's in your ~ directory (home) in a code 
editor to start helping with development.

### Windows

1. Install Python 3.8 or greater from https://python.org/downloads/. You can skip this step if you've already installed Python 3.8 or greater.
2. Install Git from https://git-scm.com/download/win. Again, you can also skip this step if Git is already installed on your machine.
3. Type "cmd" into the Windows search bar, and open it. Run these commands in it to finish the setup:
```bat
cd %userprofile%
git clone https://github.com/C-ffeeStain/Hangman.git
cd Hangman
py -m venv venv
"venv/bin/activate.bat"
pip install -r requirements.txt
```
4. You're finished! Now, you can execute the main file by running `py src/main.py` while in the Hangman folder.

## P-Bug Builds
Probably Buggy, or P-Bug for short, builds are special versions of the program that are untested, so they most likely contain bugs. Feel free to download these, but please report any bugs to this link.
