# IntheTowersofHanoipuzzle,wearegivenaplatformwiththreepegs,a, b, and c, sticking out of it. On peg a is a stack of n disks, each larger than the next, so that the smallest is on the top and the largest is on the bottom. The puzzle is to move all the disks from peg a to peg c, moving one disk at a time, so that we never place a larger disk on top of a smaller one. See Figure 4.15 for an example of the case n = 4. Describe a recursive algorithm for solving the Towers of Hanoi puzzle for arbitrary n. (Hint: Consider first the subproblem of moving all but the nth disk from peg a to another peg using the third as “temporary storage.”)



""" A recursive algorithm to solve towers of hanoi problem """

def ToH(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move 1 from rod", from_rod , "to", to_rod)
        return
    ToH(n-1, 
