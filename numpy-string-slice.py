import numpy as np

'''
This program is written for pythonsnacks.com
function: numpy.strings.slice
Usecase: Extracting customer id from invoices'
filename using numpy.strings.slice and demonstrating dtype
'''

customer_invoices = np.array([
   
    '2346_账单_四月.pdf',               # Chinese
    '2347_فاتورة_مايو.pdf',           # Arabic
    '2🚀50_invoice_july.pdf',          # Emoji
])

# Create a NumPy array with StringDtype
invoices_array = np.array(customer_invoices,  dtype=np.dtypes.StringDType())

customer_id = np.strings.slice(invoices_array,[2,1,0] , [5,-1,-2])
print(customer_id)
customer_invoices = np.array([
                     '2346_invoice_jan.pdf',
                     '2347_invoice_jan.pdf',
                     '2348_invoice_jan.pdf'
                      ])


customer_id = np.strings.slice(customer_invoices, [3,2,1], [4,-1,-2])
print(customer_id)