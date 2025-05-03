import tkinter as tk
from tkinter import messagebox

# Function to show the terms and conditions window
def show_terms():
    # Create a top-level window
    terms_window = tk.Toplevel()
    terms_window.title("Terms and Conditions")
    terms_window.geometry("450x320")

    # Updated Terms and Conditions content
    terms_text = """
    SYSTEM TERMS AND CONDITIONS

    1. Only authorized users are allowed to access this system.
    2. All data entered will be stored securely and used for official purposes only.
    3. Unauthorized modification or duplication of system data is prohibited.
    4. System activity may be logged for monitoring and audit purposes.
    5. By clicking "Accept", you agree to follow all guidelines stated.

    Please read carefully before proceeding.
    """

    # Add a Label to display terms
    terms_label = tk.Label(terms_window, text=terms_text, justify="left", wraplength=420, anchor="w")
    terms_label.pack(padx=15, pady=15)

    # Add an "Accept" button
    accept_button = tk.Button(terms_window, text="Accept", command=terms_window.destroy)
    accept_button.pack(pady=10)

# Main window
root = tk.Tk()
root.title("Main System")
root.geometry("300x200")

# Button to open Terms and Conditions
terms_button = tk.Button(root, text="Show Terms and Conditions", command=show_terms)
terms_button.pack(pady=50)

root.mainloop()