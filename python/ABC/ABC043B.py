S = input()

st = []
for i in S:
    if i == 'B':
        if st:
            st.pop()
    else:
        st.append(i)

print(*st, sep='')
