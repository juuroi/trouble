import itertools
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    # write the recursive function here
    # remember to print out the route as the recursion ends
    allports = route + ports
    perms = itertools.permutations(allports)
    for perm in perms:
        #output = [portnames[route[0]]]
        #output = route[0]
        output = []
        for item in perm:
            #output.append(portnames[item])
            output.append(item)
        print(output)

# this will start the recursion with 0 as the first stop
permutations([0], list(range(1, len(portnames))))
