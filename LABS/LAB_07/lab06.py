from Apartment import Apartment

def mergesort(apartmentList):

    if len(apartmentList)>1:
        mid = len(apartmentList)//2
        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i]< righthalf[j]:#here the other <=
                apartmentList[k]=lefthalf[i]
                i=i+1
            else:
                apartmentList[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            apartmentList[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            apartmentList[k]=righthalf[j]
            j=j+1
            k=k+1
            


def ensureSortedAscending(apartmentList):
    lex=len(apartmentList)-1
    for i in range(lex):
        if (apartmentList[i]>apartmentList[i+1]) ==True:
            return False
    return True




def getNthApartment(apartmentList, n):
    a=apartmentList
    if len(a)-1<n:
        return "(Apartment) DNE"
    
    temp=a[n].getApartmentDetails()
    return temp

def getTopThreeApartments(apartmentList):
    mergesort(apartmentList)
    temp=apartmentList
    if len(temp)==1:
        strR="1st: "+temp[0].getApartmentDetails()
        return strR
    if len(temp)==2:
        str1="1st: "+temp[0].getApartmentDetails()
        str2="2nd: "+temp[1].getApartmentDetails()
        strR=str1+"\n"+str2
        return strR

        
    else:
        str1=temp[0].getApartmentDetails()
        str2=temp[1].getApartmentDetails()
        str3=temp[2].getApartmentDetails()
        strR="1st: "+str1+"\n"+"2nd: "+str2+"\n"+"3rd: "+str3
        return strR
    