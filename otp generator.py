#otp generator
import random as np
print("\n\n---------------OTP GENERATOR---------------\n\n")
val=np.random()
otp=str(val)
num=int(input("How many digit OTP you want:"))
print("your otp is: ",otp[3: num+3])
