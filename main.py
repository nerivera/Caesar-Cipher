def cc(op, dis, inp):
  a = ((op == "encode") * 2 - 1) * dis
  a += (a < 0) * 26
  lib = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")
  mes = ""
  for x in inp:
    if (x in "".join(lib)):
      b = lib[int(x.islower())]
      mes += b[(b.find(x) + a) % 26]
    else:
      mes += x
  return mes
print(cc(input("Encode or decode: "), int(input("Shift amount: ")), input("Message: ")))
