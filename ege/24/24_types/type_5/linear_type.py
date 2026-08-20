#
# data = "DSFS23543132S555"
# k = 5
# odds = "13579"
# max_len = 0
# for start in range(len(data)):
#     if not data[start] == "S":
#         continue
#     cnt_s = cnt_odds = 0
#     for end in range(start, len(data)):
#         if data[end] in odds:
#             cnt_odds += 1
#         if data[end] == "S":
#             cnt_s += 1
#
#         if cnt_odds > k:
#             break
#         if cnt_s > 1:
#             break
#         if cnt_odds == k and cnt_s == 1:
#             max_len = max(max_len, end - start + 1)
#
# print(max_len)


