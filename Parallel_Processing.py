""" This program calculates time required by the computer to process file with n
number of lines."""
file = 5
num_lines_files = [4,2,7,8.6]
num_cores = 5
limit = 4
to_process = [x[:limit] for x in num_lines_files]
time = sum(to_process)/num_cores
print(time)