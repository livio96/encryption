
plain_text = [] 
encrypted_list = [] 
secret_key = ""


def read_from_plaintext():
#read all the information and store it to a list
	myfile = open("send_message.txt", 'r')
	plain_text = myfile.readlines()
	return plain_text 


def write_encrypted_file():
	encrypted_list = [] 
	plain_text = read_from_plaintext()
	myfile1 = open("encrypted_message.txt" , 'w')
	for i in range(0, len(plain_text)):
		for c in plain_text[i]:
			myfile1.write(str(ord(c)))
			encrypted_list.append(ord(c))  #store the ecrypted text to a list
	return encrypted_list

		

def key_generator():
	secret_key = ""
	ch = ''
	string_converted = ""
	count = 0 

	encrypted_list = write_encrypted_file()
	print("Press 1 to generate a secret key")
	choice = int(input())
	
	i= int(len(encrypted_list)/2)
	list_length = len(encrypted_list)

	while(choice != 1):	
		print("Try again")
		choice = int(input())
	
	if(choice == 1):
		with open("encrypted_message.txt") as fileobj:
			for line in fileobj:
				for ch in line:
					if(count<2):
						string_converted = str(ch)   #security key consists of the first two letters of the encrypted
									     #file and ab2 in the end.
						secret_key += string_converted
						count+=1
					else:
						break; 
	
						
		secret_key +="ab2" 			#append ab2 to the end of the string	

	print("The secret key is : " + secret_key)
	return secret_key	
	

def main_func():
	random_string = ""
	print("1.Sender")
	print("2.Receiver")
	num_choice = int(input(">> "))

	while(num_choice < 1  or num_choice > 2):
		print("Try again")
	#------------------------------------------------------
	if(num_choice == 1):           			 #If user is the message Sender 
		read_from_plaintext()
		write_encrypted_file()
		key_generator()
	#-------------------------------------------------------	        #if user is message receiver
	if(num_choice == 2):
		flag= 0 						
		iterator = 0
		ch = ''
		real_key = ""
		sec_key = str(raw_input("Enter security key ")) 		#give access with the security key is correct 
										#otherwise deny acces 
		with open("encrypted_message.txt") as fileobj:
    			for line in fileobj:  
       				for ch in line:
					if(iterator<2):
						random_string = str(ch)
						real_key +=random_string
						iterator+=1
					else: break
		if(sec_key == (real_key + "ab2")):
			print("Password is correct!!!")
			flag +=1
		while(sec_key != str(real_key+ "ab2")):
			print("ACCESS DENIED!!!")	
			sec_key = raw_input("Enter security key ") 
			if(sec_key== (real_key + "ab2")):
				print("Password is correct!!!")
				flag+=1
				break ; 

		#algorithm to decrypt the encrypted file so user can read the original
		#content of plaintext.txt
		
		if(flag != 0 ): 				#if user entered the right security key, do the following 
			enc_list = write_encrypted_file()
			
			myfile3 = open("received_message.txt" , 'w')
			for i in enc_list:
				myfile3.write(chr(i))


					
		

		

		
			
		 
			 
						
				
           		
		
			
main_func()

	
			
		
