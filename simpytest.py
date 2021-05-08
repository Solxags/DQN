#
# """
# 银行排队服务例子
#
# 情景:
#   一个柜台对客户进行服务, 服务耗时, 客户等候过长会离开柜台
# """
#
# import random
# import simpy
#
#
# RANDOM_SEED = 42
# NEW_CUSTOMERS = 10# 客户数
# INTERVAL_CUSTOMERS = 1.0 # 客户到达的间距时间
# MIN_PATIENCE = 1 # 客户等待时间, 最小
# MAX_PATIENCE = 3 # 客户等待时间, 最大
#
# def source(env, number, interval, counter):
#     """进程用于生成客户"""
#     for i in range(number):
#         c = customer(env, 'Customer%02d' % i, counter, time_in_bank=12.0)
#         env.process(c)
#         yield env.timeout(1)
#
# def customer(env, name, counter, time_in_bank):
#     """一个客户表达为一个协程, 客户到达, 被服务, 然后离开"""
#
#     arrive = env.now
#     print('%7.4f %s: Here I am' % (arrive, name))
#
#     req=counter.request()
#     patience = 1
#     # 等待柜员服务或者超出忍耐时间离开队伍
#     results = yield req | env.timeout(patience)
#     wait = env.now - arrive
#
#     if req in results:
#         # 到达柜台
#         print('%7.4f %s: Waited %6.3f' % (env.now, name, wait))
#         tib = 2
#         yield env.timeout(tib)
#         counter.release(req)
#         print('%7.4f %s: Finished' % (env.now, name))
#     else:
#         # 没有服务到位
#         print('%7.4f %s: RENEGED after %6.3f' % (env.now, name, wait))
#
# # Setup and start the simulation
# print('Bank renege')
# random.seed(RANDOM_SEED)
# env = simpy.Environment()
#
# # Start processes and run
# counter = simpy.Resource(env, capacity=1)
# env.process(source(env, NEW_CUSTOMERS, INTERVAL_CUSTOMERS, counter))
# env.run()

#
# """
# 银行排队服务例子
#
# 情景:
#   一个柜台对客户进行服务, 服务耗时, 客户等候过长会离开柜台
# """
#
# import random
# import simpy
#
#
# RANDOM_SEED = 42
# NEW_CUSTOMERS = 10# 客户数
# INTERVAL_CUSTOMERS = 1.0 # 客户到达的间距时间
# MIN_PATIENCE = 1 # 客户等待时间, 最小
# MAX_PATIENCE = 3 # 客户等待时间, 最大
#
# def source(env, number):
#     """进程用于生成客户"""
#     for i in range(number):
#         customer_leave=env.event()
#         c = customer(env, 'Customer%02d' % i, customer_leave)
#         env.process(c)
#         yield customer_leave
#         print(2)
#
# def customer(env, name,  customer_leave):
#     """一个客户表达为一个协程, 客户到达, 被服务, 然后离开"""
#
#     arrive = env.now
#     print('%7.4f %s: Here I am' % (arrive, name))
#     yield env.timeout(1)
#     customer_leave.succeed()
#     print(1)
#
#
#
# # Setup and start the simulation
# print('Bank renege')
# random.seed(RANDOM_SEED)
# env = simpy.Environment()
#
# # Start processes and run
# env.process(source(env, NEW_CUSTOMERS))
# env.run()

for i in range(5):
  for j in range(5):
    print(i, j)
    if i == 3 and j == 3:
      break
  else:
    continue
  break