#!/bin/bash
# This script calculates simple interest given principal,
# annual rate of interest and time period in years.
# Do not use this in production. Sample purpose only.
# Author: Upkar Lidder (IBM)

# Additional Authors:
# RadwaSawy

# Input:
# p, principal amount
# t, time period in years
# r, annual rate of interest

# Output:
# simple interest = p*t*r

echo &quot;Enter the principal:&quot;
read p
echo &quot;Enter rate of interest per year:&quot;
read r
echo &quot;Enter time period in years:&quot;
read t

s=`expr $p \* $t \* $r / 100`
echo &quot;The simple interest is: &quot;
echo $s
