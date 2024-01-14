monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

} #'{}' use these for dictionaires - key value pairs (NO DUPLICATE KEYS)

#Access to this dictionary:
#One of the ways to see the full name/value is the use of "[]" or ".get" after the var name
#Ex. (monthConversions.get/"monthConversions[]")
#"Not a valid key" is the default val.

print(monthConversions.get("Luv", "Not a valid key")) 
