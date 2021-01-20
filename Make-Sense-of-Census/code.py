# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
path
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data)
print(type(data))

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
print(new_record)
census = np.concatenate((data, new_record), axis = 0)
print(census)

#Code starts here



# --------------
#Code starts here
import numpy as np

age = np.array(census[:,0])
print(age)

max_age = np.max(age)
print(max_age)
min_age = np.min(age)
print(min_age)

age_mean = np.mean(age)
print(age_mean)

age_std = np.std(age)
print(age_std)


# --------------
#Code starts here
import numpy as np
#census = np.array([])
#print(census)

#Create a new array called 'age' by taking only age column(age is the column with index 0) of 'census' array.

#age = np.array(census[:,0])
#print(age)

race_0 = census[census[:,2]==0]
print(race_0)

race_1 = census[census[:,2]==1]
print(race_1)

race_2 = census[census[:,2]==2]
print(race_2)

race_3 = census[census[:,2]==3]
print(race_3)

race_4 = census[census[:,2]==4]
print(race_4)

#race_0 = np.array(census[:0,0])
#print(race_0)
#
#race_0 = np.array(census[:0,:0])
#print(race_0)

#race_0 = np.array(census[0:,0:])
#print(race_0)

#race_0 = np.array(census[0:,:0])
#print(race_0)

8888888888888888#race_0 = np.array(census[0,0:])
#print(race_0)

#race_0 = np.array(census[1,0:])
#print(race_0)

#race_0 = np.array(census[:1,0:])
#print(race_0)

#race_0 = np.array(census[:1,0])
#print(race_0)

#race_0 = np.array(census[1:,0])
#print(race_0)

#race_0 = np.array(census[2:,:0])
#print(race_0)

#race_0 = np.array(census[2,0:])
#print(race_0)

#race_0 = np.array(census[:2,0:])
#print(race_0)

#race_0 = np.array(census[:2,0])
#print(race_0)

#race_0 = np.array(census[2:,0])
#print(race_0)

#race_0 = np.array(census[2:,:0])
#print(race_0)

#race_1 = np.array(census[:,:1])
#print(race_1)

#race_2 = np.array(census[:,2])
#print(race_2)

#race_3 = np.array(census[:,3])
#print(race_3)

#race_4 = np.array(census[:,4])
#print(race_4)
#
#len_0 = np.array(len(race_0))
#len_0 = len(np.array(race_0))
len_0 = len(race_0)
print(len_0)

len_1 = len(race_1)
print(len_1)

len_2 = len(race_2)
print(len_2)

len_3 = len(race_3)
print(len_3)

len_4 = len(race_4)
print(len_4)
#len_0 = print(len(race_0))

#len_1 = len(np.array(race_1))
#print(len_1)

#if len(race_0) 
#minority_race = np.min(census[census[:,2]==0],axis=1)
#minority_race = print race[np.argmin(race[:, 0]), 2]
#print(minority_race)

minority_race = ''

#minority_race = census[np.argmin(census[:,2]), 1]
#minority_race = np.min(census[census[:,2]==0],axis=0)
#print(minority_race)

#minority_race = np.min(census[census[:,2]==2],axis=0)
#print(minority_race)
#minority_race = np.min(census[census[:,2]],axis=1)
#print(minority_race)

#minority_race = np.min(census[census[:,1]==0.0],axis=0)[2]
#print(minority_race)


#minority_race = np.min(census[census[:,2]],axis=0)[2]
#print(minority_race)

#minority_race = np.minimum(race_0, race_1) # race_2, race_3, race_4)
#print(minority_race)

#minority_race = min(len(race_0, race_1, race_2, race_3, race_4))
#print(minority_race)

#minority_race = census.min()
#print(minority_race)

#minority_race = census.min([2])
#print(minority_race)


#minority_race = np.min([:,2])
#print(minority_race)


#minority_race = np.min([census[:,2]])
#print(minority_race)


#minority_race = np.min(census[:,2])
#print(minority_race)


#minority_race = np.min(census[census]) #[race_0, race_1, race_2, race_3, race_4])
#print(minority_race)




if len(race_0) < len(race_1) and len(race_0) < len(race_2) and len(race_0) < len(race_3) and len(race_0) < len(race_4):
   minority_race = 0
   print(minority_race)
elif len(race_1) < len(race_0) and len(race_1) < len(race_2) and len(race_1) < len(race_3) and len(race_1) < len(race_4):
   minority_race = 1
   print(minority_race)
elif len(race_2) < len(race_0) and len(race_2) < len(race_1) and len(race_2) < len(race_3) and len(race_2) < len(race_4):
   minority_race = 2
   print(minority_race)
elif len(race_3) < len(race_0) and len(race_3) < len(race_1) and len(race_3) < len(race_2) and len(race_3) < len(race_4):
   minority_race = 3
   print(minority_race)
elif len(race_4) < len(race_0) and len(race_4) < len(race_1) and len(race_4) < len(race_2) and len(race_4) < len(race_3):
   minority_race = 4
   print(minority_race)


# --------------
#Code starts here

senior_citizens = census[census[:,0]>60]
print(senior_citizens)

working_hours_sum = sum(senior_citizens[:,6])
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = (working_hours_sum/senior_citizens_len)
print(avg_working_hours)



# --------------
#Code starts here
#import statistics
high = census[census[:,1]>10]
print(high)

low = census[census[:,1]<=10]
print(low)

avg_pay_high = np.mean(high[:,7])
print(avg_pay_high)

avg_pay_low = np.mean(low[:,7])
print(avg_pay_low)


np.array_equal(avg_pay_high, avg_pay_low)



