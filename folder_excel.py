import os
import xlsxwriter

#Create workbook
workbook = xlsxwriter.Workbook('image2.xlsx')

#create Sheet
worksheet1 = workbook.add_worksheet("image")
#Create Col 
worksheet1.write('A1', 'image')
worksheet1.write('B1', 'image_Path')



#Take path of folder
path=r"E:\script\special_4_classes/"

#Find list of all folder 
folder=os.listdir(path)
print(folder)
#Read Imageg present in folder 

#Now write each image from folder to excel 
r=1
c=0
for i in folder:
	for img in os.listdir(path+i):
		if img != "char.txt":
			print(i)
			print(img)
			worksheet1.insert_image(r,0,path+i+"/"+img)
			worksheet1.insert_image(r,1,img)
			r=r+1

workbook.close()
