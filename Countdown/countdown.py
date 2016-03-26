import random
import time
import itertools

large_numbers = [25,50,75,100]
small_numbers = range(1,11)*2

# choose whether to pick random numbers, or to type in numbers, or a selection.
large_count = raw_input("How many large numbers? (0-4): ")
if large_count == "n":
    target = int( raw_input("Enter your target: ") )
    selection = raw_input("Enter your numbers (space seperated): ")
    selection = [int(x) for x in selection.split()]
else:
    large_count = int(large_count)
    selection_large = random.sample( large_numbers, large_count )
    selection_small = random.sample( small_numbers, (6-large_count) )
    selection = selection_large + selection_small
    target = random.choice(range(101,1000))

print selection
print "Your target is: %s" %str(target)


# solver: operations are: + - * /
# todo: maybe try evolutionary example?
#good examples:
#[50, 8, 4, 5, 1, 7] -> 894
#[7, 2, 1, 3, 6, 5] -> 738

# generate permutations:
test_selection = selection + [0]
permutations = itertools.permutations(test_selection)
perms = list(permutations)

perms_new = []

for p in perms:
    pos = p.index(0)
    temp = p[0:pos]
    perms_new.append(temp)

# print "permutations (`perms`) = %s" %str(len(perms))
# print "amended permutations (`perms_new`) = %s" %str(len(perms_new))
# print "unique permutations (`perms_new`) = %s" %str(len(set(perms_new)))


def iter_solver(target, number_set, helper_str=""):

    if any(number < 0 for number in number_set):
        return ( -1, (helper_str + "No match, negative result. ") )
    elif target in number_set:
        return ( target, (helper_str + "Done! ") )
    elif len(number_set) == 0:
        return ( -1, (helper_str + "No match, no answer. ") )
    elif len(number_set) == 1 :
        return ( number_set[0], (helper_str + "No match, " + str(abs(number_set[0]-target)) + " away. ") )

    else:

        temp_number_set = number_set[2:] + ( number_set[0] + number_set[1] , )
        temp_helper_str = ( helper_str + "(%s + %s = %s). " %(number_set[0],  number_set[1], number_set[0]+number_set[1]) )
        plus_solve, plus_solve_str = iter_solver(target, temp_number_set, temp_helper_str)
        if plus_solve == target:
            return (plus_solve, plus_solve_str)
        else:
            (max_solve, max_solve_str) = (plus_solve, plus_solve_str)

        temp_number_set = number_set[2:] + ( number_set[0] * number_set[1] , )
        temp_helper_str = ( helper_str + "(%s * %s = %s). " %(number_set[0], number_set[1], number_set[0]*number_set[1]) )
        times_solve, times_solve_str = iter_solver(target, temp_number_set, temp_helper_str)
        if times_solve == target:
            return (times_solve, times_solve_str)
        else:
            if ( abs(max_solve-target) > abs(times_solve-target) ):
                (max_solve, max_solve_str) = (times_solve, times_solve_str)

        temp_number_set = number_set[2:] + ( number_set[0] - number_set[1] , )
        temp_helper_str = ( helper_str + "(%s - %s = %s). " %(number_set[0], number_set[1], number_set[0]-number_set[1]) )
        minus_solve, minus_solve_str = iter_solver(target, temp_number_set, temp_helper_str)
        if minus_solve == target:
            return (minus_solve, minus_solve_str)
        else:
            if ( abs(max_solve-target) > abs(minus_solve-target) ):
                (max_solve, max_solve_str) = (minus_solve, minus_solve_str)

    return (max_solve, max_solve_str)


solutions = []
best_result = 0
best_result_str = ""
best_result_len = 999

for the_perm in perms_new:
    result, result_string = iter_solver(target, the_perm)
    if result == target:
        solutions.append( { "result:" : result, "result_string" : result_string } )
    if ( abs(best_result-target) > abs(result-target) ):
        best_result = result
        best_result_str = result_string
        best_result_len = len(the_perm)
    elif ( abs(best_result-target) == abs(result-target) and best_result_len > len(the_perm) ):
        best_result = result
        best_result_str = result_string
        best_result_len = len(the_perm)


print "    30 seconds starts now.."
time.sleep(10)
print "    20 seconds left.."
time.sleep(10)
print "    10 seconds left.."
time.sleep(10)
print "    Time's up!"

print "Computer's best result: %s (%s away). It found %s solutions." %( best_result, abs(best_result-target), str(len(solutions)) )
print "The computer did: %s" %best_result_str
