# un programme pour calcule un pouboire
print("Tip Calculator\n")

# donne le prix de meal:
cost = float(input("Cost of meal:"))

# Calcul le pouboire et total amount
tip_percentage = [ 0.15 , 0.20 , 0.25 ]

# range(15,26,5) 
# for tip in range(0.15,0.26,0.05): 
for tip_percentage in tip_percentage :#[ 0.15, 0.20, 0.25 ]

    tip_cost = tip_percentage * cost # = round(tip_percentage * cost,2)
    total_cost = tip_cost + cost # = round(tip_cost + cost,2)

    # print pouboire 
    print(f"\n{int(tip_percentage*100)}% Tip:")
    if tip_cost.is_integer():
        print(f"Tip amout:  {int(tip_cost)}")
    elif round(tip_cost, 1) == tip_cost:
        print(f"Tip amout:  {tip_cost:.1f}")
    else:
        print(f"Tip amout:  {tip_cost:.2f}")
    # print total cost 
    if total_cost.is_integer():
        print(f"Total amout:{int(total_cost)}")
    elif round(total_cost, 1) == total_cost:
        print(f"Total amout:{total_cost:.1f}")
    else:
        print(f"Total amout:{total_cost:.2f}")
    
