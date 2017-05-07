"""from pyDes import *"""
import sys
from collections import deque
import numpy as np
import random

class Utilities:
    def toBinary(self, input):
        temp = ""
        output=[]
        for i in range(len(input)):
            temp = temp+(str(bin(ord(input[i]))[2:].zfill(8)))
        for i in range(len(temp)):
            output.append(int(temp[i]))
        return output

    def initialPermute(self,input):
        ip = [57, 49, 41, 33, 25, 17, 9, 1,
           59, 51, 43, 35, 27, 19, 11, 3,
           61, 53, 45, 37, 29, 21, 13, 5,
           63, 55, 47, 39, 31, 23, 15, 7,
           56, 48, 40, 32, 24, 16, 8, 0,
           58, 50, 42, 34, 26, 18, 10, 2,
           60, 52, 44, 36, 28, 20, 12, 4,
           62, 54, 46, 38, 30, 22, 14, 6]
        output = []
        for i in range(64):
            output.append(input[ip[i]])
        return output

    def divide(self,input):
        output1=input[:(len(input)/2)]
        output2=input[len(input)/2:]
        return{'left':output1,'right':output2}

    def expansion(self,input):
        output=[]
        et = [31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10, 11, 12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19, 20,
          19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31, 0]
        for i in range(48):
            output.append(input[et[i]])
        return output
    def initialKeyPermute(self, input):
        pc1 = [56, 48, 40, 32, 24, 16, 8,
                0, 57, 49, 41, 33, 25, 17,
                9, 1, 58, 50, 42, 34, 26,
                18, 10, 2, 59, 51, 43, 35,
                62, 54, 46, 38, 30, 22, 14,
                6, 61, 53, 45, 37, 29, 21,
                13, 5, 60, 52, 44, 36, 28,
                20, 12, 4, 27, 19, 11, 3
            ]
        output=[]
        for i in range(len(pc1)):
            output.append(input[pc1[i]])
        return output
   
    def shifting(self,input):
        temp = self.divide(input)
        left= temp['left']
        right= temp ['right']
        output=[]
        rotations = [ 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 ]
        for j in range(16):
            for i in range (rotations[j]):
                left.append(left[0])
                right.append(left[0])
                del left[0]
                del right[0]
            output.append(left+right)
        return output

    def compressKey(self,input):
        pc2 = [
            13, 16, 10, 23, 0, 4,
            2, 27, 14, 5, 20, 9,
            22, 18, 11, 3, 25, 7,
            15, 6, 26, 19, 12, 1,
            40, 51, 30, 36, 46, 54,
            29, 39, 50, 44, 32, 47,
            43, 48, 38, 55, 33, 52,
            45, 41, 49, 35, 28, 31
        ]
        output=[]
        for i in range(len(pc2)):
            output.append(input[pc2[i]])
        return output
    
    def xorArray(self, input1, input2):
        output=[]
        for i in range(len(input1)):
            output.append(input1[i]^input2[i])
        return output

    def sbox(self, input):
        iteration = len(input)/6
        strOutput=""
        sbox = [
        # S1
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
            0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
            4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
            15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

            # S2
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
            3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
            0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
            13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

            # S3
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
            13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
            13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
            1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

            # S4
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
            13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
            10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
            3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

            # S5
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
            14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
            4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
            11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

            # S6
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
            10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
            9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
            4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

            # S7
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
            13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
            1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
            6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

            # S8
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
            1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
            7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
            2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
        ]
        for i in range(iteration):
            temp = input[i*6:(i+1)*6]
            shuffle = temp[:1]+temp[5:]+temp[1:5]
            toInt = int("".join(str(i) for i in shuffle),2)
            strOutput = strOutput+bin(sbox[i][toInt])[2:].zfill(4)
        output=[]
        for i in range(len(strOutput)):
            output.append(int(strOutput[i]))
        return output

    def permutation(self, input):
        p = [
            15, 6, 19, 20, 28, 11,
            27, 16, 0, 14, 22, 25,
            4, 17, 30, 9, 1, 7,
            23,13, 31, 26, 2, 8,
            18, 12, 29, 5, 21, 10,
            3, 24
        ]
        output=[]
        for i in range(len(p)):
            output.append(input[p[i]])
        return output
    def finalPermutation(self, input):
        fp = [
            39,  7, 47, 15, 55, 23, 63, 31,
            38,  6, 46, 14, 54, 22, 62, 30,
            37,  5, 45, 13, 53, 21, 61, 29,
            36,  4, 44, 12, 52, 20, 60, 28,
            35,  3, 43, 11, 51, 19, 59, 27,
            34,  2, 42, 10, 50, 18, 58, 26,
            33,  1, 41,  9, 49, 17, 57, 25,
            32,  0, 40,  8, 48, 16, 56, 24
        ]
        output=[]
        for i in range(len(fp)):
            output.append(input[fp[i]])
        return output

    def byteToString(self, input):
        result = []
        pos = 0
        c = 0
        while pos < len(input):
            c += input[pos] << (7 - (pos % 8))
            if (pos % 8) == 7:
                result.append(c)
                c = 0
            pos += 1
        result =  ''.join([ chr(c) for c in result ])
        return bytes(result)

    def data_padding(self,input):

        block = []
        if((len(input)%64) != 0):
            print("Padding data to make multiple of 64 ..\n")
            input += (64 - ((len(input)) % 64)) * [0]
            return input
        else:
            return input

    def data_to_blocks(self, input):
        print("Creating blocks of 64 bits..\n")
        quotient, remainder = divmod(len(input), 64)
        block = []
        ind = []
        index = 0
        i = 0
        while (i < quotient):
            ind = input[index: index+64]
            block.append(ind)
            index += 64
            i += 1
        return block

    def after_decrypt_block(self, input):
        output = []
        output = input
        return output

    def modes(self, mode_input, bin_input):
        if (mode_input == 2):
            iv=[]
            row, col = 0, 64
            self.iv = np.random.randint(2, size=64)
            return self.xorArray(self.iv, bin_input)
        else:
            return bin_input


    def modes_decrypt(self, mode_input, decrypted_block):
        
        if (mode_input == 1):
            return decrypted_block
        else:
            return self.xorArray(self.iv, decrypted_block)

           
util = Utilities()

class Des(Utilities):
    util.iv = []
    def encryption(self, input):
        print("Encryption starting...\n")
        ipData = util.initialPermute(input)
        divideData = util.divide(ipData)
        binaryKey = util.toBinary("qwertyui")
        permutedKey = util.initialKeyPermute(binaryKey)
        self.keyArray = util.shifting(permutedKey)
        for i in range(16):
            rightExpanded = util.expansion(divideData["right"])
            permutedKey = self.keyArray[i]
            compressedKey = util.compressKey(permutedKey)
            xored = util.xorArray(rightExpanded, compressedKey)
            sboxed = util.sbox(xored)
            permutedData = util.permutation(sboxed)
            finalXor = util.xorArray(divideData["left"],permutedData)
            divideData["left"] = divideData["right"]
            divideData["right"] = finalXor
        finalCipher= util.finalPermutation(divideData["right"]+divideData["left"])
        print("Cipher created...\n")
        return finalCipher
    
    def decryption(self, input):
        print("Decryption starting...\n")
        decryptString =[]
        decryptInput=util.initialPermute(input)
        divideData = util.divide(decryptInput)
        binaryKey = util.toBinary("qwertyui")
        permutedKey = util.initialKeyPermute(binaryKey)
        i=15
        while(i>-1):
            rightExpanded = util.expansion(divideData["right"])
            permutedKey = self.keyArray[i]
            compressedKey = util.compressKey(permutedKey)
            xored = util.xorArray(rightExpanded, compressedKey)
            sboxed = util.sbox(xored)
            permutedData = util.permutation(sboxed)
            finalXor = util.xorArray(divideData["left"],permutedData)
            divideData["left"] = divideData["right"]
            divideData["right"] = finalXor
            i-=1
        finalCipher= util.finalPermutation(divideData["right"]+divideData["left"])
        print("Decryption done..\n")
        return finalCipher
        

    def mode(self, input_mode, bin_blocks):
        print("you selected mode: \n", input_mode)
        if (input_mode == 1):
           
            decryptString =[]
            no = 0
            for i in bin_blocks:
                print("Block sent for encryption \n", no)
                encrypted_data = self.encryption(i)
                decrypted_data = self.decryption(encrypted_data)
                decryptString.append(util.byteToString(decrypted_data))
                no +=1
            decryptString = ''.join(decryptString)
            print(decryptString)
        else:

            decr = []
            
            row, col = 0, 64
            self.iv = np.random.randint(2, size=64)
            no = 0
            for i in bin_blocks:
                print("Block sent for encryption \n", no)
                i  = self.xorArray(self.iv, i)
                processed_block_enrypt = self.encryption(i)
                processed_block_decrypt = self.decryption(processed_block_enrypt)
                decrypted_binary = self.xorArray(self.iv, processed_block_decrypt)
                # print(decrypted_binary)
                output = util.byteToString(decrypted_binary)
                decr.append(util.byteToString(decrypted_binary))
                no+=1
            decr = ''.join(decr)
            print(decr)
            



            

encrypt_decrypt = Des()
# mode=2
mode = raw_input("Which mode would you like to implement: \n")
inp_data = raw_input("Enter message you would like to send: \n")
# binaryData = util.toBinary("abcdefghghpoiuytmnbvcxzasdfghjkl p o uytplmkjn b plploikjnmbhgyuitfvb          nml,k89076543321qaz ")
binaryData = util.toBinary(inp_data)
print binaryData
padded_data = util.data_padding(binaryData)
blocks = util.data_to_blocks(padded_data)
output = encrypt_decrypt.mode(mode, blocks)
