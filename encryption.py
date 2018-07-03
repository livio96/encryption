#!/usr/bin/python
# -*- coding: utf-8 -*-
import wx 

def onButton(event):
    print ("Button Pressed")


    



plain_text = []
encrypted_list = []
secret_key = ''


def read_from_plaintext():

# read all the information and store it to a list

    myfile = open('send_message.txt', 'r')
    plain_text = myfile.readlines()
    return plain_text


def write_encrypted_file():
    encrypted_list = []
    plain_text = read_from_plaintext()
    myfile1 = open('encrypted_message.txt', 'w')
    for i in range(0, len(plain_text)):
        for c in plain_text[i]:
            myfile1.write(str(ord(c)))
            encrypted_list.append(ord(c))  # store the ecrypted text to a list
    return encrypted_list


def key_generator():
    secret_key = ''
    ch = ''
    string_converted = ''
    count = 0

    encrypted_list = write_encrypted_file()
   

    i = int(len(encrypted_list) / 2)
    list_length = len(encrypted_list)
    
    with open('encrypted_message.txt') as fileobj:
        for line in fileobj:
            for ch in line:
                if count < 2:
                    string_converted = str(ch)  # security key consists of the first two letters of the encrypted

                                         # file and ab2 in the end.

                    secret_key += string_converted
                    count += 1
                else:
                    break

        secret_key += 'ab2'  # append ab2 to the end of the string....

    print("You text file was encrypted successfully.")
    print ('The decryption key is : ' + secret_key)
    return secret_key


def sender_function(self):
    read_from_plaintext()
    write_encrypted_file()
    key_generator()

def receiver_function(self):
    
    flag = 0
    iterator = 0
    ch = ''
    real_key = ''
    sec_key = str('Enter security key ')  # give access with the security key is correct

                                        # otherwise deny acces

    with open('encrypted_message.txt') as fileobj:
        for line in fileobj:
            for ch in line:
                if iterator < 2:
                    random_string = str(ch)
                    real_key += random_string
                    iterator += 1
                else:
                    break
    if sec_key == real_key + 'ab2':
        print ('Password is correct!!!')
        flag += 1
    while sec_key != str(real_key + 'ab2'):
        print ('ACCESS DENIED!!!')
        sec_key = input('Enter security key ')
        if sec_key == real_key + 'ab2':
            print ('Password is correct!!!')
            flag += 1
            break

        # algorithm to decrypt the encrypted file so user can read the original
        # content of plaintext.txt

    if flag != 0:  # if user entered the right security key, do the following
        enc_list = write_encrypted_file()

        myfile3 = open('received_message.txt', 'w')
        for i in enc_list:
            myfile3.write(chr(i))


def main_func(self):
    random_string = ''
    print ('1.Sender')
    print ('2.Receiver')
    num_choice = int(input('>> '))

    while num_choice < 1 or num_choice > 2:
        print ('Try again')
        num_choice = int(input('>> '))
    # ------------------------------------------------------

    if num_choice == 1:  # If user is the message Sender
        sender_function()
        

    # -------------------------------------------------------....        #if user is message receiver

    if num_choice == 2:
        receiver_function()
        

app = wx.App()
frame = wx.Frame(None, -1, 'Ncryptor')
frame.SetDimensions(0,0,500,200)

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour('pink')  #add background color 
wx.StaticText(panel, -1, "Please make a selection : ", pos=(10,22))
sender_button = wx.Button(panel, wx.ID_ANY, 'Encrypt a file', (200,22))
receiver_button = wx.Button(panel, wx.ID_ANY, 'Decrypt a file', (340,22))
sender_button.Bind(wx.EVT_BUTTON, sender_function)
receiver_button.Bind(wx.EVT_BUTTON, receiver_function)


    
    

frame.Show()
frame.Centre()
app.MainLoop()

