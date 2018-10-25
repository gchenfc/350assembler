# ECE350_assembulator.py
# Gerry Chen

import opcodes

MIPScode = """
addi $1, $0, 10
sw $1, $0, 0
add  $2, $2, $1
addi $1, $1, -1
blt  $0, $1, -3
sw 	 $2, $0, 1
"""

instructions = MIPScode.split('\n')

def debugprint(*args):
	if False:
		print(*args)

for instruction in instructions:
	if (instruction == ''):
		continue
	bits = 0;
	pieces = instruction.split()
	debugprint(pieces)
	opcode = opcodes.getOpcode(pieces[0])
	# bits = bits + opcode << 27
	if (opcodes.getType(opcode)=="R"):
		debugprint("R instruction")
		ALUopcode = opcodes.getALUopcode(pieces[0])
		rd = int(pieces[1][1:-1])
		rs = int(pieces[2][1:-1])
		if (opcodes.usesShamt(ALUopcode)):
			rt = 0
			shamt = int(pieces[3])
		else:
			rt = int(pieces[3][1:])
			shamt = 0
		debugprint(opcode,rd,rs,rt,shamt,ALUopcode,0)
		bits = (opcode << 27) + (rd << 22) + (rs << 17) + (rt << 12) + (shamt << 7) + (ALUopcode << 2) + 0
	elif (opcodes.getType(opcode)=="I"):
		debugprint("I instruction")
		rd = int(pieces[1][1:-1])
		rs = int(pieces[2][1:-1])
		N = int(pieces[3])
		debugprint(opcode,rd,rs,N)
		bits = (opcode << 27) + (rd << 22) + (rs << 17) + (N & 0x1FFFF)
	print(bits)
	debugprint("{:0>32b}".format(bits))
	# for i in range(50):
	# 	print(i%10,end="")
	# print()
	# print(len("{:b}".format(5)))