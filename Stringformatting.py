country = "United States"
states = 50

# 1️⃣ C-style formatting with “%” operator (old-school)
print("%s has %d states." % (country, states))

# 2️⃣ Using .format() method (pre-Python 3.6)
print("{} has {} states.".format(country, states))

# 3️⃣ Using f-string (Python 3.6+)
print(f"{country} has {states} states.")

# Output: United States has 50 states.