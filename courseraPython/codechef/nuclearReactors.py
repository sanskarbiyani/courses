'''A,N,K = map(int,input().split())
chambers = [0]*K
for i in range(A):
    chambers[0] += 1
    for j in range(len(chambers)):
        if chambers[j] > N:
            if j == K-1:
                chambers[j] = 0
                break
            chambers[j+1] +=1
            chambers[j] = 0
        else:
            break
print(*chambers, sep=' ')
'''

from sys import stdin, stdout
no_of_particles, max_particle, no_of_chamber=map(int,stdin.readline().split())
chamber=[0 for i in range(no_of_chamber)]
max_particle+=1
for i in range(no_of_chamber):
    chamber[i] = no_of_particles % max_particle
    no_of_particles = no_of_particles//max_particle

print(*chamber)
