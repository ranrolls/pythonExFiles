-> intro -> parent/child communication using fork()
-> command execution using system() and exec()
-> Exec family function
-> Controlling process input and output
-> Inter - process communcation
-> Signal Handling
-> Sending and Receiving Signals

-> implement concurrency by having each task ( or process ) operate in a seperate memory space
-> Time slicing on single processor systems divides processor time among many processes
-> operating system allocates a short execution time called a quantum to a process
-> operation system perfoms context switching to move processes and the dependent data in and out of memory
-> operating system provides shells - programs that execute system commands on user's behalf
-> Some operating system have build-in system commands that enable programmers to create and manage processes ( e.g. Portable operating system interface in Unix naming POSIX )

function os.fork, available only on POSIX-complaint systems, creates new process
parent process invokes os.fork
parent process forks ( creates ) a child process
each process has a unique identifying process id number (pid)
function os.fork's return value
    0 for child process
    child's pid for parent
    
1. parent process executes
2. parent process calls os.fork and assigns return value to forkPID
( parent process forkPID is child's pid)
3. Parent and child processes execute same program simultaneously

