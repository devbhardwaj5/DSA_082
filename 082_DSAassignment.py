# -------------------------------
# Weather Data Storage System
# -------------------------------

# Step 1: Define the Weather Record ADT
class WeatherRecord:
    def __init__(self, date, city, temperature):
        self.date = date          # format: YYYY-MM-DD
        self.city = city          # e.g., "Delhi"
        self.temperature = temperature  # e.g., 30.5 °C

    def __str__(self):
        return f"{self.date} | {self.city} | {self.temperature}°C"


# Step 2: 2D Array-based Storage System
class WeatherDataSystem:
    def __init__(self, years, cities):
        """
        Initialize a 2D array with sentinel value None.
        Rows = years, Columns = cities
        """
        self.years = years
        self.cities = cities
        self.data = [[None for _ in range(len(cities))] for _ in range(len(years))]

    def insert(self, year, city, record):
        """Insert weather record at (year, city)"""
        row = self.years.index(year)
        col = self.cities.index(city)
        self.data[row][col] = record

    def retrieve(self, year, city):
        """Retrieve weather record"""
        row = self.years.index(year)
        col = self.cities.index(city)
        return self.data[row][col]

    def delete(self, year, city):
        """Delete weather record by replacing with None"""
        row = self.years.index(year)
        col = self.cities.index(city)
        self.data[row][col] = None

    # Step 3: Row-major and Column-major access
    def row_major_traversal(self):
        """Visit records row by row"""
        print("Row-major traversal:")
        for i in range(len(self.years)):
            for j in range(len(self.cities)):
                if self.data[i][j] is not None:
                    print(self.data[i][j])

    def column_major_traversal(self):
        """Visit records column by column"""
        print("Column-major traversal:")
        for j in range(len(self.cities)):
            for i in range(len(self.years)):
                if self.data[i][j] is not None:
                    print(self.data[i][j])

    # Step 4: Sparse Data Handling
    def display_sparse_matrix(self):
        """Show only stored data (skip None values)"""
        print("Sparse data representation:")
        for i in range(len(self.years)):
            for j in range(len(self.cities)):
                record = self.data[i][j]
                if isinstance(record, WeatherRecord):
                    print(f"[{self.years[i]}, {self.cities[j]}] -> {record.temperature}°C")

    # Step 5: Complexity Analysis
    def complexity_analysis(self):
        print("\n--- Time & Space Complexity ---")
        print("Insert: O(1)   (direct index access)")
        print("Retrieve: O(1) (direct index access)")
        print("Delete: O(1)   (direct index access)")
        print("Row/Column Traversal: O(N*M) where N=years, M=cities")
        print("Space: O(N*M) for full matrix, reduced if using sparse methods")


# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    years = [2024, 2025]
    cities = ["Delhi", "Mumbai", "Chennai"]

    system = WeatherDataSystem(years, cities)

    # Insert some records
    system.insert(2024, "Delhi", WeatherRecord("2023-06-01", "Delhi", 35.5))
    system.insert(2025, "Mumbai", WeatherRecord("2023-06-01", "Mumbai", 30.2))
    system.insert(2024, "Chennai", WeatherRecord("2024-06-01", "Chennai", 34.1))

    # Retrieve a record
    print("\nRetrieve Example:")
    print(system.retrieve(2024, "Delhi"))

    # Traversals
    print()
    system.row_major_traversal()
    print()
    system.column_major_traversal()

    # Sparse representation
    print()
    system.display_sparse_matrix()

    # Complexity
    system.complexity_analysis()
