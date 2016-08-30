-> intro    -> data hierachy    -> files and streams
-> creating a sequential-access file
-> file modes   -> funcs for file
-> creating, reading, writing/updating a sequential file
-> working with directories -> random access file
-> command line arguments

-> python views files as sequential stream of bytes
-> each file ends with end-of-file marker
-> opening a file creates a obj associated with a stream
-> Three file streams created when python program executes
sys.stdin       sys.stdout      sys.stderr

-> file modes
a r r+ w w+ ab rb r+b wb w+b

-> methods for file operation
close() fileno() flush() isatty() read([size]) readline([size])
readlines([size]) seek(offset[location]) tell() truncate([size])
write(output) writelines(outputList) xreadlines()

-> methods to work with directories
mkdir chdir getcwd rename remove rmdir