import asyncio
import sys
import pandas as pd
from playwright.async_api import async_playwright
from dotenv import load_dotenv, dotenv_values
from datetime import datetime, timedelta
import requests
import hashlib
import time

LOGIN_PAGE = "https://www.reserveamerica.com/signin?landing=%2F"
SITE_SEARCH_PAGE = "https://www.reserveamerica.com/explore/hither-hills-state-park/NY/297/campsite-availability?arrivalDate=2025-06-15&availStartDate=2025-06-15&lengthOfStay=7&pageNumber=0"

async def setup_browser():
    playwright = await async_playwright().start()
    browser = await playwright.webkit.launch(headless=False, args=['--no-sandbox'])
    context = await browser.new_context(viewport={'width': 1280, 'height': 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
    page = await context.new_page()
    print('browser setup complete')
    return playwright, browser, context, page

async def login_process(page, page_url):
    print('Logging in')
    load_dotenv()
    config = dotenv_values()

    username = config.get("user")
    password = config.get("passwd")

    await page.goto(page_url)  
    html = await page.content()
    print('Login page loaded')

    await page.get_by_placeholder("Email").fill(username)
    await page.get_by_placeholder("Password").fill(password)
    await page.get_by_placeholder("Password").press("Enter")

def get_closest_sunday(date_str):
    # Convert the input string to a datetime object
    date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Get the day of the week (0 = Monday, 6 = Sunday)
    day_of_week = date.weekday()
    
    if day_of_week == 6:
        # If it's already Sunday, return the input date
        return date_str
    else:
        # Calculate days until the next Sunday
        days_until_sunday = 6 - day_of_week
        
        # Get the next Sunday
        next_sunday = date + timedelta(days=days_until_sunday)
        
        # Get the previous Sunday
        prev_sunday = date - timedelta(days=day_of_week + 1)
        
        # Determine which Sunday is closer
        if (date - prev_sunday) < (next_sunday - date):
            closest_sunday = prev_sunday
        else:
            closest_sunday = next_sunday
        
        # Return the closest Sunday in YYYY-MM-DD format
        return closest_sunday.strftime("%Y-%m-%d")

async def check_availability(page):
    # Locator for the cell
    cell_locator = 'a.base-link[role="button"] div.bg-available'
 
        # Check if the element exists on the page
    avail_count = await page.locator(cell_locator).count()
    is_available = avail_count > 0
    nights_avail = int(avail_count/2)

    # Print based on whether the element is found or not
    if is_available:
        print(f"There are {nights_avail} available dates on this site")
        for i in range(min(nights_avail,7)):
            # Click each element (nth element) using locator.nth(i)
            print(i)
            await page.get_by_label("Available").first.click()
            # Optionally, print which element is being clicked
            print(f"Clicked element {i + 1}")

    else:
        print(f"There are {nights_avail} available dates on this site")

async def is_it_in_cart(page):
    try:
        # Wait for the element to be visible with a timeout
        equipment_locator = await page.wait_for_selector("text=Equipment", state="visible")
        
        if equipment_locator:
            send_this = "Booking is in cart. Act fast!"
            print(send_this)
            send_sms_voipms(send_this)
        else:
            send_this = "No booking acquired"
            print(send_this)
            send_sms_voipms(send_this)
    except Exception as e:
        send_this = f"Error in getting cart status: {str(e)}"
        print(send_this)
        send_sms_voipms(send_this)

def send_sms_voipms(message):
    # Import settings here
    load_dotenv()
    config = dotenv_values()

    api_username = config.get("api_username")
    api_password = config.get("api_password")
    did = config.get("did")
    dst = config.get("dst")

    # VoIP.ms API endpoint
    url = "https://voip.ms/api/v1/rest.php"

    # Generate API timestamp
    api_timestamp = int(time.time())

    # Generate API MD5 hash
    api_hash = hashlib.md5(f"{api_username}{api_password}{api_timestamp}".encode()).hexdigest()

    # Prepare the parameters
    params = {
        "api_username": api_username,
        "api_password": api_password,
        "method": "sendSMS",
        "did": did,
        "dst": dst,
        "message": message,
        "api_timestamp": api_timestamp,
        "api_hash": api_hash
    }

    # Send the request
    response = requests.get(url, params=params)

    # Check the response
    if response.status_code == 200:
        result = response.json()
        if result["status"] == "success":
            print(f"SMS sent successfully. Message ID: {result['sms']}")
        else:
            print(f"Failed to send SMS. Error: {result['status']}")
    else:
        print(f"HTTP request failed. Status code: {response.status_code}")


async def main():

    start_date = sys.argv[1]
    site = sys.argv[2]

    SELECT_7_SITE = f"https://www.reserveamerica.com/explore/hither-hills-state-park/NY/297/{site}/campsite-booking?availStartDate={start_date}&nextAvailableDate=false&arrivalDate={start_date}&lengthOfStay=7"

    playwright, browser, context, page = await setup_browser()
    await login_process(page, LOGIN_PAGE)
    await page.goto(SELECT_7_SITE)
    await page.get_by_role("button", name="Book Now").click()
    await asyncio.sleep(10)
    await is_it_in_cart(page)

    input('Press enter to continue...')

    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())