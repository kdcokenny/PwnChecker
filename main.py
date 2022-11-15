from check_domains import check_domains
from check_emails import check_emails
from add_new_breaches import add_new_breaches
from config import TIME_TO_RUN
import schedule, time

def main():
    print("Sorting through and ingesting new breaches...\n")
    add_new_breaches()
    print("Completed.\n")
    print("Checking domains for breaches...\n")
    check_domains()
    print("Completed.\n")
    print("Checking domains for breaches...\n")
    check_emails() #change to sort through humio
    print("Completed.\n")
    
    return 0

# Run every day
schedule.every().day.at(TIME_TO_RUN).do(main)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute