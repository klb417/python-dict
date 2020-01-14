stockDict = {
    "GM": "General Motors",
    "CAT": "Caterpillar",
    "EK": "Eastman Kodak",
    "GE": "General Electric"
}

purchases = [
    ('GE', 100, '10-sep-2001', 48),
    ('CAT', 100, '1-apr-1999', 24),
    ('CAT', 50, '1-jan-1999', 30),
    ('GE', 200, '1-jul-1998', 56),
    ('GM', 150, '1-mar-1997', 36),
    ('GM', 100, '1-dec-1996', 40),
    ('GM', 150, '1-mar-1996', 38),
    ('EK', 200, '20-feb-1996', 42)
]


for purchase in purchases:
    print(
        f"I purchased {stockDict[purchase[0]]} stock for ${purchase[1] * purchase[3]}")

portfolio = {}

for purchase in purchases:
    if portfolio.get(purchase[0]):
        portfolio[purchase[0]].append([purchase[1], purchase[2], purchase[3]])
    else:
        portfolio[purchase[0]] = [[purchase[1], purchase[2], purchase[3]]]

for (key, value) in portfolio.items():
    print(f"------ {key} ------")
    totalValue = 0
    for item in value:
        totalValue += item[0] * item[2]
        print(f"{item[0]} shares at {item[2]} dollars each on {item[1]}")
    print(f"\nTotal value of stock in portfolio: ${totalValue}")
