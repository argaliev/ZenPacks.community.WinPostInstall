threshold = context.getZ('cFileSystemThreshold')

if not threshold:
    return context.totalBlocks * context.blockSize / 1024 / 1024 * .1
 
logic_condition, actions = threshold.split('?')
value_if_true, value_if_false = actions.split(':')
sizeMB = context.totalBlocks * context.blockSize / 1024 / 1024
if logic_condition.startswith('>'):
    cmp_result = sizeMB > int(logic_condition[1:])
elif logic_condition.startswith('>='):
    cmp_result = sizeMB >= int(logic_condition[2:])
elif logic_condition.startswith('<'):
    cmp_result = sizeMB < int(logic_condition[1:])
elif logic_condition.startswith('<='):
    cmp_result = sizeMB <= int(logic_condition[2:])
elif  logic_condition.startswith('='):
    cmp_result = sizeMB == int(logic_condition[1:])
else:
    return context.totalBlocks * context.blockSize / 1024 / 1024 * .1

if cmp_result:
    method, value = value_if_true.split('=')
else:
    method, value = value_if_false.split('=')
if method == 'percent':
    return sizeMB * float(value) * 0.01
elif method == 'absolute':
    return float(value)
 
# If no prefixes match, default to a 10 percent.
return context.totalBlocks * context.blockSize / 1024 / 1024 * .1
