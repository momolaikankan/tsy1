with open('123', 'r') as f:
    lis = []
    for line in f:
        line_one = line.strip()
        lis.append(line_one.split())
print(lis)
lis = [['Ep02', 'SC210319', 'shot01', 'MOCAP'], ['Ep02', 'SC210319', 'shot02', 'MOCAP'], ['Ep02', 'SC210319', 'shot03', 'MOCAP'], ['Ep02', 'SC210319', 'shot04', 'MOCAP'], ['Ep02', 'SC210319', 'shot05', 'MOCAP'], ['Ep02', 'SC210319', 'shot06', 'MOCAP'], ['Ep02', 'SC210319', 'shot07', 'MOCAP'], ['Ep02', 'SC210319', 'shot08', 'MOCAP'], ['Ep02', 'SC210319', 'shot09', 'MOCAP'], ['Ep02', 'SC210319', 'shot10', 'MOCAP'], ['Ep02', 'SC210319', 'shot11', 'MOCAP'], ['Ep02', 'SC210319', 'shot12', 'MOCAP'], ['Ep02', 'SC210319', 'shot13', 'MOCAP'], ['Ep02', 'SC210319', 'shot14', 'MOCAP'], ['Ep02', 'SC210319', 'shot15', 'MOCAP'], ['Ep02', 'SC210319', 'shot16', 'MOCAP'], ['Ep02', 'SC210319', 'shot17', 'MOCAP'], ['Ep02', 'SC210319', 'shot18', 'MOCAP'], ['Ep02', 'SC210319', 'shot19', 'MOCAP'], ['Ep02', 'SC210319', 'shot20', 'MOCAP'], ['Ep02', 'SC210319', 'shot21', 'MOCAP']]
print(len(lis))