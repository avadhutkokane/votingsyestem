from matplotlib import pyplot as plt
import pandas as pd
a=b=c=d=e=f=0
w=2
c1="MODI"
c2="AMIT"
c3="YOGI"
c4="RAHUL"
c5="RAJNATH"
c6="NOTA"
g={1:"AVADHUT",2:"SUJEET",3:"SHRIDHAR",4:"NIRANJAN",5:"HARSHWARDHAN",6:"GAURAV"}
while 1>0:
    h=int(input("ENTER VOTING ID:"))
    j=int(input("ENTER VOTER PASSWORD:"))
    s={1:11,2:22,3:33,4:44,5:55,6:66}
    if h in g and j==s[h]:
        print("WELCOME",g[h],"FOR VOTING YOR CANDIDATES ARE")
        del g[h]
        print("\n","PRESS 1 FOR",c1,"\n","PRESS 2 FOR",c2,"\n","PRESS 3 FOR",c3,"\n","PRESS 4 FOR",c4,"\n"
              ,"PRESS 5 FOR",c5,"\n","PRESS 6 FOR",c6)
        while 1>0:
            i=int(input("CANDIDATE ID:"))
            if i in range(1,7):
                if i==1:
                   a+=1
                elif i==2:
                   b+=1
                elif i==3:
                   c+=1
                elif i==4:
                   d+=1
                elif i==5:
                   e+=1
                else:
                   f+=1
                print("YOU HAVE VOTED SUCCESSFULLY")
                sum=a+b+c+d+e+f
                r1=a*100/sum
                r2=b*100/sum
                r3=c*100/sum
                r4=d*100/sum
                r5=e*100/sum
                r6=f*100/sum
                m=int(input("ENTER ANY INTEGER FOR VOTING AGAIN\nENTER 2 FOR RESULTS"))
                if m!=2:
                    print("welcome next voter")
                    break
                elif m==2:
                    pw=int(input("Enter Admin Password"))
                    if pw==w:
                        print(c1,r1)
                        print(c2,r2)
                        print(c3,r3)
                        print(c4,r4)
                        print(c5,r5)
                        print(c6,r6)
                        print("TOTAL VOTES GIVEN",sum)
                        cands=[c1,c2,c3,c4,c5,c6]
                        result=[r1, r2, r3, r4, r5, r6]
                        data={"CANDIDATES":cands,"PERCENTAGE OF VOTES":result}
                        df=pd.DataFrame(data)
                        print(df)
                        explode=(0.1,0,0.1,0,0.1,0)
                        fig=plt.figure(figsize=(10,7))
                        plt.pie(result,explode,labels=cands)
                        plt.show()
                        break
                    else:
                        print("YOU ENTERED WRONG ADMIN PASSWORD")
                        break
                else:
                    break
            else:
               print("INVALID CANDIDATE ID")
               continue
    else:
        print("ERROR OCCURRED DUE TO ANY ONE OF THE FOLLOWING REASONS")
        print("1]YOU HAVE VOTED EARLIER\n2]YOUR VOTING ID IS INVALID\n2]WRONG PASSWORD")
        continue