"""
https://en.wikipedia.org/wiki/Unix_time
Answer 1:
At 03:14:08 UTC on Tuesday, 19 January 2038, 32-bit versions of the Unix time stamp will cease to work,
as it will overflow the largest value that can be held in a signed 32-bit number (7FFFFFFF16 or 2,147,483,647).
Before this moment, software using 32-bit time stamps will need to adopt a new convention for time stamps,[25] and
file formats using 32-bit time stamps will need to be changed to support larger time stamps or a different epoch.
If unchanged, the next second will be incorrectly interpreted as 20:45:52 Friday 13 December 1901 UTC.

Answer 2:
At 06:28:15 UTC on Sunday, 7 February 2106, the Unix time will reach FFFFFFFF16 or 4,294,967,295 seconds which,
for systems that hold the time on 32-bit unsigned integers, is the maximum attainable.
For these systems, the next second will be incorrectly interpreted as 00:00:00 Thursday 1 January 1970 UTC.

Answer 3:
At 15:30:08 UTC on Sunday, 4 December 292,277,026,596 (should that date happen),[26][27] 64-bit versions of the Unix time stamp would cease to work,
as it will overflow the largest value that can be held in a signed 64-bit number.
This is nearly 22 times the estimated current age of the universe,
which is 1.37×1010 years (13.7 billion).
"""
print("Read the comments to see the answer to this question.")
