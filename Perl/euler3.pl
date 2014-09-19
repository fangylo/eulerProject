#!/usr/bin/env perl
use warnings;
use strict; 

sub largestPrimeFactor
{
  my $largestFactor = 1;
  my $numberToCheck = $_[0]; 
  my $maxNumber = sqrt($numberToCheck);
  my $newMaxNumber = $maxNumber;
  for (my $i = 2; $i <= $maxNumber; $i ++) 
  {
    if ($i > $newMaxNumber) 
    {
      last;
    }
    
    while ($numberToCheck % $i == 0)
    {
      $largestFactor = $i;
      $numberToCheck = $numberToCheck/$i;
      $newMaxNumber = sqrt($numberToCheck);
    }
  }
  
  if ($numberToCheck > $largestFactor)
  {
    $largestFactor = $numberToCheck;
  }
  return $largestFactor;
}


my $result = largestPrimeFactor(600851475143);
print $result;

