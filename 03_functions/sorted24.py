from operator import itemgetter

film23 = []                                     # initialize

film23.append(["Chiru", 65, "tollywood", "Hero"])
film23.append(["Charan",  37, "tollywood", "Hero"])
film23.append(["Rajamouli", 50, "tollywood", "Director"])
film23.append(["AR Rahman", 54, "kollywood", "Music director"])
film23.append(["Nayanthara", 65, "mollywood", "heroine"])
film23.append(["SRK",  60, "bollywood", "Hero"])
film23.append(["Tom Cruise", 61, "hollywood", "Hero"])
film23.append(["Amitab",  81, "bollywood", "Hero"])
film23.append(["Kamal Hasan", 65, "kollywood", "Hero"])
film23.append(["Jennifer Aniston",  57, "hollywood", "heroine"])

# film23.append({"Chiru", 65, "Hero"})
# film23.append({"Charan",  37, "Hero"})
# film23.append({"Rajamouli", 50, "Director"})
# film23.append({"AR Rahman", 54, "Music director"})


# newFilmlist22 = sorted(film23, key=itemgetter(1),reverse=True)        #### sorts based on age
# newFilmlist22 = sorted(film23, key=itemgetter(0))                       #### sorts based on name
newFilmlist22 = sorted(film23, key=itemgetter(2))                       #### sorts based on industry

print("newFilmlist22 ===> ", newFilmlist22)