s = str(input()).lower()

w_count = 0
m_count = 0

u_count = 0
consecutive_u_count = 0
current_consecutive_u_count = 0

n_count = 0
consecutive_n_count = 0
current_consecutive_n_count = 0

for i in range(len(s)):
    if s[i] == "u":
        u_count += 1
        current_consecutive_u_count += 1
        if current_consecutive_u_count > consecutive_u_count:
            consecutive_u_count = current_consecutive_u_count
    else:
        current_consecutive_u_count = 0

    if s[i] == "n":
        n_count += 1
        current_consecutive_n_count += 1
        if current_consecutive_n_count > consecutive_n_count:
            consecutive_n_count = current_consecutive_n_count
    else:
        current_consecutive_n_count = 0

    if s[i] == "m":
        m_count += 1
    elif s[i] == "w":
        w_count += 1

if consecutive_n_count == 1:
    consecutive_n_count = 0
if consecutive_u_count == 1:
    consecutive_u_count = 0

if ((m_count > 0 or w_count >0) or(m_count ==0 and w_count ==0 and n_count ==0 and u_count==0)):
    print(0)
    exit()
if u_count > 0 and consecutive_u_count == 0:
    print(1)
elif n_count > 0 and consecutive_n_count == 0:
    print(1)
else:
    print(int(consecutive_u_count) + int(consecutive_n_count))
