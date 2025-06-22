import matplotlib.pyplot as plt

I_C_mA = [2, 5, 10, 15, 20] 
u_pp_eingang_mV = [9.9, 9.7, 9.3, 8.9, 8.6] 
u_pp_ausgang_V = [0.749, 1.75, 3.25, 4.45, 5.53]
v_u = [75.7, 180.4, 349.5, 500.0, 643.0] 

plt.figure(figsize=(8, 5))
plt.plot(I_C_mA, v_u, marker='o', linestyle='-', color='b', label=r'$v_u$')

plt.title('Spannungsverstärkung $v_u(I_C)$')
plt.xlabel(r'Kollektorstrom $I_C$ [mA]')
plt.ylabel(r'Spannungsverstärkung $v_u$')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
