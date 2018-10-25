# opcodes.py

opcodes = {	"add":	0b00000,
			"addi":	0b00101,
			"sub":	0b00000,
			"and":	0b00000,
			"or":	0b00000,
			"sll":	0b00000,
			"sra":	0b00000,
			"mul":	0b00000,
			"div":	0b00000,
			"sw":	0b00111,
			"lw":	0b01000,
			"j":	0b00001,
			"bne":	0b00010,
			"jal":	0b00011,
			"jr":	0b00100,
			"blt":	0b00110,
			"bex":	0b10110,
			"setx":	0b10101}
ALUopcodes = {
		   	"add":	0b00000,
		   	"sub":	0b00001,
		   	"and":	0b00010,
		   	"or":	0b00011,
		   	"sll":	0b00100,
		   	"sra":	0b00101,
		   	"mul":	0b00110,
		   	"div":	0b00111
}

Ropcodes = 	[0b00000]
Iopcodes = 	[0b00101, 0b00111, 0b01000, 0b00010, 0b00110]
JIopcodes =	[0b00001, 0b00011, 0b10110, 0b10101]
JIIopcodes= [0b00100]
shamtopcodes = [0b00100, 0b00101]

def getOpcode(str):
	return opcodes[str]
def getALUopcode(str):
	return ALUopcodes[str]

def getType(opcode):
	if opcode in Ropcodes:
		return "R"
	if opcode in Iopcodes:
		return "I"
	if opcode in JIopcodes:
		return "JI"
	if opcode in JIIopcodes:
		return "JII"
def usesShamt(ALUopcode):
	return ALUopcode in shamtopcodes