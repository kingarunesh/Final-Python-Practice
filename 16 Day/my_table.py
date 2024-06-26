import os
from prettytable import PrettyTable


clear = lambda: os.system("cls")
clear()

print("🙏 Sita Ram 🙏\n")


table = PrettyTable()

table.field_names = ["City", "Visited"]
table.add_row(["Delhi", "Yes"])
table.add_row(["Mumbai", "No"])
table.add_row(["Chennai", "Yes"])
table.add_row(["Bangalore", "Yes"])
table.add_row(["Pune", "No"])
table.add_row(["Noida", "No"])
table.add_row(["Gurugram", "No"])
table.add_row(["Patna", "Yes"], divider=True)
table.add_row(["Jammu", "Yes"])

print(table.align)
table.align = "l"
print(table.align)


print(table)


angela = PrettyTable()

angela.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
angela.add_column("Type", ["Electric", "Water", "Fire"])

angela.align = "r"
print(angela)