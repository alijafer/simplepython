from faker import Faker
from faker.providers import internet
# To create a json file
import json		

# For student id
from random import randint	

fake = Faker("ar_SA")
fake.add_provider(internet)
def input_data(x):

	# dictionary
    student_data ={}
    for i in range(0, x):
        student_data[i]={}
        student_data[i]['id']= randint(1, 100)
        student_data[i]['name']= fake.name()
        student_data[i]['address']= fake.address()
        student_data[i]['country'] = fake.country()
        student_data[i]['latitude']= str(fake.latitude())
        student_data[i]['longitude']= str(fake.longitude())
        student_data[i]['tast'] = str(fake.email())
        student_data[i]["ip"]= fake.ipv4_private()
        student_data[i]["active"] = fake.boolean()
        student_data[i]["DOB"]= str(fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115))
        student_data[i]['plate']= (fake.license_plate() +fake.license_plate_en())
        student_data[i]['color'] = fake.safe_color_name()
    print(student_data)

	# dictionary dumped as json in a json file
    with open('studentsgs.json', 'w', encoding='utf-8') as fp:
	    json.dump(student_data, fp, ensure_ascii=False)
	

def main():

	# Enter number of students
	# For the above task make this 100
	number_of_students = 19
	input_data(number_of_students)
main()
# The folder or location where this python code
# is save there a students.json will be created
# having 10 students data.
