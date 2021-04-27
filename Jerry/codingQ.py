class manage:
    def __init__(self):
        self.sequence = []

    def add(self, f, t):
        if self.sequence==[]:
            self.sequence.append([f,t])
        else:
            sequenceNew = []
            added = False
            for i in range(len(self.sequence)):
                start, end = self.sequence[i]
                if t<start:
                    sequenceNew.append([f,t])
                    sequenceNew.append(self.sequence[i])
                    added = True
                elif end<f:
                    sequenceNew.append(self.sequence[i])
                elif (f>=start and f<=end):
                    f = start
                elif (t>=start and t<=end):
                    t = end
            if added==False:
                sequenceNew.append([f,t])
            self.sequence = sequenceNew


    def remove(self, f, t):
        if f<self.sequence[0][0] or t>self.sequence[-1][1]:
            print("Error: remove outside of range!")
        sequenceNew = []
        for i in range(len(self.sequence)):
            start, end = self.sequence[i]
            if f>start and t<end:
                sequenceNew.append([start,f])
                sequenceNew.append([t,end])
            elif f>start and f<end:
                sequenceNew.append([start,f])
            elif t>start and t<end:
                sequenceNew.append([t, end])
            elif f<start and t>end:
                continue
            else:
                sequenceNew.append(self.sequence[i])
        self.sequence = sequenceNew


if __name__ == '__main__':
    M = manage()

    M.add(1,5)
    print(M.sequence)
    M.remove(2,3)
    print(M.sequence)
    M.add(6,8)
    print(M.sequence)
    M.remove(4,7)
    print(M.sequence)
    M.add(2,7)
    print(M.sequence)
