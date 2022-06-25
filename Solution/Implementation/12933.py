from tokenize import String



sound = input()
visited = [0] * len(sound)
duck_sound = "quack"
print(sound[2])

for i in range(5):
    if(sound[i] == 'q'):
        if(visited[i] == False):
            visited[i] = True
            for j in range(i, len(sound)):
                if(sound[j] == 'u'):
                    visited[j] 