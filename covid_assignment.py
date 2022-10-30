print("        welcome to great kirikalan magic show       ")
print("--covid 19 Tamil nadu details 2020--")

#list
covid=["1.covid 19 positive cases","2.Positive case which age sector high","3.covid bed apply  ","4.To Apply Epass","5.covid certificate ","6.vaccine status","7.vaccine side affect ","8.top 3 District wise covid status "]
#for loop using print
#length use
#range use
for i in range(len(covid)):
    print(covid[i])

#function 
#function arguments pases

def details(tamilnadu):
    #first string
    print(f"Tamil Nadu posiitive cases is {tamilnadu}")

def ages(age,age1,age2):
    print(f"A majority of the coronavirus (COVID-19) cases in India affected people between ages {age} and {age1}   years as of October 18, 2020. Of these, the highest share of deaths during the measured time period was observed in people under the age of {age2} years.")

def covid_bed(district,hospital,bed1,case):
    print(f"your district is {district} ")
    print(f"your hospital is {hospital}")
    print(f"your bed is {bed1} ")
    print(f"your case is {case}")

def epass(a,b,c,d,e,f,g,h):
    print()
    print(f"vechicle  owner: {a}")
    print(f"vechicle number : {b}")
    print(f"type of vechicle : {c}")
    print(f"Driver name : {d}")
    print(f"License Number : {e}")
    print(f"pass validity: {f}")
    print(f"From {g} To {h}")
    
    
def covid_certificate():
    print("REF ID : xxxx78")
    print("SECRET CODE : xx468")
    print("PHOTO ID: AADHAAR CARD")
    print("ID NUMBER : xxxxxxxxxxx1785")
    print("YEAR BIRTH: 2003")
    print("DOSE 1 COMPLETED -COVID SHIELD")
    print("DOSE 2 COMPLETED - COVID SHIELD")

def status():
    if user99>=18 and user98<=28:
        print("vaccine 1 status :68282")
        print("vaccine 2 status :48928")
        print("not vaccinated : 893")
        print("death : 63")
    elif user99>=28 and user98<=50:
        print("vaccine 1 status :562982")
        print("vaccine 2 status :488828")
        print("not vaccinated : 1003")
        print("death : 1000")
    else:
        print("vaccine 1 status :2982")
        print("vaccine 2 status :8928")
        print("not vaccinated : 463")
        print("death : 890")
        

    
    
def sideaffect():
  print("Tiredness")
  print("Headache")
  print("Muscle pain")
  print("Chills")
  print("Fever")
  print("Nausea")
  
def district():
    print(" District  Total cases  Total Death Total Recovered Active cases")
    print()
    print(" Thanjavur   2378          578           679            99")
    print(" Ariyalur    5763          849           369            29")
    print(" Erode       7379          016           721            78")
print()
user=int(input("Enter number :"))
#if conditional statement
if user==1:
        user1=int(input("Enter a positive cases number :"))
        details(user1)
elif user==2:
        user2=int(input("Enter a start age :"))
        user3=int(input("Enter  a  end age :"))
        user4=int(input("Enter under age   :"))
        ages(user2,user3,user4)
elif user==3:
        user5=input(("Enter your district :"))
        user6=input(("Enter your hospital name :"))
        user7=input(("Normal Bed ,ICU Bed,O² Bed :"))
        user8=input(("For Severe Cases or Moderate Cases or Mild Cases :"))
        covid_bed(user5,user6,user7,user8)

elif user==4:
        user9=input("Enter your vechicle owner name : ").upper()
        user10=input("Enter your vechicle number :")
        user11=input("Enter your vechicle type :").upper()
        user12=input("Enter driver name :").lower()
        user13=input("Enter your License Number :")
        user14=input("Enter your pass validity :")
        user15=input("Enter your from area :").lower()
        user16=input("Enter your destination :").lower()
        epass(user9,user10,user11,user12,user13,user14,user15,user16)

elif user==5:
    user17=int(input("Enter your mobile number :"))
    user18=int(input("Enter you OTP :"))
    covid_certificate()
    
elif user==6:
    print("TamilNadu vaccine status")
    user99=int(input("Enter the age :"))
    user98=int(input("Enter the age :"))
    status()

elif user==7:
    sideaffect()

elif user==8:
    district()
    
    
else:
        print("Enter only 1 to 8 ")

