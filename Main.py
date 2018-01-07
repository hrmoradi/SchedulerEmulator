import SchedulerEmulator.Settings as Set
import copy
from SchedulerEmulator.JobCreator import ClassJobCreator as CJ
from SchedulerEmulator.Scheduler import ClassSchduler as CS

class MainClass:
    def mainMethod():
        meo=[]
        first=[]
        last=[]

        failed=0
        scaled=1
        unused=2
        gain=3

        print("\nnumber of iteration: ",Set.numberOfIteration,
              "| number of time interval: ", Set.NumberOfTimeInterval,
              "| each interval: ",Set.eachTimeInterval,
              "| avg Load: ", Set.avgSysLoad,
              "| random Job: ",Set.randJob)


        """ Running Simulation iterations """

        for i in range(Set.numberOfIteration):

            print("\n Main Iteration:", i,"\n")
            #print("\n\n***Main:createJobList")
            JobCreator= CJ()
            jobList=JobCreator.MainJobCreator()

            #print("\n\n***Main:Emulate TSRA-MEO")
            Set.firstOptionOnly = False
            Set.MEO = True
            Set.lastOption = False
            EmulateMEO =CS()
            results=EmulateMEO.MainScheduler(jobList,Set.resources)
            meo.append(results)

            #print("\n\n***Main:Emulate TSRA-First")
            Set.firstOptionOnly=True
            Set.MEO=False
            Set.lastOption=False
            EmulateFirst=CS()
            results =EmulateFirst.MainScheduler(jobList,Set.resources)
            first.append(results)

            #print("\n\n***Main:Emulate TSRA-last")
            Set.firstOptionOnly=False
            Set.MEO=False
            Set.lastOption=True
            EmulateLast=CS()
            results =EmulateLast.MainScheduler(jobList,Set.resources)
            last.append(results)



        """ Average of simulations """

        avgMeoFailed = sum(int(f) for f,s,u,g in meo)/float(Set.numberOfIteration)
        print("\navg Meo Failed: %",avgMeoFailed)
        avgMeoScaled = sum(int(s) for f,s,u,g in meo)/float(Set.numberOfIteration)
        print("avg Meo Scaled: %",avgMeoScaled)
        avgMeoUnused = sum(int(u) for f,s,u,g in meo)/float(Set.numberOfIteration)
        print("avg Meo Unused: %",avgMeoUnused)
        avgMeoGained = sum(int(g) for f,s,u,g in meo)/float(Set.numberOfIteration)
        print("avg Meo Gained Bid: %",avgMeoGained)

        avgFirstFailed = sum(int(f) for f,s,u,g in first)/float(Set.numberOfIteration)
        print("\navg First Failed: %",avgFirstFailed)
        avgFirstScaled = sum(int(s) for f,s,u,g in first)/float(Set.numberOfIteration)
        print("avg First Scaled: %",avgFirstScaled)
        avgFirstUnused = sum(int(u) for f,s,u,g in first)/float(Set.numberOfIteration)
        print("avg First Unused: %",avgFirstUnused)
        avgFirstGained = sum(int(g) for f,s,u,g in first)/float(Set.numberOfIteration)
        print("avg First Gained Bid: %",avgFirstGained)

        avgLastFailed = sum(int(f) for f,s,u,g in last)/float(Set.numberOfIteration)
        print("\navg Last Failed: %",avgLastFailed)
        avgLastScaled = sum(int(s) for f,s,u,g in last)/float(Set.numberOfIteration)
        print("avg Last Scaled: %",avgLastScaled)
        avgLastUnused = sum(int(u) for f,s,u,g in last)/float(Set.numberOfIteration)
        print("avg Last Unused: %",avgLastUnused)
        avgLastGained = sum(int(g) for f,s,u,g in last)/float(Set.numberOfIteration)
        print("avg Last Gained Bid: %",avgLastGained)

        print("\nnumber of iteration: ",Set.numberOfIteration,
              "| number of time interval: ", Set.NumberOfTimeInterval,
              "| each interval: ",Set.eachTimeInterval,
              "| avg Load: ", Set.avgSysLoad,
              "| random Job: ",Set.randJob)

        return ([avgMeoFailed,avgMeoGained,avgFirstFailed,avgFirstGained,avgLastFailed,avgLastGained],
                ["number of iteration: ",Set.numberOfIteration,
              "| number of time interval: ", Set.NumberOfTimeInterval,
              "| each interval: ",Set.eachTimeInterval,
              "| avg Load: ", Set.avgSysLoad,
              "| random Job: ",Set.randJob])

if __name__== '__main__':
    MainClass.mainMethod()