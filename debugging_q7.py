# `raw_input` ka use kar ke user se din aur abhi ka samay (lunch, dinner) input
# leke uss samay ka menu print karvana hai. Abhi hum sirf monday aur tuesday ke
# liye likh rahe hain
# Monday aur Tuesday dono time daal roti banegi, bas Tuesday raat ko Pav Bhaji banegi
# Neeche waale program mein jab tuesday daalte ho toh pav bhaji print nahi hota.
# Isko sahi karo.
#day = raw_input("Aaj ka din kya hai? (monday/tuesday) > ")
#time = raw_input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
#if day == "monday" or day == "tuesday":
#condition may humne time mention nhi  kiya tha
    #print "Daal-Roti banegi aaj"
#is condition mai bhi nhi kiya tha time mention
#elif day == "tuesday" and time == "dinner":
    #print "Pav-Bhaji banegi aaj toh :)"
day = raw_input("Aaj ka din kya hai? (monday/tuesday) > ")
time = raw_input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
if day == "monday" or day=="tuesday"and time=="lunch":
    print "Daal-Roti banegi aaj"
elif day == "tuesday" and time == "dinner":
    print "Pav-Bhaji banegi aaj toh :)"

