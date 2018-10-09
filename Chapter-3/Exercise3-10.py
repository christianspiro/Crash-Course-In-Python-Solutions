languageList = ["english", "albanian", "japanese", "french", "italian"]
# Languages not capitalized due to sort return non-alpha order
print("I can currently speak " + languageList[0].title() + " and " + languageList[1].title() + ".")
# Some functions can be used like JavaScript
print("I will take " + languageList[2].title() + " at University.")
print("Then I would like to learn either " + languageList[3].title() + " or " + languageList[4].title() + "." )
# Backtick strings would be nice like in JavaScript ex) `#${variable} of stuff`
languageList.append("russian")
# Also could be cool to learn
del languageList[5]
popped = languageList.pop(1)
print(popped)
languageList.remove("italian")
languageList.sort()
# Every other function used in Chapter-3 occurs in previous exercise.
