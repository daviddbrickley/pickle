import pickle
#1

leader = {}
leader['Jacore Baptiste'] = '(845) 200-6250'
leader['Andrew'] = '(925) 727-4611'
leader['Aris Carter'] = '(510) 229-6359'
leader['Gaberiel Reader'] = '(510) 326-5834'
leader['Richard Kamau'] = '(510) 228-5623'

#2. create/open pod_nbrs.pkl file
pod_file = open('pod_nbrs.pkl', 'wb')


#3 Write pod leader number to file
pickle.dump(leader,pod_file)

#4 Member Numbers
member = {}
member['Miles'] = '(510) 604-3128' 

#5 Write member numbers to pod_file
pickle.dump(member,pod_file)

#6 close pod_file
pod_file.close()

#7 open pod folr
pod_file = open('pod_nbrs.pkl', 'rb')

#8 leader numbers
print('Leaders: ')
for key,value in leader.items():
    print(key, value)

print('/n')


print('members')
for key,value in member.items():
    print(key, value)

print('\n')

#10 close pod_file
pod_file.close()
