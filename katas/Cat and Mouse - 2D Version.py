def cat_mouse(map_, moves):
    if 'C' not in map_ or 'm' not in map_:
        return "boring without two animals"
    st = ''
    gg = map_.find('\n')
    for i in map_:
        if i == '\n':
            continue
        st += i
    moves = abs(moves)
    y_c = st.find('C')//gg
    x_c = st.find('C')%gg
    y_m = st.find('m')//gg
    x_m = st.find('m')%gg
    if abs(y_c - y_m) + abs(x_c - x_m) <= moves:
        return "Caught!"
    else:
        return "Escaped!"

map_ = '''\
..C......
.........
....m....'''
print(cat_mouse(map_, 5))