import re

def solve(args):
	c=re.findall('[\.\d]+',args)
	n1=float(c[0])
	n2=float(c[1])
	op=args[len(c[0]):-len(c[1])].strip()
	if op=='+':
		ans=n1+n2
	elif op=='-':
		ans=n1-n2
	elif op=='/':
		if n2==0:
			ans='Cannot divide by zero'
		else:
			ans=n1/n2
	elif op=='//':
		ans=n1//n2
	elif op=='*':
		ans=n1*n2
	elif op=='**':
		ans=n1**n2
	elif op=='^':
		if int(n1)==n1 and int(n2)==n2:
			ans=int(n1)^int(n2)
		else:
			ans='Cannot XOR floating point numbers'

	if isinstance(ans,str):
		return ans
	else:
		if int(ans)==ans:
			return int(ans)
		else:
			return ans