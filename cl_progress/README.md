# cl_progress

## Usage

```bash
% python
>>> from cl_progress.cl_progress import *
>>>
>>> # True : process succeed (output [SUCCEED])
>>> # False: process failed (output [FAILED])
>>> progress("process 1", True)
process 1                                                                           [SUCCEED]
>>> progress("process 2", False)
process 2                                                                            [FAILED]
```
