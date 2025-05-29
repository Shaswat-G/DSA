class Computer:
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.storage = None
        self.graphics_card = None
        self.motherboard = None
        self.power_supply = None
        self.case = None
        self.price = 0

    def __str__(self):
        specs = []
        if self.cpu:
            specs.append(f"CPU: {self.cpu}")
        if self.memory:
            specs.append(f"RAM: {self.memory}")
        if self.storage:
            specs.append(f"Storage: {self.storage}")
        if self.graphics_card:
            specs.append(f"GPU: {self.graphics_card}")
        if self.motherboard:
            specs.append(f"Motherboard: {self.motherboard}")
        if self.power_supply:
            specs.append(f"PSU: {self.power_supply}")
        if self.case:
            specs.append(f"Case: {self.case}")
        specs.append(f"Total Price: ${self.price}")
        return "\n".join(specs)


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu, price=0):
        self.computer.cpu = cpu
        self.computer.price += price
        return self

    def set_memory(self, memory, price=0):
        self.computer.memory = memory
        self.computer.price += price
        return self

    def set_storage(self, storage, price=0):
        self.computer.storage = storage
        self.computer.price += price
        return self

    def set_graphics_card(self, gpu, price=0):
        self.computer.graphics_card = gpu
        self.computer.price += price
        return self

    def set_motherboard(self, motherboard, price=0):
        self.computer.motherboard = motherboard
        self.computer.price += price
        return self

    def set_power_supply(self, psu, price=0):
        self.computer.power_supply = psu
        self.computer.price += price
        return self

    def set_case(self, case, price=0):
        self.computer.case = case
        self.computer.price += price
        return self

    def build(self):
        # Validation could go here
        if not self.computer.cpu:
            raise ValueError("CPU is required")
        if not self.computer.memory:
            raise ValueError("Memory is required")
        return self.computer


# Usage
gaming_pc = (
    ComputerBuilder()
    .set_cpu("Intel i9-13900K", 600)
    .set_memory("32GB DDR5", 200)
    .set_storage("1TB NVMe SSD", 150)
    .set_graphics_card("RTX 4080", 1200)
    .set_motherboard("ASUS Z790", 300)
    .set_power_supply("850W Gold", 150)
    .set_case("Fractal Define 7", 100)
    .build()
)

office_pc = (
    ComputerBuilder()
    .set_cpu("Intel i5-13600", 300)
    .set_memory("16GB DDR4", 80)
    .set_storage("512GB SSD", 60)
    .set_motherboard("Basic B660", 100)
    .set_power_supply("500W Bronze", 60)
    .set_case("Basic Mid Tower", 40)
    .build()
)

print("Gaming PC:")
print(gaming_pc)
print("\nOffice PC:")
print(office_pc)


class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_gaming_pc(self):
        return (
            self.builder.set_cpu("Intel i9-13900K", 600)
            .set_memory("32GB DDR5", 200)
            .set_storage("1TB NVMe SSD", 150)
            .set_graphics_card("RTX 4080", 1200)
            .set_motherboard("ASUS Z790", 300)
            .set_power_supply("850W Gold", 150)
            .set_case("Fractal Define 7", 100)
            .build()
        )

    def build_office_pc(self):
        return (
            self.builder.set_cpu("Intel i5-13600", 300)
            .set_memory("16GB DDR4", 80)
            .set_storage("512GB SSD", 60)
            .set_motherboard("Basic B660", 100)
            .set_power_supply("500W Bronze", 60)
            .set_case("Basic Mid Tower", 40)
            .build()
        )

    def build_budget_pc(self):
        return (
            self.builder.set_cpu("AMD Ryzen 5 5600", 150)
            .set_memory("16GB DDR4", 60)
            .set_storage("256GB SSD", 40)
            .set_motherboard("Basic B450", 70)
            .set_power_supply("400W Bronze", 40)
            .set_case("Budget Case", 25)
            .build()
        )


# Usage with Director
director = ComputerDirector(ComputerBuilder())
gaming_pc = director.build_gaming_pc()
budget_pc = director.build_budget_pc()


# ---------------------------------------------
class SQLQueryBuilder:
    def __init__(self):
        self.query_parts = {
            "select": [],
            "from": "",
            "joins": [],
            "where": [],
            "group_by": [],
            "having": [],
            "order_by": [],
            "limit": None,
        }

    def select(self, *columns):
        self.query_parts["select"].extend(columns)
        return self

    def from_table(self, table):
        self.query_parts["from"] = table
        return self

    def where(self, condition):
        self.query_parts["where"].append(condition)
        return self

    def join(self, table, condition):
        self.query_parts["joins"].append(f"JOIN {table} ON {condition}")
        return self

    def order_by(self, column, direction="ASC"):
        self.query_parts["order_by"].append(f"{column} {direction}")
        return self

    def limit(self, count):
        self.query_parts["limit"] = count
        return self

    def build(self):
        query = f"SELECT {', '.join(self.query_parts['select'])}"
        query += f" FROM {self.query_parts['from']}"

        if self.query_parts["joins"]:
            query += " " + " ".join(self.query_parts["joins"])

        if self.query_parts["where"]:
            query += " WHERE " + " AND ".join(self.query_parts["where"])

        if self.query_parts["order_by"]:
            query += " ORDER BY " + ", ".join(self.query_parts["order_by"])

        if self.query_parts["limit"]:
            query += f" LIMIT {self.query_parts['limit']}"

        return query


# Usage
query = (
    SQLQueryBuilder()
    .select("users.name", "profiles.email", "COUNT(orders.id) as order_count")
    .from_table("users")
    .join("profiles", "users.id = profiles.user_id")
    .join("orders", "users.id = orders.user_id")
    .where("users.active = 1")
    .where("orders.created_at > '2023-01-01'")
    .order_by("order_count", "DESC")
    .limit(10)
    .build()
)

print(query)


# --------------------------------------------------------------------------
class HTTPRequestBuilder:
    def __init__(self):
        self.method = "GET"
        self.url = ""
        self.headers = {}
        self.params = {}
        self.body = None
        self.timeout = 30

    def get(self, url):
        self.method = "GET"
        self.url = url
        return self

    def post(self, url):
        self.method = "POST"
        self.url = url
        return self

    def header(self, key, value):
        self.headers[key] = value
        return self

    def param(self, key, value):
        self.params[key] = value
        return self

    def json_body(self, data):
        self.body = data
        self.header("Content-Type", "application/json")
        return self

    def timeout_seconds(self, seconds):
        self.timeout = seconds
        return self

    def build(self):
        return {
            "method": self.method,
            "url": self.url,
            "headers": self.headers,
            "params": self.params,
            "body": self.body,
            "timeout": self.timeout,
        }


# Usage
request = (
    HTTPRequestBuilder()
    .post("https://api.example.com/users")
    .header("Authorization", "Bearer token123")
    .header("User-Agent", "MyApp/1.0")
    .json_body({"name": "John", "email": "john@example.com"})
    .timeout_seconds(60)
    .build()
)

#-----------------------------------------------------------------------------------------------