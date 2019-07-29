def collision(x1,y1,x2,y2):
	if (x1<x2+44) and (x1>x2-44) and (y1<y2+44) and (y1>y2-44):
		return 1
	return 0