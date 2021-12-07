for line in open('input.txt'):
    positions = line.split(",")
    pos = [int(x) for x in positions]

def fact_sum(n):
    # The infinite series whose terms are the natural numbers 1 + 2 + 3 + 4 + ⋯ is a divergent series.
    # https://wikimedia.org/api/rest_v1/media/math/render/svg/99476e25466549387c585cb4de44e90f6cbe4cf2 
    return n*(n+1)//2

fuelarr = []
fuel = 0

for i in range(max(pos) + 1):
    for j in range(len(pos)):
        fuel += abs(i - pos[j])
    fuelarr.append(fuel)
    fuel = 0

print(min(fuelarr))

fuelarr2 = []
fuel2 = 0

for i in range(max(pos) + 1):
    for j in range(len(pos)):
        fuel2 += fact_sum(abs(i - pos[j]))
    fuelarr2.append(fuel2)
    fuel2 = 0

print(min(fuelarr2))