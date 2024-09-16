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
  
## Schedule run in MacOS using launchd

- copy plist file to ~/Library/LaunchAgents/
- chmod 644 ~/Library/LaunchAgents/com.hitherhills
- launchctl load ~/Library/LaunchAgents/com.hitherhills

When done booking

- kill pid of running script
- unload using launchctl unload ~/Library/LaunchAgents/com.hitherhills

## Notes

### Sample URL

<https://www.reserveamerica.com/explore/hither-hills-state-park/NY/297/249568/campsite-booking?availStartDate=2025-06-15&arrivalDate=2025-06-15&lengthOfStay=7>

### URL with automatic select of 7 days (change 7 for number of days selected)

<https://www.reserveamerica.com/explore/hither-hills-state-park/NY/297/{site}/campsite-booking?availStartDate={start_date}&nextAvailableDate=false&arrivalDate={start_date}&lengthOfStay=7>

### Testing

Try with
G008 = 249566
start_date = 2025-04-27,

<https://www.reserveamerica.com/explore/hither-hills-state-park/NY/297/249566/campsite-booking?availStartDate=2025-04-18&nextAvailableDate=false&arrivalDate=2025-04-18&lengthOfStay=2>

<https://www.reserveamerica.com/explore/hither-hills-state-park/NY/297/249565/campsite-booking?availStartDate=2025-04-18&nextAvailableDate=false&arrivalDate=2025-04-18&lengthOfStay=2>

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

## Heckscher State Park, NY

Cot1__4 = 278470
Cot2__6_stairs = 278518
Cot3__4 = 278517
Cot4__4 = 278469
Cot5__6_stairs = 278516
Cot6__4 = 278468
Cot7__4 = 278467
Cot8__6_stairs = 278471
Cot9__4 = 278466
Cot10__4 = 278166
Cot11__6_spiral = 277766
Cot12__2 = 277816
Cot13__2 = 277817
Cot14__2 = 277818
Cot15__2 = 277819

<https://www.reserveamerica.com/explore/heckscher-state-park/NY/277/277817/campsite-booking?availStartDate=2025-06-13&nextAvailableDate=false&arrivalDate=2025-07-11&lengthOfStay=2>

2024 Cottage Season Schedule

Cottages 4, 6, 9, 11, 15
Non-Peak (2-night minimum stay): Friday, April 26, 2024 - Tuesday, June 18, 2024
Peak pricing applies to Memorial Day Weekend: Friday, May 24, 2024 – Sunday, May 26, 2024
CORE (7-night minimum stay, Wednesday to Wednesday): Wednesday, June 19, 2024 – Tuesday, August 27, 2024
Non-Peak (3-night minimum stay): Wednesday, August 28, 2024 - Monday, October 14, 2024
Peak pricing applies to Columbus Day Weekend: Friday, October 11, 2024 - Monday, October 14, 2024
Non-Peak (2-night minimum stay): Tuesday, October 15, 2024 - Saturday, October 19, 2024

Cottages 1, 3, 5, 7, 13
Non-Peak (2-night minimum stay): Friday, April 26, 2024 - Wednesday, June 19, 2024
Peak pricing applies to Memorial Day Weekend: Friday, May 24, 2024 – Sunday, May 26, 2024
CORE (7-night minimum stay, Thursday to Thursday): Thursday, June 20, 2024 – Wednesday, August 28, 2024
Non-Peak (3-night minimum stay): Thursday, August 29, 2024 - Monday, October 14, 2024
Peak pricing applies to Columbus Day Weekend: Friday, October 11, 2024 - Monday, October 14, 2024
Non-Peak (2-night minimum stay): Tuesday, October 15, 2024 - Saturday, October 19, 2024

Cottages 2, 8, 10, 12, 14
Non-Peak (2-night minimum stay): Friday, April 26, 2024 – Thursday, June 20, 2024
Peak pricing applies to Memorial Day Weekend: Friday, May 24, 2024 – Sunday, May 26, 2024
CORE (7-night minimum stay, Friday to Friday): Friday, June 21, 2024 – Thursday, August 29, 2024
Non-Peak (3-night minimum stay): Friday, August 30, 2024 - Monday, October 14, 2024
Peak pricing applies to Columbus Day Weekend: Friday, October 11, 2024 - Monday, October 14, 2024
Non-Peak (2-night minimum stay): Tuesday, October 15, 2024 - Saturday, October 19, 2024

1 Bedroom Cottages
12, 13, 14, 15
Max Occupancy 4
1 Queen bed
Pull-out sofa

2 Bedroom Cottages
1, 3, 4, 6, 7, 9, 10
Max Occupancy 6
1 Queen bed
2 Twin beds
Pull-out sofa

2 Bedroom Cottages with Loft
2, 5, 8, 11
Max Occupancy 8
1 Queen bed
4 Twin beds
Pull-out sofa

Each Cottage is equipped with a refrigerator/freezer and ice cube trays, stovetop, oven, microwave, toaster, coffee maker, dish rack, cutting board, broom, dustpan, mop, paper towel holder, toilet paper and garbage bags.
Cottages have propane heat, wi-fi and air-conditioning.
Patio table with seating to match capacity, 2 Adirondack chairs, 2 longue chairs, small side table and metal firepit with grill.

Guests are encouraged to bring:
• bedding, pillows, and linens
• kitchen and bath towels
• toiletries and cleaning supplies
• cookware, utensils, and oven mitts
• plates, bowls, cups, flatware, and cutlery
• can and bottle openers
• firewood (purchase or source locally)
