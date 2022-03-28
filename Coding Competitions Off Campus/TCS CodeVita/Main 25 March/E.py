'''

Worker 2
Problem Description
This is a resource to a task allocation problem. There are two types of tasks viz. one that the human needs to do and the other which is amenable to machine processing. A human-oriented task cannot be performed by a machine and vice-versa. Also, assume that all human workers are equally efficient. So, the same task will be performed in the same time, irrespective of which human worker does that task.

Given the number of workers, number of tasks, points awarded for every task completion and time taken to finish each task, compute the total number of points earned by every worker. Some rules and conventions that need to be adhered to while doing task allocation to workers are as follows.

Machine processing for any task takes 0 minutes
Time taken (in minutes) by a human worker to complete a particular task is mentioned in the input
Workers and tasks are identified by their suffixes i.e., Worker 1 is W1 and Task 1 is T1
Task information is provided in the input in form of a tuple that consists of 4 things viz. <Taskname, TaskType, Points, CompletionTime> where
Taskname will be of form T1, T2, T3 etc
TaskType will be a keyword which can be either Manual or Machine
Points is a reward given to a worker after completion of task
CompletionTime is a number denoting time in minutes needed for manual tasks and 0 for machine-bound tasks
A worker will still need to be assigned even if a task can be done only by the machine
Tasks need to be processed in sequential order i.e., T1 has to be allocated before T2
Initially when all workers are free, worker Wi will be allocated task before worker Wi+1 i.e., in general a worker with lower suffix will be assigned to the task before a worker with a higher suffix
If one or more workers are available at the same time, then the worker who processed lower suffix task will get the next task allocated prior to the other workers
Assume the switching time from one task to another as 0 min
Refer the Examples section for better understanding of how tasks are allocated to workers.

Compute the total number of points earned by each worker. The output specifications provide information on how output should be printed

Constraints
1 <= N <= 10

0 < M <= 100

Input
First line contains an integer N which denotes the number of workers.

Second line contains an integer M which denotes the number of tasks.

Next M lines contain a task information tuple as described in the previous section.

Output
Output should adhere to the following specifications:

Each output should be a tuple comprising of 2 pieces of information viz <Worker name, total number of points earned by that worker>
The tuple should be first sorted in descending order of points and then in ascending order of worker name
For better understanding refer to the Examples section.

Time Limit (secs)
1

Examples
Example 1

Input

3

4

T1 Machine 1

T2 Manual 6 5

T3 Machine 1

T4 Machine 1

Output

W2 6

W1 2

W3 1

Explanation:

Here, N=3 denotes number of workers W1, W2, W3.

First, Workers W1, W2, W3 will be assigned with tasks T1, T2, T3 at the 0th minute, respectively.

Here, T1 is Machine-bound so it will be completed in the 0th minute and W1 will be awarded 1 point. W1 will then be available for the remaining tasks. T2 is Manual and it will be completed in the 5th minute and W2 will be awarded 6 points. So, W2 will be free after 5 minutes. T3 again is Machine-bound so it will be completed in the 0th minute and W3 will be awarded 1 point. W3 will then be available for remaining tasks.

Now, Workers available for pending tasks in the 0th minute = {W1, W3}

Here, W1 will be assigned with the next pending task (T4) first, because the worker W1 completed the task with lower suffix (T1) than W3 (T3). W1 will then be awarded 1 point after completion of T4.

As the number of pending tasks is zero, no further assignment takes place.

W2 will complete T2 at the end of the 5th minute and will be awarded with 6 points.

Hence, Total number of points earned by each worker till now is:

W1 = 2

W2 = 6

W3 = 1

Hence, first line of output is "W2 6", where 6 is the number of total points earned by Worker W2.

Second line of output is "W1 2", where 2 is the number of total points earned by Worker W1.

Third line of output is "W3 1", where 1 is the number of total points earned by Worker W3.

So, the output is as follows:

W2 6

W1 2

W3 1

Example 2

Input

3

4

T1 Machine 1

T2 Machine 1

T3 Machine 1

T4 Machine 1

Output

W1 2

W2 1

W3 1

Explanation:

Given N = 3 denotes number of workers W1, W2 and W3

First, Workers W1, W2, W3 will be assigned with tasks T1, T2, T3 in the 0th minute, respectively.

Here, T1, T2 and T3 are Machine-bound and will be completed in the 0th minute and will be awarded 1 point each. After completion of these tasks, W1, W2, W3 will be available for the remaining tasks.

Since W1 is the first worker in the list of available workers at the 0th minute, W1 will pick up the T4 and will complete it in the 0th minute and will be awarded 1 point.

Total number of points earned by each worker till now is:

W1 = 2

W2 = 1

W3 = 1

Hence, first line of output is "W1 2", where 2 is the number of total points earned by Worker W1.

Second line of output is "W2 1", where 1 is the number of total points earned by Worker W2.

Third line of output is "W3 1", where 1 is the number of total points earned by Worker W3.

Hence the output is as follows:

W1 2

W2 1

W3 1

'''

def worker(n,m,tasks):


n=int(input())
m=int(input())
tasks=[]
for i in range(m):
    tasks.append(input().split())
