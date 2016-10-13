thresholds = context.getZ('cFileSystemThreshold')
default_threshold = None
 
# If no thresholds are set, default to a 10 percent.
if not hasattr(thresholds, 'append'): 
    return context.totalBlocks * context.blockSize / 1024 / 1024 * .1
 
for threshold in thresholds:
    prefix, method, value = threshold.split(':')
    if context.mount.startswith(prefix) and method == 'percent':
        return context.totalBlocks * context.blockSize / 1024 / 1024 * float(value) * 0.01
    if context.mount.startswith(prefix) and method == 'absolute':
        return float(value)
    if prefix == 'default' and method == 'percent':
        default_threshold = context.totalBlocks * context.blockSize / 1024 / 1024 * float(value) * 0.01
    if prefix == 'default' and method == 'absolute':
        default_threshold = float(value)
 
if default_threshold is not None:
    return default_threshold
# If no prefixes match, default to a 10 percent.
return context.totalBlocks * context.blockSize / 1024 / 1024 * .1
