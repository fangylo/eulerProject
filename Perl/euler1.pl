#!/usr/bin/env perl
use warnings;
use strict; 

my $count =0;
my $total = 0;

while ($count <1000)
{
  if ($count % 3 ==0 or $count %5 ==0)
  {
    $total += $count;
  }
  $count ++;
}
print $total;