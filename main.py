#                                       VOCABULARY IMPROVING -- WORD OF THE DAY

from plyer import notification

import time

if __name__ == '__main__':
    file = open("Wordfile.txt", "r" , encoding='utf-8') # Improve the list when learning
    read_file = file.readlines()
    for vocabulary in read_file:
        notification.notify(title=" *** Word of the day *** ",  #Display Title
                            message=vocabulary.strip(),
                            app_icon="C:\\Users\\User\\Desktop\\Python`3_ Programming\\Desktop_Notifier\\Icon.ico", #Specify icon full path.

                            timeout=10) #specify how much tme in seconds the notification should last.
        time.sleep(60) # 60*60 = 1 hour
        #If you want it in a day put 60*60*24



