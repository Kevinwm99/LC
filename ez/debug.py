# 10/11/2020 array intersection 2

# attempt 1
# from collections import defaultdict
# nums1 = [1,2,2,1]
# nums2 = [4,2,2]
# d = defaultdict(int)
# for i in nums1:
#     d[i]+=1
# nums1 = []
# for i in nums2:
#     old = d[i]
#     d[i]+=1
#     if d[i]>old:
#         pass

# atempt 2
# from collections import defaultdict
# nums1 = [1,1,2,2]
# nums2 = [2,2]
# d = defaultdict(int)
# for i in nums1:
#     d[i]+=1
# d2 = defaultdict(int)
# for i in nums2:
#     # old = d[i]
#     d2[i]+=1
#     # if old !=0:
#     #     num1.append(i)
# num1=[]
# for i in d:
#     try:
#         a = d2[i]
#         b = d[i]
#         if a == d[i]:
#             if a == 1:
#                 num1.append(i)
#             else:
#                 for j in range(a):
#                     num1.append(i)
#         elif a<d[i]:
#             if a == 1:
#                 num1.append(i)
#             else:
#                 for j in range(a):
#                     num1.append(i) 
#         else:
#             if d[i]==1:
#                 num1.append(i)
#             else:
#                 for j in range(d[i]):
#                     num1.append(i)
#     except:
#         pass
        #success :)     run time faster than 94%, memory less than 100%
# could improve by using min(a,d[i]) and we can eliminate the try except
# the rewrite code will be
        # for i in d:
        #     a = d2[i]
        #     n = min(a,d[i])
        #     if n !=0:
        #         for j in range(n):
        #             nums1.append(i)
