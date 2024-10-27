# Results

Read + Write: increment (`+=`)

```
mb@DESKTOP-N0UU2KA:~/dev/workspace/my/Cengal$ /bin/python3 /home/mb/dev/workspace/my/Cengal/cengal/hardware/memory/shared_memory/versions/v_0/development/shared_memory_benchmark.py
Consumer is ready
<< Creator >>: 7001 messages put in 0.6714376746676862 seconds. MPS: 10426.87990879421. Wait time: 0.11812437803018838
<< Consumer >>: 7000 messages taken in 0.11776620231103152 seconds. MPS: 59439.80414272295. Wait time: 0.6642624932574108
<< Creator >>: puting an IList
<< Consumer >>: waiting for an IList
<< Creator >>: waiting for the list to be changed by the consumer
<< Consumer >>: adding elements to the list
<< Consumer >>: waiting for the list to be changed by the creator
<< Creator >>: changing list
<< Creator >>: saving working list into a variable
<< Consumer >>: saving working list into a variable
<< Consumer >>: concurently adding elements to the list
<< Creator >>: concurently adding elements to the list
<< Consumer >>: 1045184.222300395. Starting adding elements to the list
<< Creator >>: 1045184.2223246356. Starting adding elements to the list
<< Creator >>: alloc_dtime=0.0
<< Creator >>: 1045186.8859652659. Finished adding elements to the list
<< Creator >>: 2000000 additions made in 1.3003784291213378 seconds. APS: 1538013.8236770004. Wait time: 1.3472807867219672
<< Creator >>: 2000000 additions made in 1.2973417468601838 seconds. APS: 1541613.846035853
<< Consumer >>: alloc_dtime=0.0
<< Consumer >>: 1045186.8998893033. Finished adding elements to the list
<< Consumer >>: 2000000 additions made in 1.376771113020368 seconds. APS: 1452674.2906541592. Wait time: 1.3006884984206408
<< Consumer >>: 2000000 additions made in 1.3735054127173498 seconds. APS: 1456128.2259843375
```

Read or Write: assignment (`=`)

```
mb@DESKTOP-N0UU2KA:~/dev/workspace/my/Cengal$ /bin/python3 /home/mb/dev/workspace/my/Cengal/cengal/hardware/memory/shared_memory/versions/v_0/development/shared_memory_benchmark.py
Consumer is ready
<< Creator >>: 7001 messages put in 0.6546518480172381 seconds. MPS: 10694.233921746529. Wait time: 0.11777839704882354
<< Consumer >>: 7000 messages taken in 0.11758282338269055 seconds. MPS: 59532.50482187754. Wait time: 0.6508834027918056
<< Creator >>: puting an IList
<< Consumer >>: waiting for an IList
<< Creator >>: waiting for the list to be changed by the consumer
<< Consumer >>: adding elements to the list
<< Consumer >>: waiting for the list to be changed by the creator
<< Creator >>: changing list
<< Creator >>: saving working list into a variable
<< Consumer >>: saving working list into a variable
<< Creator >>: concurently adding elements to the list
<< Creator >>: 1046550.7621118738. Starting adding elements to the list
<< Consumer >>: concurently adding elements to the list
<< Consumer >>: 1046550.7695078929. Starting adding elements to the list
<< Consumer >>: alloc_dtime=0.0
<< Consumer >>: 1046552.0208049886. Finished adding elements to the list
<< Consumer >>: 2000000 additions made in 0.6520137328188866 seconds. APS: 3067420.054717698. Wait time: 0.5602756307926029
<< Consumer >>: 2000000 additions made in 0.6513118222355843 seconds. APS: 3070725.774844887
<< Creator >>: alloc_dtime=0.0
<< Creator >>: 1046552.0529665485. Finished adding elements to the list
<< Creator >>: 2000000 additions made in 0.6311954219127074 seconds. APS: 3168590.789108408. Wait time: 0.6522154993144795
<< Creator >>: 2000000 additions made in 0.6304945176234469 seconds. APS: 3172113.2287378097
```
