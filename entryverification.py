'''the concert is going to take place on 12th,13th and 14th of march in slikboard.the artists are martin garrix,alesso,charlotte.
people shuold book their tickets of rs.999yellow band for general,1999blue band for vip and 2999red band  for back stage. 
write a program for it so that the differnt categories ticket mem should enter to their respective places.
'''
concertname='techno'
artists=input('enter your artist name:' )
date=input('enter you booking date:')
name=input("enter your name:")
band_colour_stage=input('enter your band colour:')
gender=input('enter your gender(male/female):')
place='silkboard'
age=int(input('enter your age:'))
floorno=2
if gender=='male':
  givenas='mr.'
elif gender=='female':
  givenas='mrs.' 
else:
  givenas=""
print(f'welcome to the {concertname} concert verification process {givenas}{name}')
print('verification:')
print(f'artist={artists}')
print(f'date={date}')
print(f'name={name}')
print(f'gender={gender}')
print(f'bandcolour and stage={band_colour_stage}')
print(f'age={age}')
if age>=21:
 if (artists == 'martin garrix' and date == '12th march') or (artists == 'alesso' and date == '13th march') or (artists=='charlotte' and date=='14th march'):
  if band_colour_stage=='yellow-general':
    print(f" hello {givenas}{name} welcome to the {concertname} concert of {artists} at {place}{floorno}") 
    print(f"you have to enter at general entry zone.")
  elif band_colour_stage=='blue-vip': 
    print(f" hello {givenas}{name} welcome to the {concertname} concert of {artists} at {place}{floorno}.")
    print(f"you have to enter at vip entry zone.")
  elif band_colour_stage=='red-backstage':
     print(f" hello {givenas}{name} welcome to the {concertname} concert of {artists} at {place}{floorno}.")
     print(f"you have to enter at backstage zone near stage.")
 else:
   print('sorry your band colour does not match you cant enter')
   print('please go and check at the another entry gate')
else :
 print('sorry your details did not match...entry denied')
 print('sorry your age must be atleast 21 years to enter the concert')

print('\n "Thankyou for providing the details"\n')
print("For any assistance, feel free to reach out to our help desk.")
print('be safe, be hydrated, be supportive.')
print("drive home safely.\n LOVE from techno team. ")
print("We look forward to seeing you again at our future events!")
