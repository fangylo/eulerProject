#!/usr/bin/env perl
use warnings;
use strict; 

sub fibonacciGenerator
{
  my $max = @_[0]; 
  my $num1 = 1;
  my $num2 = 2;
  my $nextNumber = 0;
  my @resultArray = (1,2);
  while (($num1+$num2)<= $max)
  {
    $nextNumber = $num1+$num2;
    $num1 = $num2;
    $num2 = $nextNumber;
    push (@resultArray, $num2);
  }
  return @resultArray;
}

sub sumOfEvenNumbers
{
  my @listOfNumbers = @_;
  my $total = 0;
  foreach (@listOfNumbers)
  {
    if ($_%2==0)
    {
      $total+=$_;
    }
  }
  return $total;
}


my @result = fibonacciGenerator(4000000);
my $total = sumOfEvenNumbers(@result);
print $total;

