me = (40.814944, -73.488623)
erica = (40.816314, -73.491651)
parents = (40.757531, -73.713568)
fara = (40.765105, -73.962530)
og = me + erica + parents + fara
print(me, erica, parents, fara)

d_erica = (me[0] - erica[0])**2 + (me[1] - erica[1])**2
d_parents = (me[0] - parents[0])**2 + (me[1] - parents[1])**2
d_fara = (me[0] - fara[0])**2 + (me[1] - fara[1])**2

if d_erica <= d_parents and d_erica <= d_fara:
    closest = "erica"
elif d_parents <= d_fara:
    closest = "parents"
else:
    closest = "fara"

print("Closest is", closest)
# optional peek at the scores you compared
print(d_erica, d_parents, d_fara)
