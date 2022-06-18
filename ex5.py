name = 'John R. Moran'
age = 47 #for a little while longer

height = 196 #centimetres
conv_cm_inch = 2.54 # divide height in cm by conversion factor to get inches
height_in_inches = height / conv_cm_inch

weight = 102 #kilograms
conv_kg_lbs = 2.205 #multiply weight in kg by conversion factor to get lbs
weight_in_lbs = weight * conv_kg_lbs

eyes = 'blue'
hair = 'brown'
teeth = 'present'

print(f"Let's talk about {name}.")
print(f"He's {height} centimetres or {round(height_in_inches)} inches tall")
print(f"He's {weight} kilograms or {round(weight_in_lbs)} in pounds heavy")
print("He's a bit of a fatty")
print(f"he's got {eyes} eyes and {hair} hair.")
print(f"his teeth are still {teeth} although who knows for how much longer?")

#this line is tricky so try to get it right!
total = age + height + weight
print(f"If I add {age}, {weight} and {height} I get {total}")
