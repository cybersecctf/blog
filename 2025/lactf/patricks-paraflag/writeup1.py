def unscramble_flag(target):
    # Length of the target
    target_len = len(target)
    
    # Validate that target length is even
    if target_len % 2 != 0:
        raise ValueError("Target length must be even.")
    
    # Half length of the target
    half_len = target_len // 2
    
    # Unscramble the target
    part1 = target[0::2]  # Characters at even indices
    part2 = target[1::2]  # Characters at odd indices
    
    # Reconstruct the original input
    inp = part1 + part2
    return inp

# Given target
target = "l_alcotsft{_tihne__ifnlfaign_igtoyt}"

# Unscramble the flag
flag = unscramble_flag(target)
print(f"Recovered Flag: {flag}")
