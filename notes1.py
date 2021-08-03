ORM(Object Relational Mapping):
	- in django we are using ORM to perform CRUD operations
	- To Practice ORM queries we have to open django shell by using ''' python manage.py shell'''
	- we have make a connection between shell prompt and models.py
				-'''from FirstApp.models import Register'''
	- we have to insert a record
	- SQL query is
			'''insert into register values("sanju","sanju@gmail.com") '''
			-ORM query is:
					- reg=Register(name="san",email="sani@gmail.com")
					-reg.save()
					(OR)
					reg=register.objects.create(name="")
	- Retrieve records:
		-Retrieve all records
			-sql QUERY:
				'''select * from Register'''
			-ORM query:
				data=Register.objects.all()
			-retrieve a specific column:
				''' select email from Register'''
			- ORM QUERY:
				- ''' data=Register.objects.all() '''
			- iterate loop like this
					''' for row in data:
							print(row.email)
- retrieve only specific column
		-Sql Query:
		    select * from Register where name="sanju" '''
		    -ORM QUERY:
		    -to retrieve a specific row we have 2 diffrent methods
		    		- by using filter()#accept multiple records
		    				''' info=Register.objects.filter(name="sanju")'''
		    		- by using get() dont accept multiple records	
		    		    info=Register.objects.get(id=1)

- i want to retrieve a record whose name is sanju and email is s123@gmail.com.
 		- SQL QUERY is:
 				'''select * from register where name="" and email="" '''
 				- ORM QUERY:
 					'''info=Register.objects.filter(name="sanju",email="s123@gmail.com") '''


- to retrieve first record
		-''' info=Register.objects.all().first()'''

- to retrieve last record
		-''' info=Register.objects.all().last()'''

- to retrieve top two records
		-''' info=Register.objects.all()[:2]'''#we use slicing

- to update a record :
    - update a record:
    -SQL QUERY:
    	- update register set email="sandhya@gmail.com" where name="sanju" '''
    	- ORM QUERY:
    	'''
    	  info=Register.objects.get(name="sanju")
    	  info.email="sandhya@gmail.com"
    	  info.save()
    	  '''

- delete a record:
	-SQL QUERY:
	  ''' delete from Register where name="sanju" '''
	  - ORM QUERY:
	  '''
	  info=Register.objects.get(name="Sandhya")
	  info.delete()
	  '''

- to remove all records:
   - ''' delete from register '''
   -ORM QUERY:
     '''Register.objects.all().delete()'''

























