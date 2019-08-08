# Mathmatical Formualas

import sys
import os
import math

idiot = "person"


#title screen couldn't debug it properly to make it a "def"
print("""
##############      #############     
##                  ## 
##                  ##
##                  ##
##########          ##
##                  #############
##                             ##
##                             ##
##                             ##
##                             ##
##                  #############\n\n""");

#formulas that are offered
print("""The formulas we offer are: 
\n-area                         -density
\n-basic math(+, -, *, /)       -pressure
\n-circumference                -weight
\n-surface area                 -velocity
\n-volume                    
\n-More Coming soon!""");
          
x = input("\nWhat formuala do you need? ");
  
  

def what_formula():
  if x == "area":
    shape = input("\nWhat is the shape we are working with? ");

    if shape == "rectangle":
      length = float(input("\nGive me the length: "));
      width = float(input("\nGive me the width: "));
      area_rec = (length * width);
      print("\nThe area = %.2f " %area_rec);

    if shape == "square":
      a1 = float(input("\nwhat is one side of the square? "));
      a2 = float(input("\nWhat is the number of the side that is adjacent to the one you gave me? "));
      area_sq = (a1 * a2);
      print("\nThe area = %.2f " %area_sq);

    if shape == "triangle":
      base = float(input("\nWhat is the base? "));
      height = float(input("\nWhat is the height? "));
      area_tri = (base * height) / 2;
      print("\nThe area of the triangle is %.2f" %area_tri);

    if shape == "circle":
      radius = float(input("""\nWhat is the radius of the circle? 
      \nIf you only have the diameter than don't be lazy divide it by 2 and get the radius: """));
      area_cir = (radius ** radius) * 3.14159265359;
      print("\nThe area = %.2f" %area_cir);

    if shape == "trapezoid":
      base1 = float(input("\nWhat is the number for base 1? "));
      base2 = float(input("\nWhat is the number for base 2? "));
      height = float(input("\nWhat is the verticle height? "));
      area_trap = (base1 + base2) * height / 2;
      print("\nThe area = %.2f" %area_trap);
    
      
         


  if x == "basic math":
    basic_math = input("""\nWhich of the basic math functions do you need?
    \n +
    \n -
    \n *
    \n / \n\n""");

    if basic_math == "+":
     add1 = float(input("\nWhat is the first number you need to add? "));
     add2 = float(input("\nWhat is the second number? "));
     basic_add = add1 + add2;
     print("\nThe numbers = %.2f" %basic_add);
    
    if basic_math == "-":
     sub1 = float(input("\nWhat is the first number you need to subtract? "));
     sub2 = float(input("\nWhat is the second number? "));
     basic_sub = sub1 - sub2;
     print("\nThe numbers = %.2f" %basic_sub);

    if basic_math == "*":
     mul1 = float(input("\nWhat is the first number you need to multiply? "));
     mul2 = float(input("\nWhat is the second number? "));
     basic_mul = mul1 * mul2;
     print("\nThe numbers = %.2f" %basic_mul);

    if basic_math == "/":
     div1 = float(input("\nWhat is the first number you need to divide? "));
     div2 = float(input("\nWhat is the second number? "));
     basic_div = div1 / div2;
     print("\nThe numbers = %.2f" %basic_div);



  if x == "circumference":
   r = float(input("\nWhat is the radius? "));
   circum = 2 * 3.14159265359 * r;
   print("\nThe answer = %.2f" %circum );



  if x == "surface area":

   shape = input("\nWhat shape are we working with? ");

   if shape == "cube":
     a = float(input("\nWhat is the legnth of the edge? "));
     cube_ans = 6 * a ** 2;
     print("\nThe answer = %.2f" %cube_ans);

   if shape == "cylinder":
     r = float(input("\nWhat is the radius? "));
     h = float(input("\nWhat is the height? "));
     cyl_ans = 2 * 3.14159265359 * r * h;
     print("\nYour answer = %.2f" %cyl_ans);

   if shape == "cone":
     r = float(input("\nWhat is the radius? "));
     l = float(input("\nWhat is the length? "));
     cone_ans = 3.14159265359 * r ** 2 + 3.14159265359 * r * l;
     print("\nYour answer = %.2f" %cone_ans);
   
   if shape == "sphere":
     r = float(input("\nwhat is the radius? "));
     sph_ans = 4 * 3.14159265359 * r ** 2;
     print("\nYour answer %.2f" %sph_ans);


  if x == "volume":

   shape = input("""\nWhat is the shape?
   \n -cube
   \n -cylinder
   \n -cone
   \n -sphere \n\n""");

   if shape == "cube":
     a = float(input("\nWhat is the length of the edge? "));
     vol_cub = a ** 3;
     print("\nAnswer = %.2f" %vol_cub);
   
   if shape == "cylinder":
     b = float(input("\nWhat is the base? "));
     h = float(input("\nWhat is the height? "));
     vol_cyl = b * h;
     print("\nAnswer = %.2f" %vol_cyl);
   
   if shape == "cone":
     b = float(input("\nWhat is the base? "));
     h = float(input("\nWhat is the height? "));
     vol_con = b * h / 3;
     print("\nAnswer = %.2f" %vol_con);

   if shape == "sphere":
     r = float(input("\nWhat is the radius? "));
     vol_sph = 4 * 3.14159265359 * r ** 3 / 3;
     print("\nAnswer = %.2f" %vol_sph);
  
  
  if x == "density":
    m = float(input("\nWhat is the mass? "));
    v = float(input("\nWhat is the volume? "));
    dens_ans = m / v;
    print("\nAnswer = %.2f" %dens_ans);


  
  if x == "pressure":
    f = float(input("\nWhat is the force? "));
    a = float(input("\nWhat is the area it acts on? "));
    pres_ans = f / a;
    print("\nAnswer = %.2f" %pres_ans);
    

  if x == "weight":
    m = float(input("\nWhat is the mass? "));
    g = float(input("\nWhat is the grams? "));
    w = m / g;
    print("\nAnswer = %.2f" %w);


  if x == "velocity":
    d = float(input("\nWhat is the distance(m)? "));
    t = float(input("\nWhat is the time(s)? "));
    v = d / t;
    print("\nAnswer = %.2f" %v);






what_formula();
