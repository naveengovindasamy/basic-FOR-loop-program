for i in range(10):
    print(f"You ran {i+1} miles")
    tired = input("Are you tired? ")
    if tired == 'yes':
        break

if i == 9:
    print("You just finished 10 km race!")
else:
    print("You didn't finish 10 km race but hey congrats anyways!")
