import tkinter as tk

window = tk.Tk()
window.title("Discount Calculator")
window.geometry("400x200")

# Price label & input
label_price = tk.Label(window, text="Original Price: ") 
label_price.pack()

entry_price = tk.Entry(window)
entry_price.pack()

# Discount label & input
label_discount = tk.Label(window, text="Discount (%): ")
label_discount.pack()

entry_discount = tk.Entry(window)
entry_discount.pack()

# Calculate & show result
def calculate():
  price = float(entry_price.get())
  discount = float(entry_discount.get())
  final = ((100 - discount) * 0.01) * price
  label_result.config(text=f"Final Price: Rp{final:,.2f}")
  
    
# Button
button = tk.Button(window, text="Calculate", command=calculate)
button.pack(pady=10)

# Result label
label_result = tk.Label(window, text="Final Price: Rp")
label_result.pack()

window.mainloop()

