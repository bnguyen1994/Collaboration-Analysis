import mpi4py
mpi4py.rc.recv_mprobe = False
from mpi4py import MPI

def mergeDicts(x,y):
    commonKeys = list(set(x.keys()).intersection(set(y.keys())))
    for key in commonKeys:
        x[key] = x[key] + y[key]
        del y[key]
    z = x.copy()
    z.update(y)

    return z


comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

workers = range(1,size)
workList = [[] for x in range(size)]
workerData = None
workerDictList = None


if rank == 0:
    print 'Opening main file...'
    authArtFile = open('authorsArticlesFile2','r')
    masterDict = {}

    workerIndex = 0
    lineCounter = 0
    print 'Analyzing contents of file...'
    workList[0] = 'placeholder'
    for line in authArtFile:
        if lineCounter == 81672:
            workerIndex += 1
            lineCounter = 0

        if workerIndex < size - 1:
            workList[workerIndex+1].append(line.replace('\n',''))
        else:
            break

        lineCounter += 1

    print 'Closing main file...'
    authArtFile.close()
    print len(workList)
    workerData = comm.scatter(workList, root = 0)
    comm.Barrier()
    workerDictList = comm.gather(workerDictList,root=0)

    for entry in workerDictList:
        if type(entry) == dict:
            masterDict = mergeDicts(masterDict,entry)
        else:
            continue

    authArtDictFile = open('authorArticleDictFile','w')
    for author,idList in masterDict.items():
        fileLine = author + ':' + str(idList) + '\n'
        authArtDictFile.write(fileLine)

    authArtDictFile.close()
    print 'Done!'

else:
    workerData = comm.scatter(workList, root = 0)
    data = workerData

    workerDict = {}

    progressCounter = 0
    for entry in data:
        if progressCounter %  10 == 0:
            progressCounter = 0

        author,idNum = entry.split(',')
        idNum = idNum.replace('\t','')
        if author not in workerDict.keys():
            workerDict[author] = [idNum]
        else:
            workerDict[author].append(idNum)
        progressCounter += 1
    comm.Barrier()
    workerDictList = comm.gather(workerDict,root=0)
