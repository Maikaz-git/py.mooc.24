# Write your solution here

def formatted(lst:list)->list:
    result = []
    for nr in lst:
        result.append(f"{nr:.2f}")
    
    return result

if __name__=="__main__":
    outcome = formatted([1.234, 0.3333, 0.11111, 3.446])
    print(outcome)