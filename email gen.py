import random
import tkinter as tk
from tkinter import simpledialog, ttk, filedialog

# Expanded name lists
first_names = [
    "Alejandro", "Beatriz", "Carlos", "Diana", "Emiliano", "Fernanda", "Gabriel", "Hernando",
    "James", "Emily", "Michael", "Jessica", "David", "Ashley", "John", "Sarah", "Christopher", "Jennifer",
    "Daniel", "Elizabeth", "Matthew", "Samantha", "Joseph", "Amanda", "Anthony", "Brittany", "William",
    "Megan", "Jonathan", "Lauren", "Robert", "Katherine", "Kevin", "Olivia", "Nathan", "Sophia", "Justin",
    "Abigail", "Brian", "Isabella", "Ethan", "Grace", "Tyler", "Victoria", "Ryan", "Madison", "Jacob",
    "Natalie", "Brandon", "Kayla", "Austin", "Charlotte", "Joshua", "Faith", "Adam", "Savannah", "Nicholas",
    "Alyssa", "Benjamin", "Ella", "Patrick", "Lucas", "Daniela", "Juan", "Jose", "Miguel", "Pablo",
    "Ricardo", "Santiago", "Francisco", "Luis", "Fernando", "Eduardo", "Javier", "Manuel", "Diego",
    "Roberto", "Raul", "Adrian", "Cesar", "Julio", "Oscar", "Jorge", "Andres", "Alberto", "Marcos"
]

last_names = [
    "González", "Rodríguez", "Martínez", "Hernández", "Lopez", "Pérez", "Ramírez", "Torres",
    "Smith", "Johnson", "Brown", "Williams", "Jones", "Miller", "Davis", "Clark", "Taylor", "Moore",
    "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez",
    "Robinson", "Walker", "Young", "Allen", "King", "Wright", "Scott", "Green", "Baker", "Hall",
    "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker",
    "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan",
    "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres",
    "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett",
    "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson",
    "Hughes", "Flores", "Washington", "Butler", "Simmons", "Foster", "Gonzalez", "Bryant"
]

# Define suffix labels
suffix_labels = ["@gmail.com", "@yahoo.com", "@live.com"]

def generate_names():
    """Generate names with selected email suffixes as one continuous word."""
    num_names = simpledialog.askinteger("Input", "How many names do you want? (1-1000000)", minvalue=1, maxvalue=1000000)
    if num_names:
        name_list.delete(0, tk.END)  # Clear previous names

        selected_suffixes = [suffix.get() for suffix in email_options if suffix.get()]
        if not selected_suffixes:
            selected_suffixes = ["@gmail.com"]

        names = []
        for _ in range(num_names):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)

            for suffix in selected_suffixes:
                full_name = f"{first_name}{last_name}{suffix}"
                names.append(full_name)

        for name in names[:500]:  # Display the first 500 names
            name_list.insert(tk.END, name)

        return names  # Return full list for saving

def save_names():
    """Save currently displayed names in the listbox to an RTF file."""
    names = name_list.get(0, tk.END)  # Get all names from the listbox
    if names:
        file_path = filedialog.asksaveasfilename(defaultextension=".rtf", filetypes=[("Rich Text Format", "*.rtf")])
        if file_path:
            with open(file_path, "w") as file:
                file.write("{\\rtf1\\ansi\\deff0{\n")
                for name in names:
                    file.write(f"\\par {name}\n")
                file.write("}\n")
            print(f"Names saved to {file_path}")

def copy_all():
    """Copy all generated emails to clipboard."""
    all_names = name_list.get(0, tk.END)  # Get all names from the listbox
    if all_names:
        root.clipboard_clear()
        root.clipboard_append("\n".join(all_names))  # Copy all names, each on a new line
        root.update()

# Create GUI window
root = tk.Tk()
root.title("Name Generator")
root.geometry("500x450")

# Checkboxes for email suffix options
email_options = []
for label in suffix_labels:
    var = tk.StringVar(value="")
    chk = ttk.Checkbutton(root, text=label, variable=var, onvalue=label, offvalue="")
    chk.pack(anchor="w")
    email_options.append(var)

# Generate names button
generate_button = tk.Button(root, text="Generate Names", command=generate_names)
generate_button.pack(pady=10)

# Listbox for names
name_list = tk.Listbox(root, width=50, height=15)
name_list.pack()

# Save names button
save_button = tk.Button(root, text="Save Names as RTF", command=save_names)
save_button.pack(pady=5)

# Copy all names button
copy_all_button = tk.Button(root, text="Copy All Emails", command=copy_all)
copy_all_button.pack(pady=10)

# Run the GUI
root.mainloop()
