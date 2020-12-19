def seat_converter(seat):
    row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
    column = int(seat[7:].replace('L', '0').replace('R', '1'), 2)
    
    return row * 8 + column
    

def result(input_):
    boarding_passes = [seat_converter(seat) for seat in input_]
    
    part_one = max(boarding_passes)
    part_two = set(range(min(boarding_passes), max(boarding_passes))) - set(boarding_passes)
    
    return (part_one, next(iter(part_two)))
