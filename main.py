#  Function to convert temp
def temp_conv(temp):
    pt = (5/9) * (temp - 32)
    print(f'If it is', temp, 'degrees in Farenheit, than it is ', pt, 'degrees in celcius')
     
#  Function to convert weight
def weigh_conv(weight):
    pw = weight/2.2046
    print(f'If the object weighs', weight,'in pounds, then it weighs', pw, 'in kilograms')

#  Function to convert distance
def dist_conv(dist1):
    pd1 = dist1 * .6213711922 
    print(f'If the distance is', dist1,'kilometers, then it is', pd1, 'miles')

def dist_conv2(dist2):
    pd2 = dist2 * .3937007874
    print(f'If the distance is', dist2 ,'in centimeters, then it is', pd2, 'in inches')

#  Function to convert speed
def speed_conv(speed):
    ps = speed * 1.609344
    print(f'If the speed was',speed,' in miles per hour, then in kilometers per hour the speed would be', ps)

#  Loop to have the question repeat after a conversion is performed until 0 is inputted
while True:
    type = int(input('Which conversion do you want to perform: 1: (f to c), 2: (kg to lb), 3: (km to ml), 4: (cm to in), 5: (mph to kph), 0: Quit   '))
    if type == 1:
        temp_conv(int(input('Enter the temperature in F:')))
    elif type == 2: 
        weigh_conv(int(input('Enter the weight in lb:')))
    elif type == 3:
        dist_conv(int(input('Enter the distance in km:')))
    elif type == 4:
        dist_conv2(int(input('Enter the distance in cm:')))
    elif type == 5: 
        speed_conv(int(input('Enter the speed in mph:')))
    else: 
        print('See you next time!')
        break   #  Breaks loop
    


        

