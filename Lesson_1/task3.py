m_value = 60
h_value = 3600
d_value = 86400

t_value = int(input("Time value: "))

sec  = int(int (t_value % d_value) % h_value) % m_value 
min  = int(int (int (t_value % d_value) % h_value) / m_value)
hrs  = int(t_value % d_value / h_value)
days = int(t_value / d_value)

print(str(days) + ":" + str(hrs) + ":" + str(min) + ":" + str(sec))
