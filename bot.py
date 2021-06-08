from simple_hacker import cybok
import time
import schedule


with open(r'users.txt', 'r') as f:
    users = [line.strip() for line in f]

print(users)

# Auto login
insta = cybok(username='samay_826', password='arpita9423', headless=False)

def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(0)


def msg():
    for user in users:  
        # Send message
        insta.sendMessage(user=user, message='''OUR TEAM NEW WEBSITE AND APPLICATION IS NOW LAUNCHED 
PLEASE SHARE AND SUPPORT ❤️

Visit Our Website
yamhackers.com

Our New Launched Application Link 
https://www.mediafire.com/file/uwwwrouxs9fenfh/YAM_HACKERS.apk/file

Our All Social Media Links
https://linktr.ee/yamhackers''')
        
### message sent everyday at 01:05
### 24 HH:MM format
schedule.every().day.at("01:05").do(msg)



if __name__ == '__main__':
    msg()
    scheduler()

