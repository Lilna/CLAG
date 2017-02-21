# email="Lillian@cornell.edu"
# position = email.find("@")
# print position 
# UserName - email[0:position]
# print UserName
# len_username = len(UserName)
# print len_username
# len_username = len(email[0:position])
# print "UserName is {0} and its length is {1}".format(email[0:position],position)
# print "UserName is {0}".format(email[0:position])
# saying = "   The fox jumped over the log and bumped its head.    "
# print saying
# print saying.strip()
# gender = "F"
# print gender
students = 10
capacity = 50
teaching_assistants = 5
if students < capacity :
	print "Keep recruiting"
else:
	print "End of ticket signups"
if teaching_assistants == 0:
	print "None? Uh oh!"
elif teaching_assistants < students / 5:
	print "Keep recruiting TAs"
else:
	print "We have enough TAs!"