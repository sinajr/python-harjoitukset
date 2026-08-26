# täälä otettan käyttäjän nimi ja ikä
name = input("what is your name?");
print("terve "+name);
welcomeIn = input("how old are u?");
print("so you are "+welcomeIn+" years old, welcome again");

#täälä lasketan ympyrän pinta-alan ja ympärysmitan
pi=3.14;
radius= float(input("insert your radius that you want to calculate the area of a circle: "));
envionment= float(2 * pi * radius);
area = float(pi * radius ** 2);
print("the area of circlr is"+ str(area));
print("the environment of circle is:"+ str(envionment));

#täälä lasketan suorakulmion pinta-alan ja ympärysmitan
height_u= float(input("insert the height of the rectangle:"));
width_u= float(input("insert the width of the rectangle:"));
print(f"Environment of rectangle:{str(float(2*(height_u + width_u)))} \n Area of rectangle: {str(float(height_u * width_u))}");

#summan, tulon ja keskiarvon
numOne= float(input("insert the first number:"));
numTwo= float(input("insert the second number:"));  
numThree= float(input("insert the third number:"));
summa= float(numOne + numTwo + numThree);
tulo=float(numOne * numTwo * numThree);
keskiarvo=float(summa / 3);
print("your numbers are:" + str(numOne) + " " + str(numTwo) + " " + str(numThree));
print(f"Sum of the numbers:{str(summa)}\n Multiplication of the numbers: {str(tulo)}\n Average of the numbers:{str(keskiarvo)}");

#Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi

leivis_u= float(input("Anna leiviskät:"));
naula_u= float(input("Anna naulat:"));
luodi_u= float(input("Anna luodit:"));
laskinArrey=[leivis_u, naula_u, luodi_u];

a= float(((laskinArrey[0]*13.3)*32)*20);
b= float((laskinArrey[1]*32)*13.3);
c= float(laskinArrey[2]*13.3);

kilo=int(float(a+b+c)/1000);
gramma= ((float(a+b+c)/1000)-kilo)*1000;
print(f"leviskät: {str(leivis_u)}\n naulat: {str(naula_u)}\n luodit: {str(luodi_u)}");
print(f"Massa nykymittojen mukaan:\n {kilo} kg {str(gramma)} g");

#ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
import random
x=[];
for i in range (3):
    x.append(random.randint(0,9));
print("3 numerolukon koodia: "+str(x));

y=[];
for i in range (4):
    y.append(random.randint(1,6));
print("4 numerolukon koodia: "+str(y));

print("Ole hyvää, peli loppui :)))")