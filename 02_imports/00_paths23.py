import sys,os
print('sys.path[0] ====>', os.path.join(sys.path[0], 'bar', 'baz'))
print('dirname ========>', os.path.join(os.path.dirname(sys.path[0]), 'bar', 'baz'))
