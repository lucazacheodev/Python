with open('players.txt', 'r') as infile:    
    with open('players.csv', 'w') as outfile:        
        for line in infile:
            csv_line = ','.join(line.strip().split())            
            outfile.write(csv_line + '\n')