pais_x = 70000
pais_y = 180000
anos = 0

while (pais_y >= pais_x):
    pais_x += (pais_x * 0.035)
    pais_y += (pais_y * 0.015)
    anos += 1
print("O país x demorará %.2f anos para superar a população do país y " % anos)
print("População do país x: %.2f\nPolulação do país y: %.2f" % (pais_x,pais_y))