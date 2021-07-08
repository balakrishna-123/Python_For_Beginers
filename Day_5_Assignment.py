#Build a function for finding if a number is prime or not.

n=int(input("Enter number: "))
def prime(n):
    if n>1:
        
        for i in range(2,int(n/2)+1):
            if n%i==0:
                return(str(n)+" is not a prime number")
                break
        return(str(n)+"  is a Prime Number")
    else:
        print(str(n)+" is a Prime Number")
 
 
print(prime(n))

 
 
 #Build  Youtube video Downloader App using library in Python refer pypi.org.
 import pytube

url = input("Enter Url :")

youtube = pytube.YouTube(url)
video = youtube.streams.first()
video.download('../Video')
