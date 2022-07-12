# Given  sets of integers, M and N, print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both.


M = input()
M_list = input()
N= input()
N_list = input()

M_list = M_list.split()
M_newlist = list(map(int, M_list))
M_set = set(M_newlist)

N_list = N_list.split()
N_newlist = list(map(int, N_list))
N_set = set(N_newlist)

M_moin_N = M_set - N_set
N_moin_M = N_set - M_set
final = list(M_moin_N) + list(N_moin_M)

SORTED_LIST = sorted(final)
for i in SORTED_LIST:
    print(i)
