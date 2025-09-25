import array

# -------------------------------
# Project 80: Alumni Donation Log
# -------------------------------

# Integers: donation amounts
donations = [500, 1200, 700, 1500, 300]

total_donations = sum(donations)
average_donation = total_donations / len(donations)
min_donation = min(donations)
max_donation = max(donations)

# Strings: formatted report using f-strings
report = (
    f"Alumni Donation Log Report\n"
    f"---------------------------\n"
    f"Total Donations: {total_donations}\n"
    f"Average Donation: {average_donation:.2f}\n"
    f"Minimum Donation: {min_donation}\n"
    f"Maximum Donation: {max_donation}\n"
)
print(report)

# Booleans: threshold check with compound condition
threshold = 800
if average_donation >= threshold and max_donation > 1000:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# Lists: add, remove, sort, and display
print("\n--- List Operations ---")
print("Original donations:", donations)

donations.append(900)  # Add a new donation
print("After adding 900:", donations)

# Remove donations less than 400
donations = [d for d in donations if d >= 400]
print("After removing <400:", donations)

donations.sort()
print("Sorted donations:", donations)

# Arrays: fixed-size numeric subset
donations_array = array.array('i', donations[:4])  # first 4 donations
array_sum = sum(donations_array)

print("\n--- Array Operations ---")
print("Array donations:", donations_array.tolist())
print("Sum of array donations:", array_sum)
print("Sum of list donations:", sum(donations))

# Dictionaries: list of donation records
donation_records = [
    {"id": 1, "name": "Alice", "value": 500},
    {"id": 2, "name": "Bob", "value": 1200},
    {"id": 3, "name": "Charlie", "value": 700},
    {"id": 4, "name": "Diana", "value": 1500},
]

print("\n--- Dictionary Operations ---")
print("Original records:", donation_records)

# Update Bob's donation
for record in donation_records:
    if record["id"] == 2:
        record["value"] = 1300

# Delete Charlie's record
donation_records = [r for r in donation_records if r["id"] != 3]

# Compute total donation from dictionary records
dict_total = sum(r["value"] for r in donation_records)

print("Updated records:", donation_records)
print("Total from dictionary records:", dict_total)
