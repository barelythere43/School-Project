
import time

def start():
    print ("This is a program designed to identify the value of going to film school")
    print("based on a cost/benefit analysis.")
    time.sleep(2)
    print("There will be several options that the user can choose.")
    time.sleep(2)
    print("With each unique option, there is a unique response.")
    print("----------------------------------------")
    time.sleep(3)

start()

def step2():
    print("What is the main reason you want to go to film school?")
    time.sleep(2)
    print ("Your Options Are")
    print("----------------------------------------")
    time.sleep(1)
    print("1)For Making Connections")
    time.sleep(1)
    print("2)Solely to Gain Filmmaking Knowledge")
    time.sleep(1)
    print("3)For Your Resume")
    time.sleep(1)
    print("4)To Get a Job In The Film Industry in General (not specific)")
    time.sleep(1)

step2()

def step3():
    choosereason=input("Choose any Reason 1-4:")
    chooseanswer1=["1"]
    chooseanswer2=["2"]
    chooseanswer3=["3"]
    chooseanswer4=["4"]
    if choosereason in chooseanswer1:
        time.sleep(1)
        print("If you want to go to film school mainly for making connections, it is not completely neccesary for you to go to film school. Unless you are going to top tier film school, the cost would outweigh the benefits. You can make connections, albeit not as easily, without going to film school"
)              
    if choosereason in chooseanswer2:
        time.sleep(1)
        print("If you want to go to film school to gain filmmaking knowledge, then film school is valuable. For this reason, you don't have to go to a expensive, private, big name instituition. In that sense the benefits justify the cost becuase you are going to an affordable school to get a film education."
)
    if choosereason in chooseanswer3:
        time.sleep(1)
        print("If you want a film degree just as proof that you have knowledge in the subject, then it is not worth it. Yes, it is nice to have it on your resume, but internships and hands on experience are looked at just as seriously. Don't feel that it is necessary to go to film school just for the degree.")
    if choosereason in chooseanswer4:
        time.sleep(1)
        print("If you know that you want to work in the film industry, but don't have a specifc interest yet, then film school is worth it. This is because in film school, you learn more than just making a movie. There is a broad curriculum that teaches all aspects including sound, editing, cinematography, storytelling, writing, etc. Going to film school will give you enough knowledge in a wide array of subfields to work in.")


step3()
