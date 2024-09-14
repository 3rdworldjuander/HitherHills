# Hither Hills Booking Bot

## USAGE

$ *python hhbook_east.py __start_date__ __site__*

*where:*

- *__start_date__ = checkin date (must be sunday) in YYYY-MM-DD format*
- *__site__ = Number site ID*

### Site IDs - East Area

- G007 = 249565
- G008 = 249566
- G009 = 249568
- G0013 = 249571

- G0017 = 249575
- G0018 = 249576
- G0019 = 249471
  
## Notes

### Sample URL

<https://www.reserveamerica.com/explore/hither-hills-state-park/NY/297/249565/campsite-booking?availStartDate=2025-04-20&arrivalDate=2025-05-03&lengthOfStay=7>

### URL

<https://www.reserveamerica.com/explore/hither-hills-state-park/NY/297/{site}/campsite-booking?availStartDate={start_date}&arrivalDate={end_date}&lengthOfStay=7>

### URL with automatic select of 7 days

<https://www.reserveamerica.com/explore/hither-hills-state-park/NY/297/{site}/campsite-booking?availStartDate={start_date}&nextAvailableDate=false&arrivalDate={start_date}&lengthOfStay=7>

### Testing

Try with
G008 = 249566
start_date = 2025-04-27,

## Roadmap

### Auto-fill shopping cart

    page.get_by_text("Equipment", exact=True).click()
    page.get_by_label("Yes, I have read and").check()
    page.locator("#equipmentType").select_option("108060")
    page.locator("#numOfOccupants").click()
    page.locator("#numOfOccupants").fill("6")
    page.locator("#numOfVehicles").click()
    page.locator("#numOfVehicles").fill("1")
    page.get_by_role("button", name="Oamar Gianan").click()
    page.get_by_role("button", name="Continue to Cart").click()
    page.get_by_role("button", name="Abandon Cart").click()
    page.get_by_role("button", name="Yes").click()
