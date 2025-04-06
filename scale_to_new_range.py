num = float(input("Please input the number to be scaled: "))
old_min = 0
old_max = 100
new_min = 1 
new_max = 5 

# Get the offset from old range start, generalize it, apply it to the new range.
def scale_to_new_range(num, old_min, old_max, new_min, new_max):
    old_start_offset = num - old_min
    offset_fraction_of_old_range = old_start_offset / (old_max - old_min)
    new_start_offset = offset_fraction_of_old_range * (new_max - new_min)
    scaled_num = new_min + new_start_offset
    return scaled_num

print(scale_to_new_range(num, old_min, old_max, new_min, new_max))
