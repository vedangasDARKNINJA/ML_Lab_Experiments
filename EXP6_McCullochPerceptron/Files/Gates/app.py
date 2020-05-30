from tabulate import tabulate

NUMBER_OF_INPUTS = 4


def format_input(power):
    binary_str = [format(i, '0'+str(power)+'b') for i in range(2**power)]
    binary = []
    for i in range(len(binary_str)):
        binary.append([int(x) for x in binary_str[i]])
    return binary


def GATE(inp, thresh, neg=False):
    output = -1
    weights = [1 for i in range(len(inp))]
    measured_output = sum([inp[i]*weights[i] for i in range(len(inp))])
    if(measured_output > thresh):
        if neg:
            output = 0
        else:
            output = 1
    else:
        if neg:
            output = 1
        else:
            output = 0
    return output


inputs = format_input(NUMBER_OF_INPUTS)
outputs_or = []
outputs_nor = []
outputs_and = []
outputs_nand = []

for i in inputs:
    outputs_or.append([i, GATE(i, 0.5)])  # OR GATE
    outputs_nor.append([i, GATE(i, 0.5, True)])  # NOR GATE
    outputs_and.append([i, GATE(i, NUMBER_OF_INPUTS-1)])  # AND GATE
    outputs_nand.append([i, GATE(i, NUMBER_OF_INPUTS-1, True)])  # NAND GATE


print("OR GATE: ")
print(tabulate(outputs_or, headers=['inputs', 'outputs']))

print("NOR GATE: ")
print(tabulate(outputs_nor, headers=['inputs', 'outputs']))

print("AND GATE: ")
print(tabulate(outputs_and, headers=['inputs', 'outputs']))

print("NAND GATE: ")
print(tabulate(outputs_nand, headers=['inputs', 'outputs']))
