print("""

█▀ ▀█▀ █▀█ █▀▀ █▄▀   █▀█ █▀█ █▀█ █▀▀ █ ▀█▀   █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
▄█ ░█░ █▄█ █▄▄ █░█   █▀▀ █▀▄ █▄█ █▀░ █ ░█░   █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄

                                                                        by: Ryan.
""")
print("""
NS is the number of shares,

SP is the selling price per share,

BP is the buying price per share,
""")
print("-"*150)
ns = int(input("Enter NS >"))
sp = int(input("Enter SP >"))
bp = int(input("Enter BP >"))
currency = input("Enter Currency >")

profit = ((sp*ns)-(bp*ns))
print(f"Your profit is {currency} {profit}")
