import numpy as np
import time

# Initialize random generator
rng = np.random.default_rng(42)
chars = np.array(list("abcdefghijklmnopqrstuvwxyz"))

# Generate 1,000,000 strings of length 10 by shuffling the chars array
random_chars = rng.choice(chars, size=(1_000_000, 10))

# Join characters row-wise into strings using list comprehension (fast enough for setup)
string_arr = np.array([''.join(row) for row in random_chars], dtype='U10')

# For-loop slicing benchmark
start = time.time()
sliced_loop = np.array([s[:5] for s in string_arr])
print("For-loop time:", round(time.time() - start, 4), "seconds")

# numpy.strings.slice benchmark
start = time.time()
sliced_np = np.strings.slice(string_arr, 0, 5)
print("numpy.strings.slice time:", round(time.time() - start, 4), "seconds")


customer_invoices = [
   
    '2346_账单_四月.pdf',               # Chinese
    '2347_فاتورة_مايو.pdf',                # Arabic
    '2🚀50_invoice_july.pdf',          # Emoji
]

# Create a NumPy array with StringDtype
invoices_array = np.array(customer_invoices,  dtype=np.dtypes.StringDType())

customer_id = np.strings.slice(invoices_array,[2,1,0] , [5,-1,-2])
print(customer_id)