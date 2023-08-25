class FlightTable:
    def __init__(self):
        self.data = []
    
    def add_entry(self, p_id, process, start_time, priority):
        self.data.append((p_id, process, start_time, priority))
    
    def bubble_sort(self, key_func):
        n = len(self.data)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if key_func(self.data[j]) > key_func(self.data[j + 1]):
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
    
    def display(self):
        print("{:<5} {:<10} {:<10} {:<10}".format("P_ID", "Process", "Start Time", "Priority"))
        for entry in self.data:
            print("{:<5} {:<10} {:<10} {:<10}".format(entry[0], entry[1], entry[2], entry[3]))


# Define a key function for sorting by P_ID
def sort_by_p_id(entry):
    return entry[0]

# Define a key function for sorting by Start Time
def sort_by_start_time(entry):
    return entry[2]

# Define a key function for sorting by Priority
def sort_by_priority(entry):
    priority_mapping = {"Low": 0, "MID": 1, "High": 2}
    return priority_mapping[entry[3]]

# Main program
if __name__ == "__main__":
    table = FlightTable()
    
    table.add_entry(100, "VSCode", 234, "MID")
    table.add_entry(23, "Eclipse", 189, "MID")
    table.add_entry(93, "Chrome", 9, "High")
    table.add_entry(42, "JDK", 23, "High")
    table.add_entry(9, "CMD", 7, "Low")
    table.add_entry(87, "NotePad", 23, "Low")
    
    sort_options = {
        1: sort_by_p_id,
        2: sort_by_start_time,
        3: sort_by_priority
    }
    
    print("Original Table:")
    table.display()
    
    while True:
        print("\nSort Options:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Quit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 4:
            break
        
        if choice in sort_options:
            table.bubble_sort(sort_options[choice])
            print("\nSorted Table:")
            table.display()
        else:
            print("Invalid choice. Please select a valid option.")
