import math
xi=4/30000; me=0.51099895; G=6.67430e-11
print("1  xi^2            =", xi**2, " (Dok: 1.778e-8)")
print("   xi^2/(4 me)     =", xi**2/(4*me), " mit Dok-Werten 1.778e-8/(4*0.511) =", 1.778e-8/(4*0.511), " (Dok: 8.708e-9)")
g0=1.778e-8/(4*0.511)
print("2  E_char Stufe 3  = 7.4*(4/3)^2 =", 7.4*(4/3)**2, " (Dok 13.156)")
print("   Stufe 5 *pi/sqrt2 =", 7.4*(4/3)**2*math.pi/math.sqrt(2), " (Dok 29.2)")
print("   Stufe 7 *0.986  =", 7.4*(4/3)**2*math.pi/math.sqrt(2)*0.986, " (Dok 28.4)")
print("   C_dim = 1/28.4  =", 1/28.4, " (Dok 3.521e-2)")
print("3  K = 1-0.94/68   =", 1-0.94/68, "  mit D_f=2.973: 1-0.973/68 =", 1-0.973/68, "  1-100xi =", 1-100*xi)
print("4  Kette Dok: ", g0, "*3.521e-2 =", g0*3.521e-2, "; *7.783e-3 =", g0*3.521e-2*7.783e-3, "; *0.986*10 =", g0*3.521e-2*7.783e-3*9.86)
print("   Verhältnis G / Kette =", G/(g0*3.521e-2*7.783e-3*9.86))
for lab,x,K in (("Dok-Rundung",g0,0.986),("exakt, K=0.98618",xi**2/(4*me),1-0.94/68),("exakt, K=1-100xi",xi**2/(4*me),1-100*xi)):
    v=x*7.783e-3*K; print(f"5  ohne C_dim ({lab}): {v:.5e}  Abw {(v/G-1)*100:+.3f} %")
v=g0*(1/28.4)*7.783e-3*0.986; print(f"6  mit C_dim, ohne *10: {v:.4e}")
print("   C_conv noetig mit C_dim:", G/(g0/28.4*0.986))
