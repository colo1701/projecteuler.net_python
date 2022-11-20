count = 1 # Die Lösung mit der 2 pound-Münze wird nicht berechnet; der Wert wird direkt in count definiert.

for a in range(3):
    rest_a = 200 - a*100
    for b in range(int(rest_a/50)+1):
        rest_b = rest_a - 50*b
        for c in range(int(rest_b/20)+1):
            rest_c = rest_b - 20*c
            for d in range(int(rest_c/10)+1):
                rest_d = rest_c - 10*d
                for e in range(int(rest_d/5)+1):
                    rest_e = rest_d - 5*e
                    for f in range(int(rest_e/2)+1):
                        rest_f = rest_e - 2*f
                        for g in range(int(rest_f)+1):
                            if 100*a + 50*b + 20*c + 10*d + 5*e + 2*f + g == 200: count += 1

print(count)