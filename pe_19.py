def is_schalt(y):
    return y%4 == 0 and y%100 != 0 or y%4 == 0 and y%400 == 0

def feb(y):
    if is_schalt(y): return 29
    return 28

def add_month(m, y):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12: return 31
    if m == 4 or m == 6 or m == 9 or m == 11: return 30
    return feb(y)

def next_month(m, y):
    if m > 11: return 1, y+1
    return m+1, y
       
def count_sundays_on_1(m, y):
    daycount = 1
    sundaycount = 0
    m_curr = 0
    m_final = m
    y_curr = 1900
    y_final = y

    while True:
        if daycount%7 == 0: sundaycount += 1
        daycount += add_month(m_curr, y_curr)
        if y_curr == y_final and m_curr == m_final: break
        m_curr, y_curr = next_month(m_curr, y_curr)
        
    return sundaycount

def count_sundays_start_stop(mi, yi, mf, yf):
    return count_sundays_on_1(mf, yf) - count_sundays_on_1(mi, yi)

count_sundays_start_stop(1, 1901, 12, 2000)