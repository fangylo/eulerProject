#!/usr/bin/env perl
use warnings;
use strict; 
use List::Util qw(max);

sub isPanlindrome
{
    my $inputNumber = $_[0];
    my $inputStr = sprintf("%d",$inputNumber);

    if (reverse($inputStr) eq $inputStr)
    {
        return 1;
    }
    else
    {
      return 0;
    }
}


sub findMaxPalindrome
{
  my @palindromeList = ();
  
  for (my $i = 999; $i > 100; $i-- )
  {
    for (my $j = 999; $j >100; $j--)
    {
      if ( $i >= $j)
      {
        my $product = $i * $j;
        if (isPanlindrome($product))
        {
          # print $product;
          # print "\n";
          push (@palindromeList, $product);
          # print @palindromeList;
        }        
      }
    }
  }
  return max(@palindromeList);
}

my $result = findMaxPalindrome();
print $result;

