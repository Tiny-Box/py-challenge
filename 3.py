s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

a = "map"

def translate(s):
	b = []

	for i in range (0, len(s)):
		a = s[i]
		if ord(a) >= 97 and ord(a) <= 122:
			if ord(a) >= 121:
				a = chr(2 + ord(a) - 28)
			a = chr(2 + ord(a))
		
		b.append(a)

	b = ''.join(b)
	return b

print translate(a)
