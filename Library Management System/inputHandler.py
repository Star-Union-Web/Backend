def handle_idx(idx, sz):
    is_correct = False

    while is_correct == False:
        if idx >= 0 and idx <= sz-1:
            is_correct = True
            
        if idx < 0:
            inp = input("Incorrect ID. Did you mean 0? (Y/N)")
            if "Y" in inp or "y" in inp:
                return 0
            else:
                idx = int(input("Please nter correct ID: "))
        elif idx > sz-1:
            inp = input(f"Incorrect ID. Did you mean {sz-1}? (Y/N)")
            if "Y" in inp or "y" in inp:
                return sz-1
            else:
                idx = int(input("Please nter correct ID: "))
    
    return int(idx)