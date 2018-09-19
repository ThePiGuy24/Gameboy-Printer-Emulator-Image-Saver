data = [["FF", "00"],["EA", "AE"]]
for bytes in data:
	out = [((int(bytes[0],16)%256)//128)*2+((int(bytes[1],16)%256)//128)*2,((int(bytes[0],16)%128)//64)*2+((int(bytes[1],16)%128)//64)*2,((int(bytes[0],16)%64)//32)*2+((int(bytes[1],16)%64)//32)*2,((int(bytes[0],16)%32)//16)*2+((int(bytes[1],16)%32)//16)*2,((int(bytes[0],16)%16)//8)*2+((int(bytes[1],16)%16)//8)*2,((int(bytes[0],16)%8)//4)*2+((int(bytes[1],16)%8)//4)*2,((int(bytes[0],16)%4)//2)*2+((int(bytes[1],16)%4)//2)*2,((int(bytes[0],16)%2)//1)*2+((int(bytes[1],16)%2)//1)*2]
	print(out)