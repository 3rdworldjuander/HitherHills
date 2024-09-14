from datetime import datetime, timedelta

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
