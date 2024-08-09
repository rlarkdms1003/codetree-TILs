x1_1, y1_1, x2_1, y2_1 = map(int, input().split())
x1_2, y1_2, x2_2, y2_2 = map(int, input().split())

x_overlap_start = max(x1_1, x1_2)
x_overlap_end = min(x2_1, x2_2)
y_overlap_start = max(y1_1, y1_2)
y_overlap_end = min(y2_1, y2_2)

overlap_width = max(0, x_overlap_end - x_overlap_start)
overlap_height = max(0, y_overlap_end - y_overlap_start)
overlap_area = overlap_width * overlap_height

remaining_area = (x2_1 - x1_1) * (y2_1 - y1_1) - overlap_area

if remaining_area == 0:
    print(0)
else:
    min_x1 = min(x1_1, x1_2)
    max_x2 = max(x2_1, x2_2)
    min_y1 = min(y1_1, y1_2)
    max_y2 = max(y2_1, y2_2)
    
    width = max_x2 - min_x1
    height = max_y2 - min_y1
    
    print(width * height)