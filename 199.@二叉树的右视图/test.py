rightmost_value_at_depth = dict() # 深度为索引，存放节点的值
depth = 1
node = 1
rightmost_value_at_depth.setdefault(depth, node)
print(rightmost_value_at_depth)
depth = 1
node = 2
rightmost_value_at_depth.setdefault(depth, node)
print(rightmost_value_at_depth)