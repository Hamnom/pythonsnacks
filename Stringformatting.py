country = "United States"
count = 50

# 1️⃣ C-style formatting with “%” operator (old-school)
print("%s has %d states." % (country, count))

# 2️⃣ Using .format() method (pre-Python 3.6)
print("{} has {} states.".format(country, count))

# 3️⃣ Using f-string (Python 3.6+)
print(f"{country} has {count} states.")

# Output: United States has 50 states.